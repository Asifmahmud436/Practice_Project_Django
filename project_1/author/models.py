from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=8)
    last_name = models.CharField(max_length=8)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name +' ' +self.last_name
