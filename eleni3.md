**success.html**



<!DOCTYPE html>

<html>

<body>

&nbsp;   <h2>Data saved successfully ✅</h2>

&nbsp;   <a href="/books/add/">Add another book</a>

</body>

</html>







&nbsp; 





**Upload.html**

<!DOCTYPE html>

<html>

<head>

&nbsp;   <title>Upload Excel File</title>

</head>

<body>

&nbsp;   <h2>Upload Excel File</h2>



&nbsp;   <form method="post" enctype="multipart/form-data">

&nbsp;       {% csrf\_token %}

&nbsp;       <input type="file" name="file" required>

&nbsp;       <button type="submit">Upload</button>

&nbsp;   </form>

</body>

</html>



**Views.py**

import pandas as pd

import datetime

from django.shortcuts import render, redirect

from .models import Book

from .forms import BookForm



def show\_books(request):

&nbsp;   books = Book.objects.all()

&nbsp;   return render(request, 'main/book\_list.html', {'books': books})



def add\_book(request):

&nbsp;   if request.method == "POST":

&nbsp;       form = BookForm(request.POST)

&nbsp;       if form.is\_valid():

&nbsp;           form.save()

&nbsp;           return redirect('show\_books')

&nbsp;   else:

&nbsp;       form = BookForm()

&nbsp;   return render(request, 'main/add\_book.html', {'form': form})



def upload\_excel(request):

&nbsp;   if request.method == "POST" and request.FILES.get('file'):

&nbsp;       excel\_file = request.FILES\['file']



&nbsp;       # Διαβάζουμε το Excel αρχείο με pandas

&nbsp;       df = pd.read\_excel(excel\_file)



&nbsp;       # Για κάθε γραμμή του DataFrame, δημιουργούμε ένα βιβλίο στη βάση

&nbsp;       for \_, row in df.iterrows():

&nbsp;           entry\_date\_value = row.get('entry\_date')

&nbsp;           for index, row in df.iterrows():

&nbsp;               print(f"Processing row {index}: {row.to\_dict()}")

&nbsp;               



&nbsp;           # Διαχείριση τύπου ημερομηνίας

&nbsp;           if pd.notnull(entry\_date\_value):

&nbsp;               if isinstance(entry\_date\_value, str):

&nbsp;                   try:

&nbsp;                       entry\_date\_value = datetime.date.fromisoformat(entry\_date\_value)

&nbsp;                   except ValueError:

&nbsp;                       # Αν το string δεν είναι ISO format, προσπάθησε με parse

&nbsp;                       from dateutil.parser import parse

&nbsp;                       entry\_date\_value = parse(entry\_date\_value).date()

&nbsp;               elif hasattr(entry\_date\_value, 'to\_pydatetime'):

&nbsp;                   entry\_date\_value = entry\_date\_value.to\_pydatetime().date()

&nbsp;               elif isinstance(entry\_date\_value, datetime.datetime):

&nbsp;                   entry\_date\_value = entry\_date\_value.date()

&nbsp;           else:

&nbsp;               entry\_date\_value = None



&nbsp;           Book.objects.create(

&nbsp;               entry\_number=row.get('entry\_number'),

&nbsp;               entry\_date=entry\_date\_value,

&nbsp;               author=row.get('author'),

&nbsp;               koha\_author=row.get('koha\_author'),

&nbsp;               title=row.get('title'),

&nbsp;               publisher=row.get('publisher'),

&nbsp;               edition=row.get('edition'),

&nbsp;               publish\_year=row.get('publish\_year'),

&nbsp;               publish\_place=row.get('publish\_place'),

&nbsp;               shape=row.get('shape'),

&nbsp;               pages=row.get('pages'),

&nbsp;               volume=row.get('volume'),

&nbsp;               notes=row.get('notes'),

&nbsp;               isbn=row.get('isbn'),

&nbsp;               column1=row.get('column1'),

&nbsp;               column2=row.get('column2'),

&nbsp;           )

&nbsp;       print("All rows processed successfully!")

&nbsp;       # Μετά την εισαγωγή, κάνουμε redirect στη λίστα βιβλίων

&nbsp;       return redirect('show\_books')



&nbsp;   # Αν GET ή δεν ανέβηκε αρχείο, απλά εμφανίζουμε τη φόρμα ανεβάσματος

&nbsp;   return render(request, 'main/upload\_excel.html')



def success(request):

&nbsp;   return render(request, 'main/success.html')







