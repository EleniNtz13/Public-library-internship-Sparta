## ρυθμιση php 

sto path C:\Apache24\conf to file httpd antikatastasi sthn proteleytaia grammi poy prosthesame prin toy AddTupe me AddHandler



(proairetika) -> start -> Services.msc -> Apache24 -> restart


sto C:\Apache24\htdocs new file me onoma info.php  apo notepad o code:




<? php
phpinfo();
?>



save as info.php all files



if it is ok, then open browser -> http://.../info.php -> and appears php informations




## εγκατάσταση phpmyadmin 
κατεβασμα απο το site all languages 

δημιουργια φακελου στο htdocs -> phpmyadmin 

εξαγωγη ολων των στιιχειων του zip εκει 
προσοχη μην γινει διπλος φακελος 

στον φακελο που δημιουργησες κάνεις αντιγραφη το config sample.inc.php και το μετονομαζεις το καινούριο σε config.inc.php

ανοίγεις το καινουριο και στηβ γραμμη 16 προσθέτεις εναν τυχαίο κωδικό 32 χαρακτήρων 


ανοίγεις το httpd.conf και προσθέτεις στο τελος 

Alias /phpmyadmin "C:/Apache24/htdocs/phpmyadmin"
<Directory "C:/Apache24/htdocs/phpmyadmin">
    AllowOverride All
    Require all grunted
</Directory>

and save.


cmd as admin
cd C:\Apache24\bin 
httpd -k restart


ανοιξε το http://localhost/phpmyadmin 

αν ειναι οκ θα δεις την φορμα του login για το phpmyadmin όπου συμπληρωνεις username and password. 


## δημιουργία βασης δεδομένων 
new αριστερη στηλη 
create database 
δινεις όνομα και utf8mb4_general_ci and create 

μετατροπη του excel se .csv και μετα import στην βαση δεδομένων.

στο import αν δεν εμφανιζει τα στοιχεια σωστα ταξινομημενα τοτε βάζεις αντι για , βαζεις ;



## επομενο βημα:
εγκατάσταση Django 
cmd ->python --version an einai ok tote einai egkatestimenh h python diaforetika tin katevazeis.

στο ιδιο cmd as admin python -m venv venv 
venv\scripts\activate


cd C:\Users\...


pip install django

αν κατεβηκε επιτυχώς τοτε django-admin startproject myproject που το myproject ειναι ο καινουριος φακελος που δημιουργήθηκε στο path που ειναι ο cmd 

cd myproject


python manage.py runserver



παιρνεις την διεύθυνση ip που θα σου δωσει και θα σου εμφανισει δτο browser την αρχικη της Django εναν πύραυλο 


## επιμενο βημα 
python manage.py startapp my_app το οποιο δημιουργεί φακελο μεσα στο myproject

με την εντολη: code .      

ανοιγει ο φακελος myapp kai myproject στο vs code 




