# 🌟 Week 1 – Overview: Development Stack
During the first week of the internship, we set up the basic tools to create simple web applications. 
The goal was to build two small web servers (Python and PHP) and connect them with a MySQL database and Apache HTTP Server to create a complete development environment.

- 🐍 **Python (Flask)**: Lightweight server for displaying messages and handling HTML templates (```localhost:5000```).

- 🐘 **PHP**: Runs via the built-in PHP server (```localhost:8080```) or through Apache for a more production-like setup (```localhost:80```).

- ⚡ **Apache HTTP Server**: Provides a stable environment to serve PHP pages.

- 💾 **MySQL Database**: Stores and manages data such as books, users, and categories.

Together, these tools form a simple development stack that allows message display, data management, and local web server operation — forming the foundation for more advanced features in the library system.

Below are the steps to install and set up the development environments for **both Python and PHP**.

## 1️⃣ Python Setup
### 1. Create the Project Folder

Create a folder named ```Project_Folder``` in the path:

```
C:\
```

### 2. Create the Python File (```app.py```)

Using Notepad, create a new file named ```app.py``` and paste the Python code shown in the folder ```week-01``` of this repository.
Save the file inside ```Project_Folder```, making sure to select **"All Files"** before saving.

### 3. Create the Templates Folder and HTML File

Inside **Project_Folder**, create a new folder named ```templates```📂.
Open Notepad again and create a file named ```index.html```.
Paste the corresponding HTML code (also available in the ```week-01``` folder), select **"All Files"**, and save it inside the ```templates``` folder.

### 4. Install Flask

Open **Command Prompt** 💻 and install Flask by running:

```
pip install flask
```

Then set the Flask application environment variable:

```
set FLASK_APP=app.py
```

### 5. Install Python Extension in Visual Studio Code

If Visual Studio Code is not installed, download and install it.
Inside VS Code, go to **Extensions** 🔌 (left sidebar) and install the **Python extension**.

### 6. Run the Application

Open the ```app.py``` file in VS Code and run one of the following commands:

#### Option A: Through Visual Studio Code terminal
```
python app.py
```

#### Option B: Through Command Prompt

Navigate to the project directory:

```
cd C:\Project_Folder
python app.py
```

### 7. Access the Web Page

If everything is set up correctly, the terminal will display a line similar to:

```
Running on http://localhost:5000/
```


Open that URL in your browser, and the page will display the messages:

👋 **Hello!**

🎉 **Welcome!**

📝 **This is a message.**


## 2️⃣ PHP Setup
### 1. Download and Install PHP

Go to the official PHP for Windows download page: https://windows.php.net/download/

Download the **Thread Safe ZIP package** and extract it into:

```
C:\php
```

### 2. Create the PHP File (```index.php```)

Inside the ```C:\php``` folder, create a new file named ```index.php``` using Notepad.
Select **"All Files"** when saving, and paste the PHP code provided in the ```week-01``` folder.

Example structure:

```
C:\php\
   └── index.php
```

### 3. Install the PHP Extension in Visual Studio Code

Open Visual Studio Code → Go to **Extensions** 🔌 → Install the extension named **PHP** (this enables syntax highlighting and support for PHP code)

### 4. Run the PHP Development Server

Open **Command Prompt** 💻 and type:

```
cd C:\php
php -S localhost:8080
```


If everything is correct, the server will start on port 8080.

### 5. Open the Web Page in Your Browser

Open your browser and visit:

```
http://localhost:8080
```


You should now see the displayed messages:

👋 **Hello!**

🎉 **Welcome!**

📝 **This is a message.**

---

After setting up the basic web servers using Python and PHP, the next step was to prepare the environment required for data storage and dynamic content management. For this purpose, a relational database system was introduced, using 💾 **MySQL**, which allows the application to store, retrieve, and manage library-related data efficiently (such as book information, categories, and user activity).

Additionally, the setup process included the installation and configuration of the ⚡ **Apache HTTP Server**, which provides a stable, production-level environment for serving PHP applications. Apache enables the web server to deliver PHP pages reliably and is commonly used in combination with MySQL to create full-stack web applications.

The following sections describe the installation steps for **MySQL** and **Apache**, as well as how they integrate with the overall project architecture.


## 3️⃣ MySQL Database (MySQL Server)

