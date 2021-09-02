from django.db import models

# Create your models here.

class People(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    profession = models.CharField(max_length=254)

    class Meta:
        db_table = "peoples_people"