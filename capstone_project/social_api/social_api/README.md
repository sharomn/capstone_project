# 📱 Social Media API – Capstone Project

## 🔍 Project Overview
This is a backend-only social media API built with Django and Django REST Framework. It allows users to register, manage profiles, create posts, follow other users, and interact through likes and comments. The project is modular, secure, and designed for clean deployment.

## 🚀 Features
- User registration and profile management
- CRUD operations for posts
- Like and comment on posts
- Follow/unfollow users
- Token-based authentication
- Admin panel customization
- Security best practices (HTTPS, HSTS, CSP, etc.)

## 🛠️ Tech Stack
- Python 3.11
- Django
- Django REST Framework
- SQLite (for development)
- Git & GitHub

## 📁 Project Structure


## 📦 Setup Instructions
```bash
# Clone the repository
git clone https://github.com/sharomn/capstone_project.git
cd capstone_project

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the development server
python manage.py runserver

