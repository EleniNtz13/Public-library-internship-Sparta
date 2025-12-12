## ⚙️ phpMyAdmin Setup


### 1️⃣ phpMyAdmin Installation
#### 📥 Download phpMyAdmin

Go to the official site:
```
https://www.phpmyadmin.net/downloads/
```

Download the **All Languages ZIP** version

#### 📁 Extract Files

Create a folder inside ```htdocs``` named:

```
C:\Apache24\htdocs\phpmyadmin
```

Extract **all ZIP contents** *directly inside it*

⚠️ Make sure no double folder is created (e.g. phpmyadmin/phpmyadmin).

#### ⚙️ Configure phpMyAdmin

Inside the ```phpmyadmin``` folder:

1. Copy ```config.sample.inc.php```
2. Paste → rename to:
```
config.inc.php
```

3. Open it and on **line 16**, add a **random 32-character secret key**:
```
$cfg['blowfish_secret'] = 'your32charactersecretkeyhere';
```
and save.

#### ⚙️ Register phpMyAdmin in Apache

Open:
```
C:\Apache24\conf\httpd.conf
```

Scroll to the end and add:
```
Alias /phpmyadmin "C:/Apache24/htdocs/phpmyadmin"
<Directory "C:/Apache24/htdocs/phpmyadmin">
    AllowOverride All
    Require all granted
</Directory>
```

💾 Save the file.

#### ⚙️ Set Default Directory Index
Still inside:
```
C:\Apache24\conf
```
Open ```httpd.conf``` and add this line at the very end:
```
DirectoryIndex index.php index.html
```
This ensures Apache loads ```index.php``` first when a folder is accessed.
💾 Save the file.

#### ⚙️ Configure PHP Extensions
Navigate to the PHP installation folder:
```
C:\php
```
1. Copy the file ```php.ini-production```
2. Paste and rename the copy to:
```
php.ini
```
3. Open ```php.ini```
4. Press **Ctrl + F** and search for the following extensions:
- extension=mysqli
- extension=pdo_mysql
5. Remove the semicolon ```;``` in front of them so they become:
```
extension=mysqli
extension=pdo_mysql
```
💾 Save the ```php.ini``` file.

#### Restart Apache

Open **Command Prompt as Administrator**:
```
cd C:\Apache24\bin
httpd -k restart
```

#### Access phpMyAdmin

Open:
```
http://localhost/phpmyadmin
```

If configured correctly, the **login page** will appear.
Enter your **MySQL username and password**.

#### 🗄️ Create a Database in phpMyAdmin
➕ Create New Database

1. Left sidebar → **New**
2. Enter a name
3. Choose collation:
```
utf8mb4_general_ci
```
4. Click **Create**

#### 📤 Import Data (CSV)

If you have Excel data:

1. Convert Excel file to **.csv**

2. Open phpMyAdmin → select your database

3. Go to **Import**

4. Upload your CSV file

#### 💡 Tip: CSV Import Notes

When importing your .csv file into phpMyAdmin:

- Make sure that the **column names in the CSV match exactly** the fields in your database table (same order, same spelling, no extra spaces).
- If the data does not appear correctly aligned after import, change the **Field Separator** from ```,``` to ```;```.
- Ensure the file is saved in **UTF-8** encoding to avoid incorrect characters.

---️

### 2️⃣ Installing & Setting Up Django
#### 🚀 Verify Python Installation

Open **CMD** and run:
```
python --version
```

- If Python is **not installed**, download and install it from the official website.
- If the command prints a version number, you're good to go. ✔️

#### Create a Virtual Environment (Recommended)

In **CMD (Run as Administrator)**, navigate to your desired directory and run:
```
python -m venv venv
```

Activate it:
```
venv\Scripts\activate
```

⚠️ The virtual environment must be active before installing Django.

#### Install Django

Navigate to your working directory:
```
cd C:\Users\...
```

Then install Django:
```
pip install django
```

✅ If installation completes successfully, continue to the next step. 

#### 🗂️ Create a New Django Project

Run:
```
django-admin startproject myproject
```

A new folder named ```myproject``` will be created in your current path.

Move into the project directory:
```
cd myproject
```

#### ✨ Run the Development Server

Start the Django server:
```
python manage.py runserver
```

You will receive a local URL such as:
```
http://127.0.0.1:8000/
```

Open it in your browser — you should see the **default Django page with the rocket** 🚀

Stop the server anytime with:
```
Ctrl + C
```

#### Create a Django App

Inside the project directory, run:
```
python manage.py startapp my_app
```

This will generate a new folder named **my_app** inside **myproject**.

#### 💻 Open the Project in VS Code

Run:
```
code .
```

This will open both **myproject** and **my_app** in Visual Studio Code for development. 



### 3️⃣ Install & Configure PostgreSQL & pgAdmin4

#### 🛠️ Install PostgreSQL (Windows)

1. Download PostgreSQL for Windows from the official website.
2. Run the installer → click **Yes** to all prompts.
3. Leave all default components selected:
   - PostgreSQL Server
   - pgAdmin 4
   - Stack Builder
4. Choose the default installation directory.
5. Set a **password** for the default user ```postgres```.
6. Leave the default **port 5432**.
7. Keep all other settings on default.
8. Click **Next** → **Next** → **Install** → **Finish**.


#### 🗃️ Close Stack Builder

After installation finishes, Stack Builder will appear.

