
#booking and cancellation

from . import db, models, search
import uuid

TRIPS = "trips"
RESERVATIONS = "reservations"

def create_reservation(username, trip_id, seats):
    seats = int(seats)
    avail = search.seats_available(trip_id)
    if seats <= 0:
        raise ValueError("invalid_seat_count")
    if seats > avail:
        raise ValueError("not_enough_seats")
    reservations = db.read(RESERVATIONS)
    res_id = "R-" + uuid.uuid4().hex[:8].upper()
    res = models.make_reservation(res_id, trip_id, username, seats)
    reservations.append(res)
    db.write(RESERVATIONS, reservations)
    return res

def cancel_reservation(reservation_id, username):
    reservations = db.read(RESERVATIONS)
    r = next((x for x in reservations if x["reservation_id"] == reservation_id), None)
    if not r:
        raise ValueError("reservation_not_found")
    if r["username"] != username:
        raise ValueError("not_permitted")
    reservations = [x for x in reservations if x["reservation_id"] != reservation_id]
    db.write(RESERVATIONS, reservations)
    return True

def user_reservations(username):
    reservations = db.read(RESERVATIONS)
    return [r for r in reservations if r["username"] == username]
