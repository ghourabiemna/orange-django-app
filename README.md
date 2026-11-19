# Orange – Network Interface Resource Management

A web application built with **Django** to manage, search, visualize and reserve network interfaces.

## 📌 Project Overview

Orange is a Django-based web application designed to simplify network interface resource management. It allows users to consult interface information, filter network resources and manage interface reservations.

##  Features

- **Network Interface Management:** Display network interface information.
- **Search and Filtering:** Search interfaces by IP address, description, network element name and administrative status.
- **Pagination:** Navigate through interface records with configurable page sizes.
- **Interface Reservations:** Create and view network interface reservations.
- **Admin Panel:** Use Django's administration interface to manage application data.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django 5.2.4 | Backend framework |
| SQLite | Local development database |
| HTML / CSS | Frontend |
| JavaScript | Frontend interactions |
| OpenPyXL | Excel file generation |
| Pandas | Excel data processing |
| WhiteNoise | Static file serving |

## 📂 Project Structure

```text
orange/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── orange/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── interface_resource/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── migrations/
│   ├── templates/
│   └── static/
│
└── mystaticfiles/
```

##  Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/orange-django-app.git
```

### 2. Navigate to the project directory

```bash
cd orange-django-app
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
pip install python-dotenv
```

### 5. Configure environment variables

Create a `.env` file in the same directory as `manage.py`.

Add the following variables:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Generate a new Django secret key for your local environment. Never publish your real `.env` file.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account (optional)

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open your browser:

- Application: http://127.0.0.1:8000/home/
- Dashboard: http://127.0.0.1:8000/home/dashboard/
- Reservations: http://127.0.0.1:8000/home/reservation/
- Administration: http://127.0.0.1:8000/admin/

##  Database Models

The application includes two main models:

### Interface

Stores network interface information, including:

- Interface name
- Description
- Network Element (NE) name
- IPv4 address
- Subnet mask
- MAC address
- Interface rate
- Administrative status
- IPv4 operating status

### Reservation

Stores reserved interface information, including:

- Interface name
- Description
- Network Element (NE) name


##  Security

Sensitive information must never be committed to the public repository.

The following files and directories should remain excluded:

- `.env`
- `db.sqlite3`
- Database backups
- Secret keys and passwords
- Generated production files
- Python cache files

For production deployment:

- Set `DJANGO_DEBUG=False`.
- Configure `ALLOWED_HOSTS`.
- Store secrets in environment variables.
- Use a properly configured production database.

## 👩‍💻 Author

Developed as a Django project for network interface resource management.

## 📄 License

No license has been specified yet.
