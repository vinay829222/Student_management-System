# Student Management System

A **Student Management System** developed using **Django (Python)**, **Bootstrap**, and an **SQL database**.  
This project allows authenticated users to manage student records efficiently and securely.

---

## 📖 About the Project

The Student Management System is a web application that helps manage student information such as roll number, name, email, address, and phone number.  
It provides a secure login system so that **only authorized users** can add, update, or delete student records.

The project follows Django’s **MVT (Model–View–Template)** architecture and uses Django’s built-in authentication system.

---

## ✨ Features

- User registration and login
- Secure authentication using Django Auth
- Add new student records
- View all students
- Update student details
- Delete student records
- Login-protected pages using `@login_required`
- Responsive user interface using Bootstrap
- SQL database integration with Django ORM

---

## 🔐 Authentication

- Users must log in to access the dashboard
- Only logged-in users can add, update, or delete records
- Unauthorized users are redirected to the login page

---

## 🖼️ Screenshots

### Login Page
![Login Page](std/screenshots/Login.png)

### Add Student Page
![Add Student](std/screenshots/Register.png)

### Home Page (Dashboard)
![Home Page](std/screenshots/Homepage.png)

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQL (MySQL / SQLite)  
- **Authentication:** Django built-in authentication  
- **Version Control:** Git, GitHub  

---

## 📂 Project Structure
```
std_manage/
│── std/ # Application (views, models, urls)
│── std_manage/ # Project settings
├── templates/std/           # HTML templates
│    ├── login_page.html
│    ├── register.html
│    ├── home.html
│    ├── add_std.html│    └── std_update.html
│── screenshots/                 # Screenshots for README
│   ├── login_page.png
│   ├── home_page.png
│   └── add_student.png
│── manage.py
│── requirements.txt
│── README.md
│── .gitignore
```
--- 
## ⚙️ Installation & Setup
**Clone the repository**
   ```bash
   git clone https://github.com/vinay829222/Student_management-System.git
```
## Go to the project directory
```
cd std_manage
```
## Create a virtual environment
```
python -m venv venv
```
## Activate the virtual environment
```
venv\Scripts\activate   # Windows
```

## Install dependencies
```
pip install -r requirements.txt
```

## Apply database migrations
```
python manage.py makemigrations
python manage.py migrate
```

## Run the development server
```
python manage.py runserver
```
## Open your browser and visit:
```
Open on your local server
http://127.0.0.1:8000/
```

## 🚀 Future Improvements

- Search and filter functionality
- Role-based access control
- Student profile view
- REST API integration

## 👤 Author

- Vinay Kumar
- Django & Python Developer

## 📄 License
This project is created for educational purposes.

