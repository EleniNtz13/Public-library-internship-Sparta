# 🌟 Week 2 – Overview: Development Environment Setup Overview
This section documents the setup of a local development environment for a library system project. It includes configuring phpMyAdmin for database management, installing Django with a virtual environment, setting up **PostgreSQL** and **pgAdmin4**, and connecting **Django** to the database using models and migrations.
These steps provide the foundation for managing library data and building dynamic web applications.

## ⚙️ phpMyAdmin Setup

### 1️⃣ phpMyAdmin Installation
### 1. 📥 Download phpMyAdmin

Go to the official site: https://www.phpmyadmin.net/downloads/


Download the **All Languages ZIP** version

### 2. 📁 Extract Files

Create a folder inside ```htdocs``` named:

```
C:\Apache24\htdocs\phpmyadmin
```

Extract **all ZIP contents** *directly inside it*

⚠️ Make sure no double folder is created (e.g. phpmyadmin/phpmyadmin).

### 3. ⚙️ Configure phpMyAdmin

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

### 4. ⚙️ Register phpMyAdmin in Apache

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

### 5. ⚙️ Set Default Directory Index
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

### 6. ⚙️ Configure PHP Extensions
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

### 7. Restart Apache

Open **Command Prompt as Administrator**:
```
cd C:\Apache24\bin
httpd -k restart
```

### 8. Access phpMyAdmin

Open:
```
http://localhost/phpmyadmin
```

If configured correctly, the **login page** will appear.
Enter your **MySQL username and password**.

### 2️⃣ 🗄️ Create a Database in phpMyAdmin
### 1. Create New Database

1. Left sidebar → **New**
2. Enter a name
3. Choose collation:
```
utf8mb4_general_ci
```
4. Click **Create**

### 2. 📤 Import Data (CSV)

If you have Excel data:

1. Convert Excel file to **.csv**

2. Open phpMyAdmin → select your database

3. Go to **Import**

4. Upload your CSV file

### 💡 Tip: CSV Import Notes

When importing your .csv file into phpMyAdmin:

- Make sure that the **column names in the CSV match exactly** the fields in your database table (same order, same spelling, no extra spaces).
- If the data does not appear correctly aligned after import, change the **Field Separator** from ```,``` to ```;```.
- Ensure the file is saved in **UTF-8** encoding to avoid incorrect characters.


---


### 3️⃣ Installing & Setting Up Django
### 1. 🚀 Verify Python Installation

Open **CMD** and run:
```
python --version
```

- If Python is **not installed**, download and install it from the official website.
- If the command prints a version number, you're good to go. ✔️

### 2. Create a Virtual Environment (Recommended)

In **CMD (Run as Administrator)**, navigate to your desired directory and run:
```
python -m venv venv
```

Activate it:
```
venv\Scripts\activate
```

⚠️ The **v**irtual **env**ironment must be active before installing Django.

### 3. 📌 Install Django

Navigate to your working directory:
```
cd C:\Users\...
```

Then install Django:
```
pip install django
```

✅ If installation completes successfully, continue to the next step. 

### 4. 🗂️ Create a New Django Project

Run:
```
django-admin startproject myproject
```

A new folder named ```myproject``` will be created in your current path.

Move into the project directory:
```
cd myproject
```

### 5. ✨ Run the Development Server

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

The files ```manage.py``` and ```db.sqlite3``` must be located in the root directory created by the user. Keeping them in the initial folder ensures that Django can properly manage the project and database.


### 6. 📌 Create a Django App

Inside the project directory, run:
```
python manage.py startapp my_app
```

This will generate a new folder named **my_app** inside **myproject**.

### 7. 💻 Open the Project in VS Code

Run:
```
code .
```

This will open **myproject** folder in Visual Studio Code for development. 



### 4️⃣ Install & Configure PostgreSQL & pgAdmin4

### 1. 🛠️ Install PostgreSQL (Windows)

1. Download **PostgreSQL** for *Windows* from the official website: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
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


### 🗃️ Close Stack Builder

After installation finishes, Stack Builder will appear.

➡️ Click **Cancel** and close it — not required for now.

### 🔄 Optional: Verify PostgreSQL Service

You can optionally check that the PostgreSQL service is running:
1. Open **Services** (Start → type Services).
2. Locate **postgresql-x64-18** (or your installed version).
3. Make sure the **Status** is Running.

If it is stopped, right-click → **Start**.

### 2. 🖥️ Open pgAdmin4

Go to **Start** → **pgAdmin 4**.

The program opens in your browser.

In the left panel, expand **Servers** → **PostgreSQL 18**.

Enter the password you set earlier.

### 3. 🧱 Create a New Database

In the left sidebar, right-click **Databases**.

Select **Create** → **Database**…

Enter a **name** for your database.

Click **Save**.


### 5️⃣🐘 Connecting Django with PostgreSQL
### 1. 🔌 Install PostgreSQL Driver

Open the terminal **inside the folder where** ```manage.py``` **exists** and run:
```
pip install psycopg2-binary
```
If the installation completes successfully, continue to the next step.

### 2. 🗄️ Database Credentials

Use the following settings (adjust values as needed):

- **Database name**: ```library_db```
- **User**: ```postgres```
- **Password**: *(the password you set during PostgreSQL installation)*
- **Host**: ```localhost```
- **Port**: ```5432```

**3. ⚙️ Edit Django Settings** **(**```settings.py```**)**

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

#### 4. 🔄 Apply Initial Migrations

In the same terminal:
```
python manage.py migrate
```

If everything is correct, Django will create the necessary tables in PostgreSQL.

#### 5. 📁 Create a New Django App

Run:
```
python manage.py startapp library
```

A new folder named **library** will be created inside your project.

#### 6. 🧩 Register the App in Django

Open ```settings.py``` again and find:
```
INSTALLED_APPS = [
```

Add your new app:
```
'library',
```

Save the file.

#### 7. 📚 Define the Book Model

Open:
```
library/models.py
```

Replace the Python code (```models.py```) shown in the folder ```week-02``` of this repository and save the file. 

#### 8. 🏗️ Create and Apply Migrations for the New Model

Run:
```
python manage.py makemigrations
python manage.py migrate
```

This will create the Book table inside the PostgreSQL database according to your model.


