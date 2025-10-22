from django.db import models

class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre_cine = models.CharField(max_length=100, help_text="Nombre del cine")
    direccion = models.TextField()
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    numero_salas = models.IntegerField()
    imagen_sucursal = models.ImageField(upload_to='img_sucursales/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_cine} - {self.ciudad}"

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

class Sala(models.Model):
    TIPO_SALA_CHOICES = [
        ('VIP', 'VIP'),
        ('Tradicional', 'Tradicional'),
        ('4DX', '4DX'),
        ('3D', '3D'),
        ('Junior', 'Junior'),
        ('IMAX', 'IMAX'),
    ]
    
    ESTADO_SALA_CHOICES = [
        ('Ocupada', 'Ocupada'),
        ('Desocupada', 'Desocupada'),
        ('En mantenimiento', 'En mantenimiento'),
    ]
    
    id_sala = models.AutoField(primary_key=True)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='salas')
    numero_sala = models.IntegerField()
    tipo_sala = models.CharField(max_length=20, choices=TIPO_SALA_CHOICES)
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_SALA_CHOICES)

    def __str__(self):
        return f"Sala {self.numero_sala} - {self.tipo_sala}"

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"