
# simple model classes represented as dictionaries

import hashlib
from datetime import datetime

def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def make_user(username, password, student_id, is_admin=False):
    return {
        "username": username,
        "password_hash": hash_password(password),
        "student_id": student_id,
        "is_admin": bool(is_admin),
        "created_at": datetime.utcnow().isoformat()
    }

def make_vehicle(vehicle_id, vehicle_type, capacity, notes=""):
    return {
        "vehicle_id": vehicle_id,
        "type": vehicle_type,  # "bus" or "train"
        "capacity": int(capacity),
        "notes": notes
    }

def make_trip(trip_id, vehicle_id, origin, destination, date, time, fare):
    return {
        "trip_id": trip_id,
        "vehicle_id": vehicle_id,
        "origin": origin,
        "destination": destination,
        "date": date,  # YYYY-MM-DD
        "time": time,  
        "fare": float(fare),
        "created_at": datetime.utcnow().isoformat()
    }

def make_reservation(res_id, trip_id, username, seats):
    return {
        "reservation_id": res_id,
        "trip_id": trip_id,
        "username": username,
        "seats": int(seats),
        "created_at": datetime.utcnow().isoformat()
    }
