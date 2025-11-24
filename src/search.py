#searching trips
from . import db

TRIPS = "trips"
VEHICLES = "vehicles"
RESERVATIONS = "reservations"

def list_trips():
    return db.read(TRIPS)

def find_trips(origin=None, destination=None, date=None):
    trips = list_trips()
    results = []
    for t in trips:
        if origin and t["origin"].lower() != origin.lower():
            continue
        if destination and t["destination"].lower() != destination.lower():
            continue
        if date and t["date"] != date:
            continue
        results.append(t)
    return results

def seats_available(trip_id):
    trips = db.read(TRIPS)
    vehicles = db.read(VEHICLES)
    reservations = db.read(RESERVATIONS)
    trip = next((t for t in trips if t["trip_id"] == trip_id), None)
    if not trip:
        return 0
    vehicle = next((v for v in vehicles if v["vehicle_id"] == trip["vehicle_id"]), None)
    if not vehicle:
        return 0
    cap = int(vehicle["capacity"])
    booked = sum(r["seats"] for r in reservations if r["trip_id"] == trip_id)
    return max(0, cap - booked)
