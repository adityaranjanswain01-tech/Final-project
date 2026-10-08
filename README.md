# Shop_Shpere

A full-stack web application developed using **Python and Django**. The project provides a structured web interface with backend functionality, database integration, user interaction, and dynamic content management.

## 🚀 Features

* User-friendly web interface
* Django-based backend
* Database integration
* User authentication
* CRUD operations
* Dynamic web pages
* Form handling and validation
* Static files management
* Responsive frontend design

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **SQLite**
* 
## 📂 Project Structure

```text
Final-Project/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   └── ...
│
└── project_app/
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── ...
```

> The exact folder structure may vary depending on the Django apps included in the project.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/adityaranjanswain01-tech/Final-project.git
```

### 2. Navigate to the project

```bash
cd Final-project
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the virtual environment

**Windows:**

```bash
myenv\Scripts\activate
```

**Linux/macOS:**

```bash
source myenv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 🔐 Admin Panel

Django provides an admin panel for managing application data.

After creating a superuser, visit:

```text
http://127.0.0.1:8000/admin/
```

Log in using your superuser credentials.

## 📦 Dependencies

All required Python packages are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

## 🗄️ Database

This project uses **SQLite** during development.

Database migrations can be applied with:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 🔒 Important

The following files and folders should not be uploaded to GitHub:

```text
myenv/
__pycache__/
db.sqlite3
.env
.vscode/
```

These are excluded using `.gitignore`.

## 👨‍💻 Author

**Jyotiraditya Ranjan Swain**

GitHub: [@adityaranjanswain01-tech](https://github.com/adityaranjanswain01-tech)

This project is created for educational and project-development purposes.
