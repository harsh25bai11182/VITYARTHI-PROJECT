
from src import db, auth, search, reservation, models, utils
import os, sys

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

def seed_sample_data():

    vehicles = db.read("vehicles")
    trips = db.read("trips")
    if not vehicles:
        vehicles = [
            models.make_vehicle("V-BUS-01", "bus", 40, "Campus Shuttle"),
            models.make_vehicle("V-TRAIN-01", "train", 120, "Intercity special")
        ]
        db.write("vehicles", vehicles)
    if not trips:
        trips = [
            models.make_trip("T1", "V-BUS-01", "Campus Gate A", "Hostel Block 1", "2025-11-28", "08:00", 0.0),
            models.make_trip("T2", "V-TRAIN-01", "College Station", "City Central", "2025-12-01", "06:30", 50.0)
        ]
        db.write("trips", trips)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    auth.ensure_admin_exists()
    seed_sample_data()
    user = None
    while True:
        clear_screen()
        print("=== College Transport Reservation System ===")
        if not user:
            print("1. Register")
            print("2. Login")
            print("0. Exit")
            choice = input("Choose: ").strip()
            if choice == "1":
                username = input("username: ").strip()
                password = input("password: ").strip()
                student_id = input("student id: ").strip()
                try:
                    auth.register(username, password, student_id)
                    print("Registered. You can login now.")
                except Exception as e:
                    print("Error:", e)
                input("enter to continue...")
            elif choice == "2":
                username = input("username: ").strip()
                password = input("password: ").strip()
                u = auth.login(username, password)
                if u:
                    user = u
                    print("Logged in as", user["username"])
                else:
                    print("invalid credentials")
                input("enter to continue...")
            elif choice == "0":
                print('bye')
                sys.exit(0)
            else:
                print("Invalid")
                input("enter to continue...")
        else:
            clear_screen()
            print(f"Hello, {user['username']} ({'Admin' if user.get('is_admin') else 'Student'})")
            if user.get("is_admin"):
                utils.print_menu(["Create Trip", "List Trips", "View Reservations", "Logout"])
                c = input("Choose: ").strip()
                if c == "1":
                    trip_id = input("trip id: ").strip()
                    vehicle_id = input("vehicle id: ").strip()
                    origin = input("origin: ").strip()
                    dest = input("destination: ").strip()
                    date = input("date (YYYY-MM-DD): ").strip()
                    time = input("time (HH:MM): ").strip()
                    fare = input("fare: ").strip()
                    trips = db.read("trips")
                    trips.append(models.make_trip(trip_id, vehicle_id, origin, dest, date, time, fare))
                    db.write("trips", trips)
                    print("Trip created.")
                    input("enter to continue...")
                elif c == "2":
                    trips = db.read("trips")
                    for t in trips:
                        print(utils.format_trip(t))
                    input("enter to continue...")
                elif c == "3":
                    res = db.read("reservations")
                    for r in res:
                        print(r)
                    input("enter to continue...")
                elif c == "4":
                    user = None
                else:
                    print("invalid")
                    input("enter to continue...")
            else:
                utils.print_menu(["Search Trips", "My Reservations", "Cancel Reservation", "Logout"])
                c = input("Choose: ").strip()
                if c == "1":
                    origin = input("origin (or leave blank): ").strip()
                    dest = input("destination (or leave blank): ").strip()
                    date = input("date (YYYY-MM-DD or leave blank): ").strip()
                    trips = search.find_trips(origin or None, dest or None, date or None)
                    if not trips:
                        print("No trips found.")
                    else:
                        for t in trips:
                            print(utils.format_trip(t), "| seats left:", search.seats_available(t["trip_id"]))
                        sel = input("Enter trip id to book / leave blank: ").strip()
                        if sel:
                            seats = input("seats to book: ").strip()
                            try:
                                reservation.create_reservation(user["username"], sel, int(seats))
                                print("Booked.")
                            except Exception as e:
                                print("Error:", e)
                    input("enter to continue...")
                elif c == "2":
                    res = reservation.user_reservations(user["username"])
                    for r in res:
                        print(r)
                    input("enter to continue...")
                elif c == "3":
                    rid = input("reservation id to cancel: ").strip()
                    try:
                        reservation.cancel_reservation(rid, user["username"])
                        print("Canceled.")
                    except Exception as e:
                        print("Error:", e)
                    input("enter to continue...")
                elif c == "4":
                    user = None
                else:
                    print("invalid")
                    input("enter to continue...")

if __name__ == "__main__":
    main()
