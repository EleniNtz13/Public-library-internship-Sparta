# 🌟 Week 3 – Library Management System
This week focuses on completing the **full integration between Django forms, views, and the PostgreSQL database**. The system now supports **data persistence**, **Excel imports**, and **web-based data management**.

## 🧭 Overview
During Week 3, the application transitions from initial setup to a **fully functional backend system** by:

- 📐 Defining database models
- 💾 Persisting data in PostgreSQL
- 📊 Importing Excel data into the database
- 📝 Connecting Django forms to models
- 🌐 Displaying stored data using views and templates

## ✨ Features
- 📚 Book model integration with PostgreSQL
- 📝 Manual book entry using Django forms
- 📊 Excel (.xlsx) upload and import
- 🛠️ Database verification via Django Shell & pgAdmin
- 📦 Pandas & OpenPyXL support

---

## 1️⃣ Verify Database Table
###  Option A: Django Shell
```
python manage.py shell
```
```
from excel_data.models import Book
Book.objects.all()
```

✅ If no error occurs, the model and table exist.

Inspect fields:
```
for field in Book._meta.fields:
    print(field.name, field.get_internal_type())
```

###  Option B: pgAdmin 4
1. Open **pgAdmin 4**

2. Navigate:
```
Databases → your_db → Schemas → public → Tables
```
3. Confirm table ```excel_data_book``` exists

4. Verify fields: ```entry_number```, ```entry_date```, ```koha_author```, ```publish_year```

⚠️ Fix:
```
publish_year = models.CharField(max_length=20, null=True, blank=True)
```

Must be ```CharField```, not integer.

Run migrations if missing:
```
python manage.py makemigrations
python manage.py migrate
```

## 2️⃣ Create ```forms.py```
File: ```excel_data/forms.py``` 

Defines Django form for manual book entry.

## 3️⃣ Create ```views.py```
File: ```excel_data/views.py``` 
Handles:

- Displaying book form
- Saving data to PostgreSQL
- Rendering success templates
- Uploading Excel files


## 4️⃣ Create ```urls.py```
File: ```excel_data/urls.py``` 
⚠️ Ensure included in project-level ```urls.py``` using ```include()```.


5️⃣ Templates 🧩
Directory:
```
templates/
└── excel_data/
    ├── book_list.html
    ├── add_book.html
    ├── upload_excel.html
    ├── success.html
    ├── upload_result.html
    └── login.html
```


- 📄 ```add_book.html``` → Add book form (CSRF protected)
- 📄 ```book_list.html``` → Display stored books
- 📄 ```upload_excel.html``` → Excel upload form
- 📄 ```success.html``` → Success message
- 📄 ```upload_result.html``` → Upload results
- 📄 ```login.html``` → User login page


## 6️⃣ Manual Entry Test ✅
1. Run server:
```
python manage.py runserver
```

2. Open:
```
http://127.0.0.1:8000/books/add/
```
3. Verify form loads and saves data.

## 7️⃣ Install Libraries 📦
```
pip install pandas openpyxl
```

## 8️⃣ Configure Authentication 🔐
In ```settings.py```:
```
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/upload-excel/'
LOGOUT_REDIRECT_URL = '/login/'
```

⚠️ Note: After login, the user is redirected directly to the Excel upload page (```/upload-excel/```).

Ensure ```INSTALLED_APPS``` and ```MIDDLEWARE``` include required Django defaults.

## 9️⃣ Authentication Views
In ```urls.py```:
```
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```
Create ```templates/main/login.html```. 
Create superuser:
```
python manage.py createsuperuser
```

## 🔟 Excel Upload Logic 📊
Update ```views.py```:

- Add upload_excel view
- Read .xlsx files with Pandas
- Map rows to Book model

⚠️ Restrict file type:
```
if not file.name.endswith('.xlsx'):
    messages.error(request, 'Only .xlsx files are allowed')
```

## 1️⃣1️⃣ Excel Upload URL 🔗
In ```excel_data/urls.py```:
```
path('upload-excel/', views.upload_excel, name='upload_excel'),
```

## 1️⃣2️⃣ Final Test – Excel Upload 🚀
Run server:
```
python manage.py runserver
```
Open:
```
http://127.0.0.1:8000/login/
```
➡️ After login, user is redirected to:
```
http://127.0.0.1:8000/upload-excel/
```
Verify:

- Login works
- Upload form loads
- ```.xlsx``` accepted
- Records imported into PostgreSQL

---

## ✅ Key Notes
- 📌 Only ```.xlsx``` files supported
- 📌 Templates contain HTML only
- 📌 Run migrations after any model change
- 📌 Confirm app URLs are registered at project level
- 📌 Login redirects directly to Excel upload page

## 🎯 Result
You now have a complete Django backend that supports:
- 📝 Manual book entry via forms
- 📊 Excel-based bulk data import
- 💾 PostgreSQL-backed data persistence
- 🔐 Secure login flow → redirect to Excel upload

🚀 Happy coding!


