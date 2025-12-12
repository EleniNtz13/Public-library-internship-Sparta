from django.db import models

class Book(models.Model):
    entry_number = models.IntegerField()  
    entry_date = models.DateField()       
    author = models.CharField(max_length=255)  
    koha_author = models.CharField(max_length=255, blank=True, null=True)  
    title = models.CharField(max_length=255)   
    publisher = models.CharField(max_length=255, blank=True, null=True)  
    edition = models.CharField(max_length=255, blank=True, null=True)    
    publish_year = models.IntegerField(blank=True, null=True)  
    publish_place = models.CharField(max_length=255, blank=True, null=True)  
    shape = models.CharField(max_length=255, blank=True, null=True)  
    pages = models.CharField(max_length=50, blank=True, null=True)  
    volume = models.CharField(max_length=50, blank=True, null=True) 
    notes = models.TextField(blank=True, null=True)                 
    isbn = models.CharField(max_length=50, blank=True, null=True)   
    column1 = models.CharField(max_length=255, blank=True, null=True)  
    column2 = models.CharField(max_length=255, blank=True, null=True)  

    def __str__(self):
        return self.title
