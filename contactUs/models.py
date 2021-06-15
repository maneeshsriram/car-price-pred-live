from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    message = models.TextField()
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.email
