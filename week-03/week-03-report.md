# 🌟 Week 3 – Library Management System

This week focuses on completing the **full integration between forms, views, and the PostgreSQL database**.  
The system now supports **data persistence**, **Excel imports**, and **web-based data management**.
This repository provides a complete guide for managing book records in a Django application, including manual form entry and Excel (`.xlsx`) upload functionality.


## 🧭 Overview

During Week 3, the application transitions from setup to a **fully functional backend system** by:

- Defining database models
- Importing Excel data into PostgreSQL
- Connecting forms to models
- Displaying stored data via Django views and templates


---

## ✨ Features

* 📚 Book model integration with PostgreSQL
* 📝 Manual book entry using Django forms
* 📊 Excel (`.xlsx`) upload and import
* 🛠️ Admin & pgAdmin verification steps
* 📦 Pandas & OpenPyXL support

---

## 1️⃣ Verify That the `Book` Table Exists

Before proceeding, ensure that the `Book` table exists in the database.

### 🔹 Option A: Check Using Django Shell (Recommended)

```bash
python manage.py shell
```

```python
from excel_data.models import Book

Book.objects.all()
```

✅ If no error occurs, the table exists.

To inspect fields:

```python
for field in Book._meta.fields:
    print(field.name, field.get_internal_type())
```

---

### 🔹 Option B: Check Using pgAdmin 4

1. Open **pgAdmin 4**
2. Navigate to:

   ```
   Databases → your_database → Schemas → public → Tables
   ```
3. Confirm a table named **`book`** exists
4. Verify fields such as:

   * `entry_number`
   * `entry_date`
   * `koha_author`
   * `publish_year`

⚠️ **Important Fix**

```python
publish_year = models.CharField(max_length=20, null=True, blank=True)
```

`publish_year` **must be a `CharField`**, not an integer.

If the table does not exist, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 2️⃣ Create `excel_data/forms.py`

Create the file:

```
excel_data/forms.py
```

Add the exact code provided in the corresponding project file.

---

## 3️⃣ Create `excel_data/views.py`

Create:

```
excel_data/views.py
```

Add the view logic provided in the project files.

---

## 4️⃣ Create `excel_data/urls.py`

Create:

```
excel_data/urls.py
```

```python
from django.urls import path
from . import views

urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
]
```

---

## 5️⃣ Create Templates 🧩

Directory structure:

```
templates/
└── excel_data/
    ├── add_book.html
    └── success.html
```

### 📄 add_book.html

* HTML only
* ⚠️ Do **NOT** include Python code such as:

```python
return redirect('show_books')
```

### 📄 success.html

* Displays a success message after submission

---

## 6️⃣ Initial Test – Manual Entry ✅

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/books/add/
```

Verify that books are saved successfully.

---

## 7️⃣ Install Required Libraries 📦

```bash
pip install pandas openpyxl
```

---

## 8️⃣ Add Excel Upload Logic 📊

Update `views.py` with:

* `upload_excel` view
* `.xlsx` file reading
* Row-to-model mapping

⚠️ Only `.xlsx` files are allowed.

```python
if not file.name.endswith('.xlsx'):
    messages.error(request, 'Only .xlsx files are allowed')
```

---

## 9️⃣ Add Excel Upload URL 🔗

Update `excel_data/urls.py`:

```python
path('upload-excel/', views.upload_excel, name='upload_excel'),
```

---

## 🔟 Final Test – Excel Upload 🚀

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/upload-excel/
```

Verify:

* File upload works
* Data is imported correctly

---

## ✅ Key Notes

* 📌 Only `.xlsx` files are supported
* 📌 Templates contain HTML only
* 📌 Always run migrations after model changes
* 📌 Confirm URLs are registered

---

## 🎯 Result

You now have a complete Django setup for:

* Manual book entry
* Excel-based bulk import
* PostgreSQL-backed persistence

Happy coding 🚀





















## 1️⃣🔧 Step-by-Step Implementation Guide

### 1. ⚙️ Environment Preparation 

All required Python libraries are installed inside the virtual environment.

Used libraries(```pip install...```):
- Django 
- psycopg2-binary
- Pandas
- OpenPyXL

📁 Code reference:
- `requirements.txt` (optional)

