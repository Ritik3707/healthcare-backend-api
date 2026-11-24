# 🏥 Healthcare Backend API

A RESTful Healthcare Backend API developed using **Python, Django, Django REST Framework, and PostgreSQL**. This application provides secure user authentication and complete CRUD operations for managing patients, doctors, and patient-doctor assignments.

The project uses JWT (JSON Web Token) authentication to secure API endpoints and Django ORM to interact with the PostgreSQL database.

---

## 📌 Table of Contents

- Project Overview
- Features
- Technology Stack
- Project Architecture
- Application Responsibilities
- Application Workflow
- Database Design
- API Documentation
- Authentication
- Installation and Setup
- Environment Configuration
- Running the Application
- API Testing
- Error Handling
- Security
- Future Improvements
- Author

---

## 📖 Project Overview

The Healthcare Backend API is designed to manage healthcare-related information through RESTful APIs.

It allows users to register and authenticate securely, manage patient records, maintain doctor information, and assign doctors to patients.

The application follows a modular Django architecture, where each application handles a specific responsibility.

---

## ✨ Features

### 1. User Authentication
- User registration.
- User login.
- JWT access and refresh token generation.
- Secure authentication for protected endpoints.

### 2. Patient Management
- Create new patient records.
- Retrieve all patients.
- Retrieve individual patient details.
- Update patient information.
- Delete patient records.

### 3. Doctor Management
- Add new doctors.
- Retrieve all doctors.
- Retrieve individual doctor details.
- Update doctor information.
- Delete doctor records.

### 4. Patient-Doctor Mapping
- Assign doctors to patients.
- Retrieve all patient-doctor assignments.
- Retrieve doctors assigned to a specific patient.
- Remove patient-doctor assignments.

### 5. Database Management
- PostgreSQL integration.
- Django ORM for database operations.
- Foreign key relationships between database models.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Django | Backend web framework |
| Django REST Framework | REST API development |
| PostgreSQL | Relational database |
| Django ORM | Database interaction |
| Simple JWT | JWT authentication |
| python-decouple | Environment variable management |
| Postman | API testing |

---

## 🏗️ Project Architecture

The project follows a modular application architecture using Django.

Each application is responsible for a specific functionality.

### Directory Structure

```text
healthcare_backend/
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── patients/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── doctors/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── mappings/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── venv/
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

### Application Responsibilities

| Application | Responsibility |
|---|---|
| accounts | User registration, login, and authentication |
| patients | Patient record management |
| doctors | Doctor information management |
| mappings | Patient-doctor assignment management |
| config | Main Django settings and URL configuration |

---

## 🔄 Application Workflow

The application processes API requests through the following workflow:

1. The client sends a request using Postman or another API client.
2. The user registers or logs in through the authentication API.
3. The server generates JWT tokens after successful authentication.
4. The client sends the access token in the Authorization header.
5. Django REST Framework verifies authentication and permissions.
6. The request reaches the appropriate application view.
7. Serializers validate incoming data and convert model instances into JSON.
8. Django ORM performs database operations.
9. PostgreSQL stores or retrieves the requested information.
10. The API returns a JSON response with an appropriate HTTP status code.

### Request Flow Diagram

```text
       Client / Postman
              |
              v
       API Request
              |
              v
    JWT Authentication
              |
              v
   Django REST Framework
              |
              v
     Application Views
              |
              v
         Serializers
              |
              v
         Django ORM
              |
              v
       PostgreSQL DB
              |
              v
       JSON Response
```

---

## 🗄️ Database Design

The application uses PostgreSQL as its relational database.

### Main Models

**1. User**

Stores user authentication information.

**2. Patient**

Stores patient details such as:

- Name
- Age
- Gender
- Phone
- Address
- Created by
- Created timestamp
- Updated timestamp

**3. Doctor**

Stores doctor information such as:

- Name
- Specialization
- Phone
- Email
- Experience
- Address
- Created timestamp

**4. PatientDoctorMapping**

Connects patients and doctors using foreign key relationships.

It stores:

- Patient ID
- Doctor ID
- Assignment timestamp

### Database Relationships

- One user can create multiple patient records.
- One patient can have multiple doctor assignments.
- One doctor can be assigned to multiple patients.
- PatientDoctorMapping connects the Patient and Doctor models.

The mapping model establishes the relationship between patients and doctors.

---

## 🔗 API Documentation

Base URL:

```text
http://127.0.0.1:8000/api/
```

### 1. Authentication APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Authenticate user and obtain JWT tokens |

### 2. Patient APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/patients/` | Create a patient |
| GET | `/api/patients/` | Retrieve all patients |
| GET | `/api/patients/<id>/` | Retrieve a specific patient |
| PUT | `/api/patients/<id>/` | Update a patient |
| PATCH | `/api/patients/<id>/` | Partially update a patient |
| DELETE | `/api/patients/<id>/` | Delete a patient |

