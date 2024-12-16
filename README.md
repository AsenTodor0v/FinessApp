## deploy: https://fitnessapp-gmfcesbhhmgdg8gh.italynorth-01.azurewebsites.net/
# Fitness Meal Plan App

A web application where certified nutritionists and fitness coaches can upload, manage, and share meal plans. The app includes public and private sections, user authentication, and an admin panel for managing content.

---

## Features

- **Authentication**: Login, register, and logout functionality.
- **Public Pages**: View available meal plans and search for specific plans.
- **Private Pages**: Create, update, and manage your meal plans (authenticated users only).
- **Admin Panel**: Customized admin interface for managing meal plans, comments, users, and roles.
- **Responsive Design**: Built with Bootstrap for a mobile-friendly experience.
- **Secure**: Protects against SQL injection, CSRF, and XSS vulnerabilities.
- **Custom Roles**: Different permissions for staff and superusers.

---

## Technologies Used

- **Backend**: [Django](https://www.djangoproject.com/) (Python Framework)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: PostgreSQL (or any database of your choice)
- **Environment Management**: `.env` for storing sensitive data securely

---

## Setup Instructions

### Prerequisites

1. Python 3.8+
2. Virtual Environment (optional but recommended)
3. PostgreSQL (or your preferred database)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AsenTodor0v/FitnessApp
   cd FitnessApp
2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**
   ```bash
    pip install -r requirements.txt
4. **Set Up the Environment Variables**
   Rename .env.template to .env:
   ```bash
   mv .env.template .env
  - Edit the .env file and update it with your environment-specific settings (e.g., database 
  credentials).
  - Example:
   ```bash
   DEBUG=True
   SECRET_KEY=your_secret_key_here
   ```
5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
7. Run the Development Server
   ```bash
   python manage.py runserver
8. Access the App
  - Visit http://127.0.0.1:8000 in your browser.
