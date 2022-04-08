from datetime import datetime
from django.db import models
from birthday import BirthdayField


class Trayecto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', null=False, blank=False, unique=True)

    def __str__(self):
        return self.nombre
    
class Horario(models.Model):
    hora = models.TimeField()
    
    def __str__(self):
        return str(self.hora)
        
class Bus(models.Model):
    patente = models.CharField(max_length=10,verbose_name='Patente',null=False, blank=False, unique=True)
    modelo = models.CharField(max_length=30, verbose_name='Modelo', null=False, blank=False)
    marca = models.CharField(max_length=50, verbose_name='Marca', null=False, blank=False)
    capacidad = models.IntegerField(max_length=40, verbose_name='Capacidad', default='10', null=True, blank=True)
    trayecto = models.OneToOneField(Trayecto, on_delete=models.CASCADE, related_name = "bus_trayecto", null=True, blank=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE, related_name = "bus_horario", null=True, blank=True)
    
    def __str__(self):
        fila = "Patente: " + self.patente + " - " + "Modelo: " + self.modelo + " - " + 'Marca: ' + self.marca
        return fila
    
class Meta:
    ordering = ('marca','patente',)

    
class Chofer(models.Model):
    opciones=(
        ('maculino','Masculino'),
        ('femenino','Femenino'),
    )
    nombre = models.CharField(max_length=10,verbose_name='Nombre',null=False, blank=False)
    apellido = models.CharField(max_length=10,verbose_name='Apellido',null=False, blank=False)
    dni = models.IntegerField(max_length=10, verbose_name='DNI', null=False, blank=False, unique=True)
    genero = models.CharField(max_length=30, choices=opciones, verbose_name='Genero', null=False, blank=False)
    fecha_nacimiento = BirthdayField()
    bus = models.OneToOneField(Bus, on_delete=models.CASCADE, related_name = "chofer_bus", null=True, blank=True)

    
    def __str__(self):
        fila =  str(self.dni) + " - " + self.nombre + " " + self.apellido
        return fila
    
    
class Pasajero(models.Model):
    opciones=(
        ('maculino','Masculino'),
        ('femenino','Femenino'),
    )
    nombre = models.CharField(max_length=10,verbose_name='Nombre',null=False, blank=False)
    apellido = models.CharField(max_length=10,verbose_name='Apellido',null=False, blank=False)
    dni = models.IntegerField(max_length=10, verbose_name='DNI', null=False, blank=False, unique=True)
    genero = models.CharField(max_length=30, choices=opciones, verbose_name='Genero', null=False, blank=False)
    correo = models.EmailField(max_length=50, verbose_name='Correo', null=True, blank=True, unique=True)
    fecha_nacimiento = BirthdayField()
    
    def __str__(self):
        fila =  str(self.dni) + " - " + self.nombre + " " + self.apellido
        return fila
    
class PasajeroBus(models.Model):
    bus = models.OneToOneField(Bus, on_delete=models.CASCADE,null=False, blank=False)
    pasajero = models.OneToOneField(Pasajero, on_delete=models.CASCADE,null=False, blank=False)
    numero_asiento = models.IntegerField(max_length=10, null=False, blank=False)
    
    def __str__(self):
        fila = + self.pasajero.nombre + " " + self.pasajero.apellido + " - " +str(self.numero_asiento)
        return fila
    
    

def generar_numero_reserva():
    reserva = Reserva.objects.all().order_by('id').last()
    if not reserva:
        return str(datetime.today().year) + str(datetime.today().month).zfill(2) +  str(datetime.today().timestamp()).replace(".", "")
    numero_reserva_int = reserva.id + 1
    nuvo_numero_reserva = str(str(datetime.today().year)) + str(datetime.today().month).zfill(2) + str(datetime.today().timestamp()).replace(".", "") + str(numero_reserva_int)
    return nuvo_numero_reserva
    
class Reserva(models.Model):
    numero_reserva = models.CharField(max_length=100, default = generar_numero_reserva, editable=False)
    pasajero = models.ForeignKey(PasajeroBus, on_delete=models.CASCADE,null=True, blank=True)
    estatus = models.BooleanField(default=True)
    
    def __str__(self):
        fila =  self.pasajero.nombre + " " + self.pasajero.apellido + " - Número de reserva: " + str(self.numero_reserva)
        return fila
    
    