from django.db import models

# Create your models here.


class ContactModel(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField()
    Subject = models.CharField(max_length=120)
    Message = models.TextField()

    def __str__(self):
        return self.Name
