# 📱 TaskFlow – Mobile Productivity Tracker App

A full-stack mobile task manager built using **React Native** (frontend), **FastAPI** (backend), and **PostgreSQL** (database).  
Designed for Android/iOS to help users manage tasks with login functionality, tagging, status filters, pagination, and a clean UI.

---

## 🚀 Features

- 🔐 Secure user login with JWT-based authentication
- 🧾 Task creation, update, delete (CRUD)
- 🏷️ Filter tasks by tag and status
- 📄 Paginated task loading for performance
- 🔁 Frontend state managed with React Hooks
- 📡 RESTful API with FastAPI
- 💾 PostgreSQL database for persistent storage

---

## 🛠️ Tech Stack

| Layer        | Tech             |
|--------------|------------------|
| Frontend     | React Native     |
| Backend      | FastAPI          |
| Database     | PostgreSQL       |
| Auth         | JWT + OAuth2     |
| Styling      | React Native Components |
| ORM          | SQLAlchemy       |

---

## 📂 Project Structure
taskflow-mobile-tracker/
├── backend/
│ ├── main.py
│ ├── models.py
│ ├── crud.py
│ ├── auth.py
│ ├── schemas.py
│ ├── database.py
│ ├── requirements.txt
├── frontend/
│ ├── App.js
│ └── screens/
│ ├── LoginScreen.js
│ ├── TaskList.js
│ └── CreateTask.js
├── README.md


---

## 🔧 Setup Instructions

### 📌 Backend Setup (FastAPI + PostgreSQL)

1. Navigate to backend folder:
    ```bash
    cd backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Update `database.py` with your PostgreSQL connection string:
    ```python
    SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/taskflow_db"
    ```

5. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

### 📱 Frontend Setup (React Native)

1. Navigate to frontend folder:
    ```bash
    cd frontend
    ```

2. Install packages:
    ```bash
    npm install
    ```

3. Start Expo or React Native:
    ```bash
    npm start
    ```

> Make sure to replace the API base URL in frontend with your local IP and FastAPI port (default: 8000).

---

## ✅ API Endpoints (Backend Preview)

| Method | Endpoint         | Description             |
|--------|------------------|-------------------------|
| POST   | /register        | Register new user       |
| POST   | /login           | Authenticate and get token |
| GET    | /tasks/          | Get list of tasks       |
| POST   | /tasks/          | Create new task         |
| PUT    | /tasks/{id}      | Update task             |
| DELETE | /tasks/{id}      | Delete task             |

---

## 📌 Environment Notes

- React Native uses Expo for development and can run on Android/iOS simulators or physical devices.
- FastAPI auto-generates Swagger docs at: [http://localhost:8000/docs](http://localhost:8000/docs)
- Make sure PostgreSQL is installed and running locally or use a hosted DB like Supabase or ElephantSQL.

---

**TaskFlow Project** 

---

## 📄 License

MIT License. Free to use and modify.
