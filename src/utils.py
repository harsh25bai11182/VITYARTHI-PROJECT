#utilities for cli

def format_trip(t):
    return f"{t['trip_id']}: {t['origin']} -> {t['destination']} on {t['date']} at {t['time']} | fare: {t['fare']} | vehicle: {t['vehicle_id']}"

def print_menu(options):
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    print("0. Exit")
