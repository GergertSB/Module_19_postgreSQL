from django.db import models
from django.db.models import CASCADE


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    name_source = models.CharField(max_length=20, null=True)
    date_message = models.DateField()

    def __str__(self):
        return self.title

class Category(models.Model):
    CATEGORY = [
        ('FIN', 'Finance'),
        ('WRD', 'Worlds'),
        ('СIT', 'City'),
        ('ANM', 'Animals'),
        ('TCH', 'Technology'),
        ('PRG', 'Programming'),
    ]

    title = models.CharField(max_length=100)
    author = models.ForeignKey(News, on_delete=models.CASCADE, related_name='name')
    cat = models.CharField(max_length=3, choices=CATEGORY, default='FIN',)

    def __str__(self):
        return self.title
