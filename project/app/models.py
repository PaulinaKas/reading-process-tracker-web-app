from django.db import models

class Book(models.Model):
    title = models.TextField(default='')
    current_page = models.IntegerField(default='')
    total_pages = models.IntegerField(default=''
    )
