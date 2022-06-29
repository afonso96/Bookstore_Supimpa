from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=150, unique=True, db_index=True)


class Genre(models.Model):
    genre = models.CharField(max_length=100, unique=True, db_index=True)
    image = models.ImageField()


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField(max_length=4)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
