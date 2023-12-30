from django.db import models

# Create your models here.
class Movies(models.Model):
    title=models.CharField(max_length=50)
    director=models.CharField(max_length=20)
    year=models.IntegerField()
    about=models.CharField(max_length=100)
    link=models.CharField(max_length=80)
    poster=models.ImageField(upload_to="movies/poster")

    def __str__(self):
        return self.title
