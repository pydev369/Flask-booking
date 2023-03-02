# Flask-booking

# Flask Appointment Booking App

![Appointment Booking App Demo](demo.gif)

## Description

This is a Flask web application for booking appointments. It utilizes SQLAlchemy to communicate with a PostgreSQL database, which stores appointment information such as the date, time, and customer information.

The app is deployed on AWS Lambda using the Serverless framework. It is designed to scale easily and handle a large volume of appointment bookings.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/flask-appointment-booking-app.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables:
    - `DATABASE_URI`: URI for the PostgreSQL database
    - `SECRET_KEY`: Secret key for Flask sessions
4. Create the database schema: `python create_db.py`
5. Deploy the app to AWS Lambda: `serverless deploy`

## Usage

Once the app is deployed, navigate to the provided URL to access the appointment booking interface. Customers can view available dates and times, select a time slot, and provide their contact information to book an appointment.

The app also provides an admin interface for managing appointments. Admins can view all booked appointments, mark them as complete, and delete appointments as needed.

## Technologies Used

- Flask
- SQLAlchemy
- PostgreSQL
- AWS Lambda
- Serverless Framework

## Credits

This app was created by [Soumendu Pal](https://github.com/pydev369).

