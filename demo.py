from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# SQLite configuration (replace 'example.db' with your desired database name)
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
    proposer_gender = db.Column(db.String(50), nullable=False)
    nominee_details = db.Column(db.String(50), nullable=False)


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
        nominee_details=data['nominee_details'],
        nominee_gender=data['nominee_gender'],
        proposer_name=data['proposer_name'],
        proposer_gender=data['proposer_gender']
    )

    # Add and commit the new data to the database
    db.session.add(new_health_data)
    db.session.commit()

    return jsonify({"message": "Health data stored successfully"}), 201


@app.route('/get_health_data', methods=['GET'])
def get_health_data():
    health_data = HealthInsurance.query.all()
    data_list = []
    for data in health_data:
        data_list.append({
            'name': data.name,
            'age': data.age,
            'mobile': data.mobile,
            'email': data.email,
            'gender': data.gender,
            'plan': data.plan,
            'pan': data.pan,
            'dob': data.dob,
            'nominee_name': data.nominee_name,
            'nominee_gender': data.nominee_gender,
            'proposer_name': data.proposer_name,
            'nominee_details': data.nominee_details,
            'proposer_gender': data.proposer_gender
        })
    return jsonify({"health_data": data_list})


@app.route('/get_health_data_by_mobile/<mobile>', methods=['GET'])
def get_health_data_by_mobile(mobile):
    health_data = HealthInsurance.query.filter_by(mobile=mobile).first()
    if health_data:
        return jsonify({
            'name': health_data.name,
            'age': health_data.age,
            'mobile': health_data.mobile,
            'email': health_data.email,
            'gender': health_data.gender,
            'plan': health_data.plan,
            'pan': health_data.pan,
            'dob': health_data.dob,
            'nominee_name': health_data.nominee_name,
            'nominee_gender': health_data.nominee_gender,
            'proposer_name': health_data.proposer_name,
            'nominee_details': health_data.nominee_details,
            'proposer_gender': health_data.proposer_gender
        })
    else:
        return jsonify({"message": "Health data not found for the given mobile number"}), 404


@app.route('/delete_health_data_by_mobile/<mobile>', methods=['DELETE'])
def del_health_data(mobile):
    health_data = HealthInsurance.query.filter_by(mobile=mobile).first()
    if health_data:
        db.session.delete(health_data)
        db.session.commit()
        return jsonify({"message": "Health data deleted successfully"}), 200
    else:
        return jsonify({"message": "Health data not found for the given mobile number"}), 404


if __name__ == '__main__':
    with app.app_context():
        # Create tables within the context of the Flask application
        db.create_all()
    # Create tables before running the app
    # db.create_all()
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 443))
    app.run(host='0.0.0.0', port=port, debug=True)
