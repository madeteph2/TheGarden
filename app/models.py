from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    disponible = models.BooleanField()
    cantidad = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    

    def __str__(self):
        return self.nombre



#Tipo de consulta desahabilitado por errores con tailwind

#opciones_consulta = [
#    [0,"Consulta"],
#    [1,"Reclamo"],
#    [2,"Sugerencia"],
#    [3,"Felicitaciones"],
 #   ]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
 #   tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre

