from django.db import models


class Author:
    author = models.CharField(max_length=150, unique=True, db_index=models.CASCADE)



class Genero:
    genero = models.CharField(max_length=100, unique=True, db_index=models.CASCADE)


class Books:
    titulo = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    ano = models.IntegerField(max_length=4)
    genero = models.ForeignKey(Genero)
    price = models.DecimalField(max_length=6, decimal_places=2)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
