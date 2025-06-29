from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import datetime
import threading
import time
import os

#Initialize the flask app
app = Flask(__name__)

# Load events from JSON file if exists,else initialize empty json list
if os.path.exists('events.json'):
    with open('events.json') as f:
        try:
            events = json.load(f)
        except json.JSONDecodeError:
            events = []
else:
    events = []

#Function to save events to JSON file
def save_events():
    with open('events.json', 'w') as f:
        json.dump(events, f)

#Function to sort the events by start time
def sort_events():
    global events
    events.sort(key=lambda x: x['start_time'])

#Function to check for upcoming eventsand print alerts
def check_reminders():
    while True:
        current_time = datetime.datetime.now()
        for event in events:
            if event.get("status") == "Completed":
                continue
            start_time = datetime.datetime.strptime(event['start_time'], '%Y-%m-%d %H:%M')
            if 0 < (start_time - current_time).total_seconds() <= 86400:
                print(f"[ALERT] Event '{event['title']}' is due soon!")
        time.sleep(60)

#Start background thread to continously check reminders
thread = threading.Thread(target=check_reminders)
thread.daemon = True
thread.start()

# ---------------- API ROUTES FOR POSTMAN --------------------

#API to get all events
@app.route('/api/events', methods=['GET'])
def get_events_api():
    return jsonify(events)

#API to create new event
@app.route('/api/events', methods=['POST'])
def create_event_api():
    event = {
        'title': request.json['title'],
        'Description': request.json['Description'],
        'start_time': request.json['start_time'],
        'end_time': request.json['end_time'],
        'status': 'To be Completed'
    }
    event_date = datetime.datetime.strptime(event['start_time'], '%Y-%m-%d %H:%M')
    current_time = datetime.datetime.now()

    #Prevents event creation in past
    if event_date < current_time:
        return jsonify({"Message": "Event date is in the past, cannot create event"}), 400
    else:
        events.append(event)
        sort_events()
        save_events()
        return jsonify({'Message': 'Event created successfully'}), 201

#API to update an event by index
@app.route('/api/events/<int:index>', methods=['PUT'])
def update_event_api(index):
    if 0 <= index < len(events):
        event = events[index]
        
        #Not allowing updates to completed events
        if event.get('status') == 'Completed':
            return jsonify({"Message": "Cannot update a completed event"}), 400

        # Allow updates only for upcoming events
        event['title'] = request.json.get('title', event['title'])
        event['Description'] = request.json.get('Description', event['Description'])
        event['start_time'] = request.json.get('start_time', event['start_time'])
        event['end_time'] = request.json.get('end_time', event['end_time'])
        event['status'] = request.json.get('status', event['status'])
        
        save_events()
        return jsonify({'Message': 'Event updated successfully'})
    else:
        return jsonify({'Message': 'Event not found'}), 404


#API to delete event by index
@app.route('/api/events/<int:index>', methods=['DELETE'])
def delete_event_api(index):
    if 0 <= index < len(events):
        del events[index]
        save_events()
        return jsonify({'Message': "Event deleted successfully"})
    else:
        return jsonify({'Message': 'Event not found'}), 404
    

# Get Upcoming Events via API
@app.route('/api/events/upcoming', methods=['GET'])
def get_upcoming_events():
    upcoming = [e for e in events if e['status'] == 'To be Completed']
    return jsonify(upcoming)

# Get Completed Events via API
@app.route('/api/events/completed', methods=['GET'])
def get_completed_events():
    completed = [e for e in events if e['status'] == 'Completed']
    return jsonify(completed)


# ---------------- HTML UI ROUTES --------------------

#Home page-shows all events
@app.route('/')
def index():
    sort_events()
    return render_template('index.html', events=events)


#Route to create new event via html form
@app.route('/create', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        event_date = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
        current_time = datetime.datetime.now()
 
       #prevent creation of events in the past
        if event_date < current_time:
            return "<script>alert('Cannot create event in the past!'); window.history.back();</script>"

        event = {
            'title': title,
            'Description': description,
            'start_time': start_time.replace('T', ' '),
            'end_time': end_time.replace('T', ' '),
            'status': 'To be Completed'
        }

        events.append(event)
        sort_events()
        save_events()
        return "<script>alert('Event Created Successfully!'); window.location.href='/'</script>"

    return render_template('create_event.html')

#Route to mark event is completed
@app.route('/mark_completed/<int:index>', methods=['POST'])
def mark_completed(index):
    if 0 <= index < len(events):
        events[index]['status'] = 'Completed'
        save_events()
    return redirect(url_for('index'))

#Route to delete an event
@app.route('/delete/<int:index>', methods=['POST'])
def delete_event(index):
    if 0 <= index < len(events):
        del events[index]
        save_events()
    return redirect(url_for('index'))

#Route to filter events(upcoming,completed, or all)
@app.route('/filter/<string:filter_type>')
def filter_events(filter_type):
    filtered = []
    if filter_type == 'upcoming':
        filtered = [e for e in events if e['status'] == 'To be Completed']
    elif filter_type == 'completed':
        filtered = [e for e in events if e['status'] == 'Completed']
    else:
        filtered = events
    return render_template('index.html', events=filtered)

#Route to editin an existing event
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_event(index):
    if index >= len(events):
        return "<script>alert('Event not found!'); window.location.href='/'</script>"
    event=events[index]

    #Prevent editing of completed events
    if event.get('status') =='Completed':
        return "<script>alert('Cannot edit a completed event!');window.location.href='/'</script>"
    
    if request.method == 'POST':
        events[index]['title'] = request.form['title']
        events[index]['Description'] = request.form['description']
        events[index]['start_time'] = request.form['start_time'].replace('T', ' ')
        events[index]['end_time'] = request.form['end_time'].replace('T', ' ')
        sort_events()
        save_events()
        return "<script>alert('Event Updated Successfully!'); window.location.href='/'</script>"

    event = events[index]
    return render_template('edit_event.html', event=event, index=index)

# ----Main entry Point

if __name__ == '__main__':
    app.run(debug=True)