**MySQL**: 
- 💾 is one of the most widely used relational database systems, ideal for web applications like the ones developed during this project,
- 🗄️ is used to store, retrieve, and manage data such as book information, categories, and user activity.

## Installation Steps (Windows)
### 1. Download MySQL Installer

- Visit the official MySQL download page: https://dev.mysql.com/downloads/installer/


- Download the **latest MySQL Installer** for Windows.

### 2. Run the Installer

- Open the downloaded file and choose **Full** → **Next** → **Execute**


This installs:

```
- MySQL Server
- MySQL Workbench
- MySQL Shell
- Utilities and connectors required for development
```

This installs all selected products.

### 3. Complete Configuration

- During the setup:
```
  - Create your MySQL root account (username + password)
  - Choose the default configuration options
  - Finalize the installation
```

When the process finishes, MySQL Workbench will be available for use.



## 4️⃣ Apache HTTP Server Setup (Without XAMPP/WAMP)

**Apache**:
- ⚡ is one of the most widely used web servers globally and serves as the backbone for running PHP applications in a stable, production-style environment.
- 🖥️ In this project, Apache is used to process and serve PHP pages directly from the local machine, creating a fully functional local web server setup.

## Installation Steps:
### 1. Download Apache

- Visit the Apache Lounge download page: https://www.apachelounge.com/download/


- Download the version compatible with your system.

### 2. Extract Apache Files

- Create a new folder in the root of your C: drive:

```
C:\Apache24
```


- Extract all downloaded files into this folder so your structure becomes:

```
C:\Apache24\bin
C:\Apache24\conf
C:\Apache24\htdocs
...
```

### 3. Configure Apache to Work with PHP

- Navigate to:

```
C:\Apache24\conf
```


- Open the file:

**httpd.conf**


- Make the following adjustments:

### ✔ Update the ServerRoot path

- Locate:

```
Define SRVROOT "/Apache24"
```


- Change it to:

```
Define SRVROOT "c:/Apache24"
```

### ✔ Enable PHP module and configuration
 
- Ensure that the following lines exist **without the # symbol** (uncommented):

```
LoadModule php_module "c:/php/php8apache2_4.dll"

AddType application/x-httpd-php .php

PHPIniDir "C:/php"
```

These lines tell Apache how to load the PHP module and where to find the PHP configuration.

- Save the file.

### 4. Install and Start the Apache Service

- Open **Command Prompt as Administrator** 💻 and run:

#### Install Apache as a service:
```
cd C:\Apache24\bin
```
And, then:
```
httpd.exe -k install
```


This registers Apache as a Windows service.

#### Start the Apache server:
```
httpd.exe -k start
```


If everything is correct, the server will start without errors.

### 5. Test the Installation

- Open your browser and visit:

```
http://localhost
```


If Apache is running successfully, you should see the message:

**It works!** ✅


### 6. Configure PHP in Apache

**🔧Update Apache Configuration** (```httpd.conf```)

Navigate to:

```
C:\Apache24\conf
```


Open the file ```httpd.conf``` and locate the line you previously added for ```AddType```. Instead of that line, type:

```
AddHandler application/x-httpd-php .php
```

Save the file when finished.

#### 🔄 (Optional) Restart Apache via Windows Services

1. Press **Start**
2. Type **services.msc**
3. Find **Apache24**
4. Right-click → **Restart**

**Create an** ```info.php``` **Test File**

Navigate to:

```
C:\Apache24\htdocs
```


Create a new file named ```info.php``` using Notepad. Insert:
```
<?php
phpinfo();
?>
```

Save it as:
```
info.php
```
(All Files)


#### ▶️ Test in Browser

Open:
```
http://localhost/info.php
```

- If everything is correct, you will see the **PHP Information Page**.


### ✔ Important Note

Make sure that ```php``` and ```Apache24``` are both located on the ```C:\drive```, since the configuration paths depend on this structure:

```
C:\php
C:\Apache24
```


**Note**: All servers run on localhost and are only accessible from your local machine. They are not exposed to the internet.


| Server   | Technology | Port |
| -------- | ---------- | ---- |
| 🐍 Flask | Python     | 5000 |
| 🐘 PHP   | Built-in   | 8080 |
| ⚡ Apache | PHP        | 80  |
