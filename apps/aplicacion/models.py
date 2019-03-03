from django.db import models

# Create your models here.
class Usuario(models.Model):
    _dni = models.CharField(max_length = 8, primary_key = True);
    nombre = models.CharField(max_length = 100);
    direccion = models.CharField(max_length = 200);
    telefono = models.CharField(max_length=9);
    email = models.CharField(max_length=50);
    ocupacion = models.CharField(max_length=30);

    def __str__(self):
        return self._dni

class Libro(models.Model):
    titulo = models.CharField(max_length=100);
    autor = models.CharField(max_length=100);
    editorial = models.CharField(max_length=50);

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    fechaEntrega = models.DateField();
    fechaDevolucion = models.DateField();
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE);
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE);