⚠️ **Warning**  
The virtual environment must be activated before installing or running any Django command.


### 2. 🏗 Django Project & App Registration 

The Django project (`myproject`) and a Django application (`main`) are created, verified and registered.

Purpose:
- Enable Django to detect models, templates, and management commands

📁 Code reference:
- `myproject/settings.py` → `INSTALLED_APPS`
- App folder: `main/`

⚠️ **Warning**  
If the app is missing from `INSTALLED_APPS`, models and forms will not work.

---

### 3. 🐘 Database Configuration (PostgreSQL)

Django is configured to use PostgreSQL instead of SQLite.
Connection details such as database name, user, password, host, and port are defined.

Purpose:
- Production-level database support
- Compatibility with bulk data import

📁 Code reference:
- `myproject/settings.py` → `DATABASES`

⚠️ **Warning**  
The database name, user, and password must match exactly the PostgreSQL configuration in pgAdmin.

---

### 4. 📦 Data Model Design

The `Book` model defines the structure of library records.
Each field corresponds **directly** to a column in the Excel file (entry number, author, title, ISBN, etc.).

Purpose:
- Map database fields to real library data
- Match Excel column names

📁 Code reference:
- `main/models.py`

⚠️ **Warning**  
Any modification to the model requires new migrations.


Special care is taken to:
- Allow nullable fields (`null=True`, `blank=True`)
- Support real-world incomplete data
- Ensure compatibility with imported Excel values

---

### 5. 🔄 Database Migration 

After defining the data model, Django migrations are created and applied. Migrations synchronize Django models with PostgreSQL tables. This step generates the actual database table inside PostgreSQL.

Purpose:
- Create database tables
- Ensure schema consistency

📁 Code reference:
- `manage.py`

📁 *Commands executed from project root*:
- `makemigrations`
- `migrate`

⚠️ **Warning**  
Commands must be executed from the directory containing `manage.py`.

---

### 6. 📊 Excel Data Placement 

The Excel file containing book records is placed inside a dedicated folder within the app.  
This keeps data files separated from source code and ensures predictable paths.

📁 Location:
`main/excel_data/data.xlsx`

The column headers of the Excel file **must exactly match** the model field names.

---

### 7. ⚙️📥 Custom Excel Import Command 

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

### 8. 📝 Form Creation for Manual Data Entry 

A Django `ModelForm` is created to allow manual insertion of new books via the web interface.

Benefits:
- Automatic validation
- Minimal code duplication
- Direct connection to the data model

📁 *Refer to*:  
- `main/forms.py`

---

### 9. 👁 Views for Data Display & Submission 

Two main views are implemented:

- **Book List View**: Retrieves and displays all books from the database
- **Add Book View**: Handles form display and submission

These views act as the logical bridge between the database and the templates.

📁 *Refer to*:  
- `main/views.py`

---

### 10. 🌐 URL Routing 

URL routing connects browser requests to the appropriate views.

- Root URL (`/`) → displays the book list
- `/add/` → displays the book entry form

📁 *Refer to*:  
- `main/urls.py`
- `myproject/urls.py`

---

### 11. 🎨 Templates & Presentation 

HTML templates are used to render data dynamically.

- `book_list.html`: Displays all books in a table
- `add_book.html`: Displays the form for adding new records

Templates are stored inside the app to leverage Django’s template discovery system.

📁 *Refer to*:  
- `main/templates/`

---

### 12. ▶️ Application Execution 

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






2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟

χρειάζεται να είναι ενεργοποιημένο το περιβάλλον σε όλη την διαδικασία;

---

να δω τις φωτο



import_books.xlsx



python manage.py shell





from main.models import Book
from openpyxl import load_workbook

# Άνοιγμα του σωστού αρχείου
wb = load_workbook("import_books.xlsx")
ws = wb.active

headers = [cell.value for cell in ws[1]]

inserted = 0

