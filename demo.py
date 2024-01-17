from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#SQLite configuration (replace 'example.db' with your desired database name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Health Insurance Plan model
class HealthInsurance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    plan = db.Column(db.String(50), nullable=False)
    pan = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(50), nullable=False)
    nominee_name = db.Column(db.String(50), nullable=False)
    nominee_gender = db.Column(db.String(50), nullable=False)
    proposer_name = db.Column(db.String(50), nullable=False)




@app.route('/store_health_data', methods=['POST'])
def store_health_data():
    # Get data from the request
    data = request.json

    # Create a new HealthInsurance instance
    new_health_data = HealthInsurance(
        name=data['name'],
        age=data['age'],
        mobile=data['mobile'],
        email=data['email'],
        gender=data['gender'],
        plan=data['plan'],
        pan=data['pan'],
        dob=data['dob'],
        nominee_name=data['nominee_name'],
        nominee_gender=data['nominee_gender'],
        proposer_name=data['proposer_name']
    )

    # Add and commit the new data to the database
    db.session.add(new_health_data)
    db.session.commit()

    return jsonify({"message": "Health data stored successfully"}), 201


if __name__ == '__main__':
    with app.app_context():
        # Create tables within the context of the Flask application
        db.create_all()
    # Create tables before running the app
    # db.create_all()
    app.run(debug=True)
