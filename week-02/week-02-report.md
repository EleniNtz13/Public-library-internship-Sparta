## ⚙️ PHP Configuration & phpMyAdmin Setup
### 1️⃣ Configure PHP in Apache

#### 🔧 Update Apache Configuration (```httpd.conf```)

Navigate to:

```
C:\Apache24\conf
```


Open the file ```httpd.conf``` and locate the line you previously added for ```AddType```.

Instead of that line, type:

```
AddHandler application/x-httpd-php .php
```


Save the file when finished.

#### 🔄 (Optional) Restart Apache via Windows Services

1. Press **Start**
2. Type **services.msc**
3. Find **Apache24**
4. Right-click → **Restart**

#### Create an info.php Test File

Navigate to:

```
C:\Apache24\htdocs
```


Create a new file named ```info.php``` using Notepad.

Insert:
```
<?php
phpinfo();
?>
```

Save it as:
```
info.php
(All Files)
```

#### ▶️ Test in Browser

Open:

```
http://localhost/info.php
```


If everything is correct, you will see the **PHP Information Page**.

### 2️⃣ phpMyAdmin Installation
#### 📥 Download phpMyAdmin

- Go to the official site:
```
https://www.phpmyadmin.net/downloads/
```

- Download the **All Languages ZIP** version

#### 📁 Extract Files

1. Create a folder inside ```htdocs``` named:

```
C:\Apache24\htdocs\phpmyadmin
```

2. Extract **all ZIP contents** *directly inside it*

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
This ensures Apache loads index.php first when a folder is accessed.
💾 Save the file

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
3. Open php.ini
4. Press **Ctrl + F** and search for the following extensions:
- extension=mysqli
- extension=pdo_mysql
5. Remove the semicolon ```;``` in front of them so they become:
```
extension=mysqli
extension=pdo_mysql
```
💾 Save the php.ini file.

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

### 🗄️3️⃣ Create a Database in phpMyAdmin
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



4️⃣ 3️⃣5️⃣ 6️⃣7️⃣8️⃣

---







## επομενο βημα:
εγκατάσταση Django 
cmd ->python --version an einai ok tote einai egkatestimenh h python diaforetika tin katevazeis.

στο ιδιο cmd as admin python -m venv venv 
venv\scripts\activate
(το venv χρειαζεται ωστε να ριναι ενεργοποιημένο)

cd C:\Users\...


pip install django

αν κατεβηκε επιτυχώς τοτε django-admin startproject myproject που το myproject ειναι ο καινουριος φακελος που δημιουργήθηκε στο path που ειναι ο cmd 

cd myproject


python manage.py runserver

παιρνεις την διεύθυνση ip που θα σου δωσει και θα σου εμφανισει δτο browser την αρχικη της Django εναν πύραυλο 
 
με ctrl & c εμφανιζει επομενη γραμμη 

python manage.py startapp my_app το οποιο δημιουργεί φακελο μεσα στο myproject

με την εντολη: code .       

ανοιγει ο φακελος myapp kai myproject στο vs code 


## επιμενο βημα για την δημιουργία φόρμας


εγκατάσταση postgresql απο το αντιστοιχο site για windows

ανοίγεις το αρχειο, ναι σε ολα 

αφηνεις επιλεγμενα τα by default οτι εμφανίσει δηλαδή 

διαλέγεις φακελο εγκατάστασης οτι εμφανισει τον αντίστοιχο 

βαζεις password 

αφηνεις το port ως εχει 5432

αφηνεις default 

next, next, install and finish 


στο πλαίσιο PostgresSQL 18(X64) on port 5432


next cancel close

sto start, pgAdmin4

servers, password 

στο databases δεξι κλικ create -> database δίνεις ονομα και save 

## συνδεση Django με postresql 

στο ιδιο cmd εκει που υπάρχει το manage.py γραψε: 
pip install psycopg2-binary

an einai ok sinexizoyme

δίνεις τα στοιχεια της βασης:
database name: library_db
user: postgres
password: ότι εβαλες ξατα την εγκατάσταση της postresql 
Host: localhost 
Port: 5432

άνοιξε το αρχειο settings.py

στο σημειο DATABASES={7 γραμμές}
αντικτεστησε απο το σημειο με το ονομα 
'NAME': 'library_db',
και προσθεσε τα υπολοιπα στοιχεια που ριναι παραπάνω οπως ακριβως και αυτο 


στο ιδιο cmd τρέξε 
python manage.py migrate 
για να δημιουργηθουν τα tables στην βάση 


στο cmd 
python manage.py startapp library 
για να γινει νεος φακελος με ονομα library στο αντίστοιχο path 



στα settings βρες το INSTALLED_APPS. και προσθεσε τη γραμμή 
**'library_db',      
???**


στο τέλος και save 


στον φακελο library που δημιουργήθηκε βρες το models.py και ανοιξε το στο vs code και αντικατεστησε το με τον κωδικα:


from django.db import models

class Book(models.Model):
    entry_number = models.IntegerField()  # Αριθμός εισαγωγής
    entry_date = models.DateField()       # Ημερομηνία εισαγωγής
    author = models.CharField(max_length=255)  # Συγγραφέας
    koha_author = models.CharField(max_length=255, blank=True, null=True)  # Συγγραφέας Koha
    title = models.CharField(max_length=255)   # Τίτλος
    publisher = models.CharField(max_length=255, blank=True, null=True)  # Εκδότης
    edition = models.CharField(max_length=255, blank=True, null=True)    # Έκδοση
    publish_year = models.IntegerField(blank=True, null=True)  # Έτος έκδοσης
    publish_place = models.CharField(max_length=255, blank=True, null=True)  # Τόπος έκδοσης
    shape = models.CharField(max_length=255, blank=True, null=True)  # Σχήμα
    pages = models.CharField(max_length=50, blank=True, null=True)  # Σελίδες
    volume = models.CharField(max_length=50, blank=True, null=True) # Τόμος
    notes = models.TextField(blank=True, null=True)                 # Παρατηρήσεις
    isbn = models.CharField(max_length=50, blank=True, null=True)   # ISBN
    column1 = models.CharField(max_length=255, blank=True, null=True)  # Στήλη 1
    column2 = models.CharField(max_length=255, blank=True, null=True)  # Στήλη 2

    def __str__(self):
       return self.title


και save

στο cmd
python manage.py makemigrations 
python manage.py migrate



*++να δω το αρχείο ολγ*

---

*ν ελέγχω ταβηματα αν ειανι σωστά*
*να φτιαξω μια πρριληψη που θα συνδεει ολο το report auto*



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