for row in ws.iter_rows(min_row=2, values_only=True):
    data = dict(zip(headers, row))

    Book.objects.create(
        entry_number=data.get("entry_number"),
        entry_date=data.get("entry_date"),
        author=data.get("author"),
        koha_author=data.get("koha_author"),
        title=data.get("title"),
        publisher=data.get("publisher"),
        edition=data.get("edition"),
        publish_year=data.get("publish_year"),
        publish_place=data.get("publish_place"),
        shape=data.get("shape"),
        pages=data.get("pages"),
        volume=data.get("volume"),
        notes=data.get("notes"),
        isbn=data.get("isbn"),
        column1=data.get("column1"),
        column2=data.get("column2"),









import os
import django
import csv
from datetime import datetime

# === 1. Ρύθμιση Django environment ===
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from main.models import Book

# === 2. Path του CSV ===
csv_path = "import_books.csv"  # το CSV πρέπει να βρίσκεται δίπλα στο manage.py

# === 3. Μετρητής εισαγωγής ===
inserted = 0

# === 4. Άνοιγμα CSV και loop σε κάθε γραμμή ===
with open(csv_path, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=2):
        print(f"Row {i}:", row)
        try:
            # Μετατροπή τύπων
            entry_number = int(row["entry_number"]) if row.get("entry_number") else None
            publish_year = int(row["publish_year"]) if row.get("publish_year") else None
            entry_date = datetime.strptime(row["entry_date"], "%Y-%m-%d").date() if row.get("entry_date") else None

            Book.objects.create(
                entry_number=entry_number,
                entry_date=entry_date,
                author=row.get("author"),
                koha_author=row.get("koha_author"),
                title=row.get("title"),
                publisher=row.get("publisher"),
                edition=row.get("edition"),
                publish_year=publish_year,
                publish_place=row.get("publish_place"),
                shape=row.get("shape"),
                pages=row.get("pages"),
                volume=row.get("volume"),
                notes=row.get("notes"),
                isbn=row.get("isbn"),
                column1=row.get("column1"),
                column2=row.get("column2"),
            )
            inserted += 1
        except Exception as e:
            print(f"Row {i} ERROR:", e)

print("Συνολικές εγγραφές που μπήκαν:", inserted)







 εμμφανιστικε στο cmd τα δατα me ta parapanw


C:\Users\spart\myproject\main




urls.py

 from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Αυτό πρέπει να υπάρχει για να "βλέπει" τα URLs του app
]


vies.py 
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def show_books(request):
    books = Book.objects.all()
    return render(request, 'main/book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        form = BookForm()
    return render(request, 'main/add_book.html', {'form': form})





add_book.html

<h2>Add a New Book</h2>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>

{% if form.errors %}
<div style="color:red;">
    <ul>
        {% for field in form %}
            {% for error in field.errors %}
                <li>{{ field.label }}: {{ error }}</li>
            {% endfor %}
        {% endfor %}
        {% for error in form.non_field_errors %}
            <li>{{ error }}</li>
        {% endfor %}
    </ul>
</div>
{% endif %}

return redirect('show_books')  # Όπως έχει ήδη σωστά





book_list.html

<!DOCTYPE html>
<html>
<head>
    <title>Library Database</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            padding: 6px;
        }
        th {
            background-color: #ddd;
        }
    </style>
</head>
<body>

<h2>Books in Library</h2>

<table>
    <tr>
        <th>entry_number</th>
        <th>entry_date</th>
        <th>author</th>
        <th>koha_author</th>
        <th>title</th>
        <th>publisher</th>
        <th>edition</th>
        <th>publish_year</th>
        <th>publish_place</th>
        <th>shape</th>
        <th>pages</th>
        <th>volume</th>
        <th>notes</th>
        <th>isbn</th>
        <th>column1</th>
        <th>column2</th>
    </tr>

    {% for book in books %}
    <tr>
        <td>{{ book.entry_number }}</td>
        <td>{{ book.entry_date }}</td>
        <td>{{ book.author }}</td>
        <td>{{ book.koha_author }}</td>
        <td>{{ book.title }}</td>
        <td>{{ book.publisher }}</td>
        <td>{{ book.edition }}</td>
        <td>{{ book.publish_year }}</td>
        <td>{{ book.publish_place }}</td>
        <td>{{ book.shape }}</td>
        <td>{{ book.pages }}</td>
        <td>{{ book.volume }}</td>
        <td>{{ book.notes }}</td>
        <td>{{ book.isbn }}</td>
        <td>{{ book.column1 }}</td>
        <td>{{ book.column2 }}</td>
    </tr>
    {% endfor %}
