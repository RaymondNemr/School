# School API

A simple REST API for managing students and their grades, built with **Python, Flask, SQLAlchemy, and PostgreSQL**, fully containerized with **Docker**.

This project demonstrates a basic backend architecture with:

* REST API
* ORM database access
* PostgreSQL database
* Dockerized services
* Unit tests

## Architecture

The system is composed of two services:

* **App Service**

  * Python
  * Flask
  * SQLAlchemy ORM
* **Database Service**

  * PostgreSQL

Both services run using **Docker Compose**.

```
Client
  |
  v
Flask API
  |
  v
SQLAlchemy ORM
  |
  v
PostgreSQL Database
```

## Features

The API allows you to:

* Create students
* Add grades for students
* Update grades
* Retrieve student information
* Retrieve student grades

### Student Endpoints

#### Get student by ID

```
GET /get-student-by-id?id=<student_id>
```

Example response:

```json
{
  "name": "John",
  "age": 20
}
```

#### Get student by name

```
GET /get-student-by-name?name=<student_name>
```

Example response:

```json
{
  "students": [
    {
      "name": "John",
      "age": 20
    }
  ]
}
```

#### Create student

```
POST /set-student
```

Body:

```json
{
  "name": "John",
  "age": 20
}
```

Response:

```json
{
  "id": 1
}
```

---

### Grade Endpoints

#### Add grade to student

```
POST /set-student-grade
```

Body:

```json
{
  "student_id": 1,
  "subject": "math",
  "grade": 9.5
}
```

Response:

```json
{
  "id": 3
}
```

#### Update grade

```
POST /set-grade
```

Body:

```json
{
  "grade_id": 3,
  "new_grade": 8.5
}
```

---

#### Get grades of a student

```
GET /get-student-grades?id=<student_id>
```

Example response:

```json
{
  "grades": [
    {
      "subject": "math",
      "grade": 9.5
    }
  ]
}
```

#### Get grade by ID

```
GET /get-grade?id=<grade_id>
```

Example response:

```json
{
  "subject": "math",
  "grade": 9.5
}
```

---

# Project Structure

```
School/
│
├── app/
│   ├── school_api.py        # Flask API
│   ├── School_methods.py    # Business logic
│   ├── Student_and_Grade.py # ORM models
│   ├── requirements.txt
│   └── Dockerfile
│
├── database/
│   └── Dockerfile
│
├── docker-compose.yml
│
└── test_School.py           # Unit tests
```

---

# Running the Project

## Requirements

* Docker
* Docker Compose

## Start the system

Clone the repository:

```
git clone <repo-url>
cd School
```

Run the services:

```
docker-compose up --build
```

The API will start at:

```
http://localhost:5000
```

---

# Running Tests

Run the unit tests with:

```
python test_School.py
```

---

# Technologies Used

* Python
* Flask
* SQLAlchemy
* PostgreSQL
* Docker
* Docker Compose
* unittest

---

# Purpose

This project was created as a **learning project to practice backend development concepts**, including API design, database interaction, containerization, and automated testing.
