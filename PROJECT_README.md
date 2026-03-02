# Django Name Entry App

A modern Django web application with a beautiful UI for entering and saving names to a SQLite3 database using the MVT (Model-View-Template) architecture.

## Features

- ✨ Modern, gradient-based UI design
- 💾 Save names to SQLite3 database
- 📋 View all saved names with timestamps
- ✅ Success/error message notifications
- 📱 Responsive design

## Tech Stack

- **Framework**: Django 4.2.7
- **Database**: SQLite3
- **Architecture**: MVT (Model-View-Template)
- **Frontend**: HTML5, CSS3 (embedded)

## Project Structure

```
demo_02/
├── manage.py
├── requirements.txt
├── nameproject/          # Main project directory
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
└── nameapp/              # Application directory
    ├── __init__.py
    ├── models.py         # Name model (M in MVT)
    ├── views.py          # View logic (V in MVT)
    ├── urls.py           # App URL routing
    ├── admin.py          # Admin configuration
    ├── apps.py
    ├── tests.py
    ├── migrations/
    └── templates/
        └── nameapp/
            └── home.html # Template (T in MVT)
```

## Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (Optional - for admin access)

```bash
python manage.py createsuperuser
```

### 4. Run Development Server

```bash
python manage.py runserver
```

### 5. Access the Application

- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Usage

1. Open your browser and navigate to `http://127.0.0.1:8000/`
2. Enter your name in the input field
3. Click "💾 Save Name" button
4. Your name will be saved to the SQLite3 database
5. View all saved names below the form with timestamps

## MVT Architecture Explained

- **Model** (`nameapp/models.py`): Defines the `Name` model with fields for name and timestamp
- **View** (`nameapp/views.py`): Contains the `home` view that handles form submission and data retrieval
- **Template** (`nameapp/templates/nameapp/home.html`): Renders the UI with form and displays saved names

## Database

The application uses SQLite3 database (`db.sqlite3`) which will be automatically created when you run migrations.

### Name Model Schema

| Field      | Type         | Description                    |
|------------|--------------|--------------------------------|
| id         | AutoField    | Primary key (auto-generated)   |
| name       | CharField    | User's name (max 100 chars)    |
| created_at | DateTimeField| Timestamp (auto-generated)     |

## Admin Panel

Access the Django admin panel to manage names:

1. Create a superuser account (see step 3 above)
2. Navigate to http://127.0.0.1:8000/admin/
3. Login with your superuser credentials
4. Manage names through the admin interface

## Customization

- **Change colors**: Edit the CSS gradient values in `home.html`
- **Modify model**: Update `nameapp/models.py` and run migrations
- **Update UI**: Edit `nameapp/templates/nameapp/home.html`
- **Add features**: Extend views in `nameapp/views.py`

## License

This project is open source and available for educational purposes.
