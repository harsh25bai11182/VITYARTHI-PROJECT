College Transport Reservation System (CLI)

A simple and efficient Python-based command-line system that helps college students search, book, and manage bus/train travel without visiting the transport office.
Designed specifically for students who frequently travel intercity or interstate from college.

2. Overview of the Project

The College Transport Reservation System is a Python Essentials–based CLI application that solves a real-world student problem:
finding and booking long-distance travel from college in a clean, digital, and organized manner.

The system eliminates the need for physical queues and manual registers and provides:

Reliable seat availability
Quick route search
Instant booking confirmation
Access to past reservations
Simple admin route management

The system operates on role-based menus:
Students → Search,  Create & manage trips, view bookings, Cancel travel

It uses JSON for storage

3. Key Features

The application provides separate capabilities for Students and Admin.

 Student Interface
1. Search Trips

Search by origin, destination, date
Supports partial or blank inputs
Displays fare, vehicle type, remaining seats

2. Book a Trip

Select trip ID
Enter number of seats
Updates seat availability automatically

3. My Reservations

Shows all bookings by the student
Includes reservation ID, trip ID, date, and seats booked

4. Cancel Reservation

Enter reservation ID
On cancel, seats are added back to the trip


4. Technologies / Tools Used
Tool / Technology	
Python 3.x	- Core logic and CLI application
JSON Files	-Simple data storage for trips, users, reservations, vehicles
Command Line Interface -User interaction
Functions, Loops, Arrays, Modules - As per Python Essentials syllabus

5. Steps to Install & Run the Project

Prerequisites
Python 3.x installed

Installation
Clone or download the project folder:https://github.com/harsh25bai11182/VITYARTHI-PROJECT/tree/main

Running the Application

Execute the Python script directly from your terminal: main.py

6. Instructions for Testing

After running the program, try these scenarios:

Scenario 1: Student Registration + Login

Select 1 (Register)

Enter username & password

Then select 2 (Login)

Expected:
 Student gets logged in and shown main menu.

Scenario 2: Search & Book a Trip

Select Search Trips

Enter origin: college station

Enter destination: jaipur jn

Enter date: 2025-12-01

Choose trip ID (e.g., T5)

Enter seats: 2

Expected:
 Booking success
 Seats reduce from the trip

Scenario 3: View Reservations

Select option 2 (My Reservations)

Expected:
Shows reservation ID, trip, seats, created date.

Scenario 4: Cancel Reservation

Select 3 (Cancel Reservation)

Enter reservation ID

Expected:
 Reservation removed
 Seats restored in trip
