from django.db import models
from author.models import Author

class Album(models.Model):
    name = models.CharField(max_length=20)
    release_date = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

