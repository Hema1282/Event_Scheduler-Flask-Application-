🗓️ Event Scheduler - Flask Web Application


The Event Scheduler is a simple yet functional web application that allows users to create, manage, and track events easily. It provides both a user-friendly web interface and REST API access for event management.This project is ideal for understanding how to build a real-world Flask application with basic backend logic, form handling, API development, and background tasks.

📦 Project Overview


 1.The Event Scheduler enables users to:

 2.Add new events with details like title, description, start time, and end time.

 3.View all scheduled events in one place.

 4.Edit or delete events when required.

 5.Mark events as completed once finished.

 6.Filter events based on their status: Upcoming or Completed.

 7.Receive console reminders for events that are due within the next 24 hours.

 8.Access and interact with the system programmatically through REST API endpoints.

 9.Event details are stored persistently using a simple JSON file, so the data remains intact even after restarting the application.

⚙️ Technology Stack
 -> Python

 -> Flask (Web framework)

 -> HTML, CSS (Basic interface)

 -> JSON (For data storage)

 -> Threading (For background reminders)

 -> Postman (For API testing)

💻 Project Requirements
To run this project successfully, you need:

* Python installed on your system

* Flask library installed (can be done using pip)

* Basic understanding of how to run Python scripts

* A web browser (to access the interface)

* Postman or similar tools (optional, for API testing)

🚀 Key Functionalities
 -> Web-based interface to easily create and manage events

 -> Data is stored in a JSON file - no external database required

 -> API endpoints to perform all actions programmatically

 -> Prevents creation of events in the past

 -> Prevents editing of completed events

 -> Console alerts for upcoming events within 24 hours

 ->Filtering options to easily view only upcoming or completed events


