## Movie Management System

A simple full-stack movie management system built with **Django** (backend) and **Vue.js** (frontend). You can **create**, **edit**, **delete**, **view**, and **play movies** (including video file upload).

---

## Project Structure

```
movie-management-application/
├── backend-django/         # Django backend
├── frontend-vue/        # Vue 2 frontend
└── README.md
```

---

## Requirements

### Backend (Python)

* Python 3.8+
* pip

### Frontend (Node.js)

* Node.js 16+
* npm

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/23twoothreee/movie-management-system.git
cd movie-management-system
```

---

## Backend Setup (Django)

### Navigate to `backend-django/`:

```bash
cd backend-django
```

### 1. Set up Django project

```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Run the development server

```bash
python manage.py runserver
```

---

## Frontend Setup (Vue 2)

### Navigate to `frontend-vue/`:

```bash
cd frontend-vue
```

### 1. Install dependencies

```bash
npm install
```

### 2. Run the development server

```bash
npm run dev
```

---

## Features

* Movie list with poster
* Upload video files
* View movie details with video player
* Edit & delete movies