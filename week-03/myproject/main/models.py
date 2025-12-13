from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def show_books(request):
    books = Book.objects.all().order_by('entry_number')
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
