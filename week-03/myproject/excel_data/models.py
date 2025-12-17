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
