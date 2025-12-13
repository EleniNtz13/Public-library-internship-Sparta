---





1️⃣2️⃣3️⃣





5️⃣6️⃣7️⃣8️⃣
















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
