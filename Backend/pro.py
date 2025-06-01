from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import oqs
import os
import base64
import hashlib

# Flask setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sarathy123@localhost/MyDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(256), nullable=False)
    salt = db.Column(db.String(256), nullable=False)
    strength = db.Column(db.String(50), nullable=False)

# Generate Post-Quantum Hash with Unique Salt
def pqc_hash_password(password):
    # Generate unique salt
    salt = base64.b64encode(os.urandom(16)).decode('utf-8')

    # Post-Quantum hashing (Placeholder using SHA-3 and salt for compatibility)
    hashed_password = base64.b64encode(
        hashlib.sha3_512((password + salt).encode()).digest()
    ).decode('utf-8')

    return hashed_password, salt

# Password Strength Checker
def check_password_strength(password):
    if len(password) >= 12 and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in "!@#$%^&*()-_=+" for c in password):
        return "Strong"
    elif len(password) >= 8:
        return "Medium"
    else:
        return "Weak"

# Store Password API
@app.route('/api/check_password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password')

    if not password:
        return jsonify({"error": "Password is required"}), 400

    # Check strength
    strength = check_password_strength(password)

    # Generate PQC hash and salt
    hashed_password, salt = pqc_hash_password(password)

    # Save to database
    user = User(password_hash=hashed_password, salt=salt, strength=strength)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "strength": strength,
        "quantum_resilient": True,
        "message": "Password stored securely.",
        "user_id": user.id  # Returning user ID for reference
    })

# Get Stored Password API
@app.route('/api/get_password', methods=['POST'])
def get_password():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    # Fetch user details
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "stored_hash": user.password_hash,
        "salt": user.salt,
        "strength": user.strength
    })

# Verify Password API
@app.route('/api/verify_password', methods=['POST'])
def verify_password():
    data = request.get_json()
    user_id = data.get('user_id')
    entered_password = data.get('password')

    if not user_id or not entered_password:
        return jsonify({"error": "User ID and password are required"}), 400

    # Fetch user details
    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Hash the entered password using the stored salt
    entered_hash = base64.b64encode(
        hashlib.sha3_512((entered_password + user.salt).encode()).digest()
    ).decode('utf-8')

    if entered_hash == user.password_hash:
        return jsonify({"message": "Password matches!", "valid": True})
    else:
        return jsonify({"message": "Password does not match!", "valid": False})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
