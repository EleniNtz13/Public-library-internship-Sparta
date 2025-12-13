# 🌟 Week 3 – Overview: Library Management System  

This project is a Django-based web application developed during an internship, aiming to manage a library database.  
It supports importing book records from Excel files, storing them in a PostgreSQL database, and displaying/managing them through a web interface.

## 🧭 Project Overview

The application follows Django’s **MVT (Model–View–Template)** architecture and consists of:

- A PostgreSQL database for persistent storage
- A Django backend for data handling
- A web interface for viewing and adding books
- A custom Django management command for importing Excel data

---

## 🔧 Step-by-Step Implementation Guide

### 1️⃣ Environment Preparation ⚙️

Before starting development, a Python virtual environment is created and activated.  
All required dependencies (Django, PostgreSQL driver, Pandas, OpenPyXL) are installed inside this environment.

📁 *Refer to*: `requirements.txt` (if provided) or virtual environment setup instructions.

---

### 2️⃣ Django Project & Application Setup 🏗

A Django project (`myproject`) and a Django application (`main`) are created.  
The application is registered in the Django settings so that models, templates, and commands are recognized.

📁 *Refer to*:  
- `myproject/settings.py` → `INSTALLED_APPS`

---

### 3️⃣ Database Configuration (PostgreSQL) 🐘

The default SQLite database is replaced with PostgreSQL.  
Connection details such as database name, user, password, host, and port are defined.

This ensures:
- Better performance
- Production-level database support
- Compatibility with bulk inserts

📁 *Refer to*:  
- `myproject/settings.py` → `DATABASES`

---

### 4️⃣ Data Model Design 📦

A `Book` model is designed to represent a library record.  
Each field corresponds **directly** to a column in the Excel file (entry number, author, title, ISBN, etc.).

Special care is taken to:
- Allow nullable fields (`null=True`, `blank=True`)
- Support real-world incomplete data
- Ensure compatibility with imported Excel values

📁 *Refer to*:  
- `main/models.py`

---

### 5️⃣ Database Migration 🔄

After defining the data model, Django migrations are created and applied.  
This step generates the actual database table inside PostgreSQL.

This guarantees:
- Schema consistency
- Version-controlled database changes

📁 *Commands executed from project root*:
- `makemigrations`
- `migrate`

---

### 6️⃣ Excel Data Placement 📊

The Excel file containing book records is placed inside a dedicated folder within the app.  
This keeps data files separated from source code and ensures predictable paths.

📁 Location:
main/excel_data/data.xlsx



The column headers of the Excel file **must exactly match** the model field names.

---

### 7️⃣ Custom Excel Import Command ⚙️📥

A custom Django management command is implemented to import Excel data into PostgreSQL.

Key features:
- Uses Pandas to read Excel files
- Safely converts dates and numeric fields
- Handles empty (NaN) values
- Uses `bulk_create` for performance

This approach is scalable and suitable for large datasets.

📁 *Refer to*:  
- `main/management/commands/import_books.py`

📌 *Execution command*:
python manage.py import_books





---

### 8️⃣ Form Creation for Manual Data Entry 📝

A Django `ModelForm` is created to allow manual insertion of new books via the web interface.

Benefits:
- Automatic validation
- Minimal code duplication
- Direct connection to the data model

📁 *Refer to*:  
- `main/forms.py`

---

### 9️⃣ Views for Data Display & Submission 👁

Two main views are implemented:

- **Book List View**: Retrieves and displays all books from the database
- **Add Book View**: Handles form display and submission

These views act as the logical bridge between the database and the templates.

📁 *Refer to*:  
- `main/views.py`

---

### 🔟 URL Routing 🌐

URL routing connects browser requests to the appropriate views.

- Root URL (`/`) → displays the book list
- `/add/` → displays the book entry form

📁 *Refer to*:  
- `main/urls.py`
- `myproject/urls.py`

---

### 1️⃣1️⃣ Templates & Presentation 🎨

HTML templates are used to render data dynamically.

- `book_list.html`: Displays all books in a table
- `add_book.html`: Displays the form for adding new records

Templates are stored inside the app to leverage Django’s template discovery system.

📁 *Refer to*:  
- `main/templates/`

---

### 1️⃣2️⃣ Application Execution ▶️

The Django development server is started, and the application is accessed through the browser.

Available endpoints:
- `http://localhost:8000/` → Book list
- `http://localhost:8000/add/` → Add new book

📁 *Refer to*:  
- `manage.py`

---

## ✅ Final Outcome 🎉

At the end of this process, the system supports:

- ✔ Structured data storage in PostgreSQL
- ✔ Bulk import of Excel records
- ✔ Dynamic display of library data
- ✔ Manual data entry via forms
- ✔ Clean separation of logic, data, and presentation

---

## 🛠 Technologies Used

- 🐍 Python  
- 🌐 Django  
- 🐘 PostgreSQL  
- 📊 Pandas & OpenPyXL  
- 🧾 HTML / CSS  

---

## 📌 Notes

This project demonstrates backend development skills, database integration, data processing, and adherence to Django best practices.  
It was developed as part of an internship program and is suitable for academic and professional evaluation.



