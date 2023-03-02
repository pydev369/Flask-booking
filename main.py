from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# set up database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# define appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Appointment %r>' % self.name

# define API routes
@app.route('/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify([{'id': a.id, 'name': a.name, 'email': a.email, 'date': a.date, 'time': a.time} for a in appointments])

@app.route('/appointments', methods=['POST'])
def create_appointment():
    name = request.json['name']
    email = request.json['email']
    date = request.json['date']
    time = request.json['time']
    appointment = Appointment(name=name, email=email, date=date, time=time)
    db.session.add(appointment)
    db.session.commit()
    return jsonify({'id': appointment.id, 'name': appointment.name, 'email': appointment.email, 'date': appointment.date, 'time': appointment.time})

# deploy to AWS Lambda
def lambda_handler(event, context):
    response = app.response_class(status=200)
    with app.app_context():
        app.dispatch_request(event, context)
    return response
