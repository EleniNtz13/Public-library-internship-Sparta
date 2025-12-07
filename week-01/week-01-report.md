## Week 1 – Creating a Simple Web Server Using Python and PHP

The first week focused on creating a basic web server that displays predefined messages on a web page, implemented using both Python and PHP. Below are the steps followed to install the required programming environments and set up the Python version of the project.

### 1️⃣ Python Setup
#### 1. Create the Project Folder

Create a folder named **Project_Folder** in the path:

C:\

#### 2. Create the Python File (app.py)

Using Notepad, create a new file named **app.py** and paste the Python code shown in the folder **week-01** of this repository.
Save the file inside **Project_Folder**, making sure to select **"All Files"** before saving.

#### 3. Create the Templates Folder and HTML File

Inside **Project_Folder**, create a new folder named **templates**.
Open Notepad again and create a file named **index.html**.
Paste the corresponding HTML code (also available in the **week-01** folder), select **"All Files"**, and save it inside the **templates** folder.

#### 4. Install Flask

Open **Command Prompt** and install Flask by running:

*pip install flask*

Then set the Flask application environment variable:

*set FLASK_APP=app.py*

#### 5. Install Python Extension in Visual Studio Code

If Visual Studio Code is not installed, download and install it.
Inside VS Code, go to **Extensions** (left sidebar) and install the **Python extension**.

#### 6. Run the Application

Open the **app.py** file in VS Code and run one of the following commands:

##### Option A: Through Visual Studio Code terminal
*python app.py*

##### Option B: Through Command Prompt

Navigate to the project directory:

*cd C:\Project_Folder*


Then run:

*python app.py*

#### 7. Access the Web Page

If everything is set up correctly, the terminal will display a line similar to:

*Running on http://localhost:5000/*


Open that URL in your browser, and the page will display the messages:

**Hello!**

**Welcome!**

**This is a message.**




2️⃣ PHP Setup
1. Download and Install PHP

Go to the official PHP for Windows download page:

https://windows.php.net/download/


Download the Thread Safe ZIP package for your system and extract the files into a new folder named php in:

C:\


After extraction, your folder should look like:

C:\php\

2. Create the PHP File (index.php)

Inside the C:\php folder, create a new file named index.php using Notepad.
Select "All Files" when saving, and paste the PHP code provided in the week-01 folder.

Example structure:

C:\php\
   └── index.php

3. Install the PHP Extension in Visual Studio Code

Open Visual Studio Code → Go to Extensions → Install the extension named "PHP"
(This enables syntax highlighting and support for PHP code.)

4. Run the PHP Development Server

Open Command Prompt and navigate to the PHP folder:

cd C:\php


Start the built-in PHP development server:

php -S localhost:8080


If everything is correct, the server will start on port 8080.

5. Open the Web Page in Your Browser

Open your browser and visit:

http://localhost:8080


You should now see the displayed messages:

Hello!

Welcome!

This is a message.






## gia php

στον σύνδεσμο: https://windows.php.net/download/ -> install php

δημιουργία φακελου php στο path C: όπου κάνεις extract all files there

στον ίδιο φάκελο δημιουργείς αρχείο index.php all files με τον κώδικα php

εγκαθιστάς το extension php στο visual code

στο τερματικό στο cmd -> cd C:\... ekei pou einai o fakelos αλλάζεις το directory και τρεχεις php -S localhost:8080

παιρνεις το localhost και το περνάς στον browser και εμφανιζει τα μηνύματα 
**Hello!**

**Welcome!**

**This is a message.**




## MySQLDB
για την αποθηκευση των δεδομένων των βιβλίων 

steps:
site: https://dev.mysql.com/downloads/installer/   install last


open file, select: full, steps: next, execute in order to be installed products


create your account and finish the installation


## Apache, without XAMPP and WAMP

Steps for web server:

site: https://www.apachelounge.com/download/ and install the appropriate one


new file -> path C:\Apache24  and extract all files from download there


sto path: C:\Apache24\conf\httpd.conf open last file, make sure the line: Define SRVROOT "/Apache24" deixnei: Define SRVROOT "c:/Apache24" and make sure that the lines below are exist without #:

  LoadModule php_module "c:/php/php8apache2_4.dll"

  AddType application/x-httpd-php .php


  PHPIniDir "C:/php"

and save the file



cmd as admin -> write: 

cd C:\Apache24\bin
httpd.exe -k install, service is installed



in the same terminal write: httpd.exe -k start


browser -> give localhost and then if it is ok appears the message: "It works!"

(php and Apache24 in the same path C:\)




## ρυθμιση php 

sto path C:\Apache24\conf to file httpd antikatastasi sthn proteleytaia grammi poy prosthesame prin toy AddTupe me AddHandler



(proairetika) -> start -> Services.msc -> Apache24 -> restart


sto C:\Apache24\htdocs new file me onoma info.php  apo notepad o code:



<? php
phpinfo();
?>



save as info.php all files



if it is ok, then open browser -> http://.../info.php -> and appears php informations



Τέλος, πέρα από το κομμάτι της πληροφορικής, εργαστήκαμε σε excel με στόχο την καταμέτρηση των βιβλίων και την καλύτερη οργάνωση-ταξινόμηση των βιβλίων της βιβλιθήκης και RFID για  την γρήγορη αναζήτηση όποιου βιβλίου. Τι είναι το RFID?

μήπως να γραψω λίγα λόγια γιατί το κάνουμε όλο αυτό; κάθετι που κάνουμε