### 3. Doctor APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/doctors/` | Create a doctor |
| GET | `/api/doctors/` | Retrieve all doctors |
| GET | `/api/doctors/<id>/` | Retrieve a specific doctor |
| PUT | `/api/doctors/<id>/` | Update a doctor |
| PATCH | `/api/doctors/<id>/` | Partially update a doctor |
| DELETE | `/api/doctors/<id>/` | Delete a doctor |

### 4. Patient-Doctor Mapping APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/mappings/` | Assign a doctor to a patient |
| GET | `/api/mappings/` | Retrieve all mappings |
| GET | `/api/mappings/<patient_id>/` | Retrieve mappings for a patient |
| DELETE | `/api/mappings/<id>/` | Delete a mapping by its ID |

**Note:** The mapping detail URL handles GET and DELETE requests differently: GET uses the supplied ID as a patient ID, while DELETE uses it as a mapping ID.

---

## 🔐 Authentication

The project uses JWT authentication through `djangorestframework-simplejwt`.

### Authentication Process

1. Register a new user.
2. Login using registered credentials.
3. Receive access and refresh tokens.
4. Use the access token to access protected API endpoints.

### Authorization Header

Include the following header in authenticated requests:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Replace `YOUR_ACCESS_TOKEN` with the actual access token received from the login API.

---

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

Make sure the following tools are installed:

- Python
- PostgreSQL
- Git
- Postman (for API testing)

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Directory

```bash
cd healthcare_backend
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure Environment Variables

Create a `.env` file in the project's root directory and configure the required environment variables.

See the Environment Configuration section below.

### Step 7: Apply Database Migrations

```bash
python manage.py migrate
```

### Step 8: Start the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Environment Configuration

The application uses environment variables to keep sensitive configuration outside the source code.

Create a `.env` file in the root directory.

Example configuration:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=your_postgresql_username
DB_PASSWORD=your_postgresql_password
DB_HOST=localhost
DB_PORT=5432
```

**Important:**

- Replace placeholder values with your local configuration.
- Never upload your actual `.env` file to GitHub.
- Keep database credentials and secret keys private.

---

## 🧪 API Testing

The APIs were tested using Postman.

The following operations were tested:

| Module | Operations |
|---|---|
| Authentication | Register and Login |
| Patients | POST, GET, GET by ID, PATCH/PUT, DELETE |
| Doctors | POST, GET, GET by ID, PATCH/PUT, DELETE |
| Mappings | POST, GET, GET by Patient ID, DELETE |

### Expected HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 OK | Request successful |
| 201 Created | Resource created successfully |
| 204 No Content | Resource deleted successfully |
| 400 Bad Request | Invalid request data |
| 401 Unauthorized | Authentication required or invalid |
| 403 Forbidden | Permission denied |
| 404 Not Found | Requested resource not found |

---

## 🛡️ Error Handling and Validation

The application uses Django REST Framework serializers and API responses to handle incoming requests.

Validation helps prevent invalid data from being stored in the database.

The API handles common situations such as:

- Missing required fields.
- Invalid input values.
- Invalid patient or doctor references.
- Unauthorized requests.
- Requests for non-existing records.

---

## 🔒 Security

Security-related implementation includes:

- JWT-based authentication.
- Protected API endpoints.
- Environment-based configuration.
- Database credentials kept outside source code.
- Django REST Framework authentication and permission handling.

---

## 🚀 Future Improvements

Possible future enhancements include:

- API pagination and filtering.
- Search functionality for patients and doctors.
- Automated unit and integration tests.
- API documentation using Swagger or OpenAPI.
- Docker-based deployment.
- Cloud deployment and production configuration.

---

## 👨‍💻 Author

**Ritik Raushan**

Healthcare Backend API – Backend Developer Internship Assignment.

---

## 📄 License

This project was developed for internship assignment purposes.