</table>

</body>
</html>



---

*να μετονομασω τους φακελους που εφτιαξα εδω αλλιώς να τους αντικαταστήσω!*

1) make sure the table Book exists on pgAdmin4 and it has fields like (entry_number, entry_date, koha_author...) poia einai ta vimata? 2 oi tropoi!
2)  δημιουργία excel_data/forms.py me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου
3)  δημιουργία excel_data/views.py me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου
4)  δημιουργία excel_data/urls.py me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου
5)  δημιουργία templates/excel_data kai ekei mesa 4 arxeia me onoma add_book.html  me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου kai success.html  me ton κώδικα που φαινεται στο αντίστοιχο αρχείο του παρόντος φακέλου
6)  test python manage.py runserver kai meta http://127.0.0.1:8000/books/add/
7)  egkatastasi vivliothikis pip install pandas openpyxl
8)  ενημερωση views.py με προσθήκη του κώδικα upload, view pou diavazei excel kai gemizei ti forma 
9)  url gia excel upload -> prosthiki sto  excel_data/urls.py to "path('upload-excel/', views.upload_excel, name='upload_excel'),
10)  test python manage.py runserver kai meta http://127.0.0.1:8000/upload-excel/



prosthiki sto views.py tou:
import pandas as pd
import datetime
from dateutil.parser import parse
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def clean_text(value):
    if pd.isna(value):
        return None
    return str(value).strip()



upload_excel:

def upload_excel(request):
    if request.method == "POST" and request.FILES.get('file'):
        df = pd.read_excel(request.FILES['file'])

        # Καθαρισμός ονομάτων στηλών Excel
        df.columns = df.columns.str.strip().str.lower()

        books = []

        for _, row in df.iterrows():

            # entry_date
            entry_date_value = row.get('entry_date')
            if pd.notnull(entry_date_value):
                if hasattr(entry_date_value, 'to_pydatetime'):
                    entry_date_value = entry_date_value.to_pydatetime().date()
                elif isinstance(entry_date_value, str):
                    entry_date_value = parse(entry_date_value).date()
            else:
                entry_date_value = None

            books.append(Book(
                entry_number=clean_text(row.get('entry_number')),
                entry_date=entry_date_value,
                author=clean_text(row.get('author')),
                koha_author=clean_text(row.get('koha_author')),
                title=clean_text(row.get('title')),
                publisher=clean_text(row.get('publisher')),
                edition=clean_text(row.get('edition')),
                publish_year=clean_text(row.get('publish_year')),
                publish_place=clean_text(row.get('publish_place')),
                shape=clean_text(row.get('shape')),
                pages=clean_text(row.get('pages')),
                volume=clean_text(row.get('volume')),
                notes=clean_text(row.get('notes')),
                isbn=clean_text(row.get('isbn')),
                column1=clean_text(row.get('column1')),
                column2=clean_text(row.get('column2')),
            ))

        Book.objects.bulk_create(books)

        return redirect('show_books')

    return render(request, 'main/upload_excel.html')





Notes: 

- πρεπει ΤΟ ΑΡΧΕΊΟ που θα φορτωθεί στον browser να είναι .xlsx
- sto add_book.html sto telos tou kwdika den prepei na iparxei return redirect('show_books') -> einai python
- na diorthoso to publish year sto models na einai char oxi int! "publish_year = models.CharField(max_length=20, null=True, blank=True)"
<img width="892" height="620" alt="image" src="https://github.com/user-attachments/assets/59eb6eaa-c39a-44a6-aa72-8c03b2d2c92a" />
<img width="982" height="503" alt="image" src="https://github.com/user-attachments/assets/28171cea-4efd-4195-a04d-f738da27ff15" />
<img width="987" height="372" alt="image" src="https://github.com/user-attachments/assets/0f23251d-876c-42d3-9e73-5a95052a8201" />
<img width="1012" height="537" alt="image" src="https://github.com/user-attachments/assets/675979b8-fc25-4d9e-adbd-9962dd12f5b0" />
<img width="1047" height="486" alt="image" src="https://github.com/user-attachments/assets/1a954e04-fc9e-4610-9a21-52b16516e50a" />



