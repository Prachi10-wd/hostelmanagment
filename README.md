# 🏨 Hostel Management System

A simple Python-based Hostel Management System that models the relationship between students, rooms, and hostels using Object-Oriented Programming (OOP) principles.

---

## 📋 Overview

This project simulates a basic hostel allocation workflow where students can request rooms, and the hostel system checks availability and allocates rooms accordingly. It demonstrates core OOP concepts such as classes, objects, encapsulation, and inter-object communication.

---

## 🗂️ Project Structure

```
hostel-management-system/
│
├── hostel_management.py   # Main source file containing all classes and logic
└── README.md              # Project documentation
```

---

## 🧩 Classes

### `Student`
Represents a student in the system.

| Attribute   | Description              |
|-------------|--------------------------|
| `stud_id`   | Unique ID of the student |
| `course`    | Course enrolled in       |

**Methods:**
- `display()` — Prints student details.
- `demands_room(hostel, room)` — Sends a room request to a hostel.

---

### `Room`
Represents a hostel room.

| Attribute        | Description                          |
|------------------|--------------------------------------|
| `room_no`        | Room number                          |
| `rooms`          | Boolean flag (default `True`)        |
| `room_available` | Availability status after evaluation |

**Methods:**
- `display()` — Prints the room number.
- `details()` — Evaluates and sets room availability based on the `rooms` flag.

---

### `Hostel`
Represents a hostel building.

| Attribute      | Description                    |
|----------------|--------------------------------|
| `hostel_name`  | Name of the hostel             |
| `total_rooms`  | Total number of rooms          |

**Methods:**
- `display()` — Prints hostel details.
- `checks_availability(room)` — Checks if a room is available and allocates it if so.
- `allocate_room(room)` — Allocates the room to the requesting student.

---

## ▶️ How to Run

### Prerequisites
- Python 3.x installed on your machine.

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/hostel-management-system.git
   cd hostel-management-system
   ```

2. **Run the script**
   ```bash
   python hostel_management.py
   ```

---

## 💡 Sample Output

```
Details of student are:
 Student ID: S12
 Course: Bca.
Details of student are:
 Student ID: S22
 Course: Btech.
The room no. is: 213.
The room no. is: 214.
Hostel Details are:
 Name of Hostel: Prayag
 Total rooms: 220.
Hostel Details are:
 Name of Hostel: Marco
 Total rooms: 240.
Room is available!
213 is yours.
```

---

## 🔄 Workflow

```
Student.demands_room()
        │
        ▼
Hostel.checks_availability()
        │
        ▼
Room.details()  ──► Sets room_available = True/False
        │
        ▼
  Available?
   ├── YES ──► Hostel.allocate_room() ──► "Room X is yours."
   └── NO  ──► "Room is not available!"
```

---

## 🚀 Future Enhancements

- [ ] Add room deallocation functionality
- [ ] Track which student is assigned to which room
- [ ] Persist data using file I/O or a database
- [ ] Add a command-line or GUI interface
- [ ] Implement room types (single, double, dormitory)
- [ ] Add fee/billing management

---

## 🛠️ Built With

- **Python 3** — Core programming language
- **OOP Principles** — Classes, encapsulation, and object interaction

---

## 🙋‍♂️ Author

Made with ❤️ as a Python OOP learning project.  
Feel free to fork, improve, and contribute!