➡️ Click **Cancel** and close it — not required for now.

#### 🔄 Optional: Verify PostgreSQL Service

You can optionally check that the PostgreSQL service is running:
1. Open **Services** (Start → type Services).
2. Locate **postgresql-x64-18** (or your installed version).
3. Make sure the **Status** is Running.

If it is stopped, right-click → **Start**.

#### 🖥️ Open pgAdmin4

Go to **Start** → **pgAdmin 4**.

The program opens in your browser.

In the left panel, expand **Servers** → **PostgreSQL 18**.

Enter the password you set earlier.

#### 🧱 Create a New Database

In the left sidebar, right-click **Databases**.

Select **Create** → **Database**…

Enter a **name** for your database.

Click **Save**.

5️⃣6️⃣
### 4️⃣🐘 Connecting Django with PostgreSQL
#### 🔌 Install PostgreSQL Driver

Open the terminal **inside the folder where** ```manage.py``` **exists** and run:
```
pip install psycopg2-binary
```
If the installation completes successfully, continue to the next step.

#### 🗄️ Database Credentials

Use the following settings (adjust values as needed):

- **Database name**: ```library_db```
- **User**: ```postgres```
- **Password**: *(the password you set during PostgreSQL installation)*
- **Host**: ```localhost```
- **Port**: ```5432```

**⚙️ Edit Django Settings** (```settings.py```)

Open the file:
```
your_project/settings.py
```

Find the ```DATABASES``` section and replace it with:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_db',
        'USER': 'postgres',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Save the file.

#### 🔄 Apply Initial Migrations

In the same terminal:
```
python manage.py migrate
```

If everything is correct, Django will create the necessary tables in PostgreSQL.

📁 Create a New Django App

Run:
```
python manage.py startapp library
```

A new folder named **library** will be created inside your project.

#### 🧩 Register the App in Django

Open ```settings.py``` again and find:
```
INSTALLED_APPS = [
```

Add your new app:
```
'library',
```

Save the file.

#### 📚 Define the Book Model

Open:
```
library/models.py
```

Replace the Python code (```models.py```) shown in the folder ```week-02``` of this repository and save the file. 

#### 🏗️ Create and Apply Migrations for the New Model

Run:
```
python manage.py makemigrations
python manage.py migrate
```

This will create the Book table inside the PostgreSQL database according to your model.



---

7️⃣8️⃣



---

*να φτιαξω μια πρριληψη που θα συνδεει ολο το report auto*
*να τα δώσω στο τέλος στο τσατ για emojis και περιληψη γενικη για αυτη την εβδομαδα*


from django.core.management.base import BaseCommand
import pandas as pd
from main.models import Person

class Command(BaseCommand):
    help = "Import Excel data into PostgreSQL"

    def handle(self, *args, **options):
        df = pd.read_excel('main/excel_data/data.xlsx')

        objects = [
            Person(
                name=row['Name'],
                age=row['Age'],
                city=row['City']
            )
            for _, row in df.iterrows()
        ]

        Person.objects.bulk_create(objects)

        self.stdout.write(self.style.SUCCESS("✔ Excel import completed!"))





----
Παρασκευή 


from django.db import models

class Book(models.Model):
    entry_number = models.IntegerField(null=True, blank=True)
    entry_date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    koha_author = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    edition = models.CharField(max_length=255, null=True, blank=True)
    publish_year = models.IntegerField(null=True, blank=True)
    publish_place = models.CharField(max_length=255, null=True, blank=True)
    shape = models.CharField(max_length=255, null=True, blank=True)
    pages = models.CharField(max_length=50, null=True, blank=True)
    volume = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=50, null=True, blank=True)
    column1 = models.CharField(max_length=255, null=True, blank=True)
    column2 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Book"










from django.core.management.base import BaseCommand
import pandas as pd
from main.models import Book

class Command(BaseCommand):
    help = "Import books data from Excel into PostgreSQL"

    def handle(self, *args, **options):
        df = pd.read_excel('main/excel_data/data.xlsx')

        books = []
        for _, row in df.iterrows():
            book = Book(
                entry_number=row.get('entry_number'),
                entry_date=row.get('entry_date'),
                author=row.get('author'),
                koha_author=row.get('koha_author'),
                title=row.get('title'),
                publisher=row.get('publisher'),
                edition=row.get('edition'),
                publish_year=row.get('publish_year'),
                publish_place=row.get('publish_place'),
                shape=row.get('shape'),
                pages=row.get('pages'),
                volume=row.get('volume'),
                notes=row.get('notes'),
                isbn=row.get('isbn'),
                column1=row.get('column1'),
                column2=row.get('column2')
            )
            books.append(book)

        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS("✔ Successfully imported all books!"))






from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all().order_by('entry_number')
    return render(request, 'book_list.html', {'books': books})













from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
]





from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),   # root -> main
    path('admin/', admin.site.urls),
]







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
        <th>Entry #</th>
        <th>Author</th>
        <th>Title</th>
        <th>Publisher</th>
        <th>Year</th>
        <th>ISBN</th>
    </tr>

    {% for book in books %}
    <tr>
        <td>{{ book.entry_number }}</td>
        <td>{{ book.author }}</td>
        <td>{{ book.title }}</td>
        <td>{{ book.publisher }}</td>
        <td>{{ book.publish_year }}</td>
        <td>{{ book.isbn }}</td>
    </tr>
    {% endfor %}
</table>

</body>
</html>
