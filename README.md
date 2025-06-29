🗓️ Event Scheduler - Flask Web Application
A simple yet functional Event Scheduler web application built with Flask, featuring:

✅ Event Creation & Management
✅ Upcoming & Completed Event Filters
✅ REST API for external access (tested via Postman)
✅ Event Reminders for upcoming events (within 24 hours)
✅ Persistent JSON storage for events

📦 Project Features
Add, edit, delete events via Web UI

Mark events as completed

Filter events (All, Upcoming, Completed)

JSON-based data storage (no database setup required)

REST API with endpoints for integration

Background reminder system alerts for upcoming events

Simple, user-friendly HTML interface

⚙️ Tech Stack
Python 3

Flask

HTML, CSS (Basic Styling)

JSON for data storage

Postman for API testing

Threading for background reminders

🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone your-repo-link
cd event-scheduler
2. Install Dependencies
bash
Copy
Edit
pip install flask
3. Run the Application
bash
Copy
Edit
python app.py
4. Access the Application
Open your browser and go to:
http://127.0.0.1:5000 (or your-local-url)

🔌 API Endpoints
1. Get All Events
http
Copy
Edit
GET /api/events
2. Create Event
http
Copy
Edit
POST /api/events
Request Body (JSON):

json
Copy
Edit
{
  "title": "Meeting",
  "Description": "Project Discussion",
  "start_time": "YYYY-MM-DD HH:MM",
  "end_time": "YYYY-MM-DD HH:MM"
}
3. Update Event
http
Copy
Edit
PUT /api/events/<index>
4. Delete Event
http
Copy
Edit
DELETE /api/events/<index>
5. Get Upcoming Events
http
Copy
Edit
GET /api/events/upcoming
6. Get Completed Events
http
Copy
Edit
GET /api/events/completed
🛠️ Screenshots
(Add screenshots of your Web UI and Postman responses here if available)

📂 Postman Collection
The Postman collection for API testing is included in the repo as:
event_scheduler_postman_collection.json

💡 Future Enhancements
Improved UI with Bootstrap or Tailwind CSS

Toast notifications for actions

Database integration (SQLite or MongoDB)

Email or SMS reminders

Streamlit or React frontend

✨ Author
Hemalatha Vallabhaneni
Aspiring Data Scientist & Python Developer

