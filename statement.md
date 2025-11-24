# Project Title – College Transport Reservation System



## 

#### Problem Statement

College students frequently need reliable and affordable transport options for inter-city and inter-state travel during weekends, semester breaks, festivals, and emergencies. Existing public transport systems are either overcrowded, poorly scheduled for student needs, or lack digital booking convenience.  
There is a need for a dedicated, simple, and student‑friendly reservation system that allows safe and organized booking of long‑distance buses and trains directly from the college campus.

#### 

#### Scope of the Project

This project focuses on designing and implementing a text‑based Bus/Train Reservation System tailored specifically for college students.  
The system will include:

* Student registration \& login
* Admin management of trips
* Search and filtering of intercity \& interstate routes
* Seat availability tracking
* Reservation \& cancellation
* Storage of all data using JSON files
* A fully menu-driven CLI interface

The scope is limited to a command-line application built using Python Essentials (Modules 1–13) without external libraries or databases.

## 

#### Target Users

* College Students  
  Students traveling home on weekends, semester breaks, holidays, or returning back to campus.
* College Transport/Admin Department  
  Staff responsible for scheduling buses/trains, managing long-distance student routes, and monitoring bookings.
* Hostel Wardens / Campus Security (Indirect Users)  
  They can view transport logs and student travel patterns (future extension).

## 

#### High-Level Features

* Student registration \& login functionality
* Admin login with route and schedule management
* Search trips by origin, destination, date, and type (bus/train)
* Realistic long-distance routes across states
* Seat availability calculation based on vehicle capacity
* Seat booking with validation
* Reservation cancellation
* Viewing all bookings (admin)
* JSON-based data persistence
* Modular design: auth, db, reservation, models, search, utils
