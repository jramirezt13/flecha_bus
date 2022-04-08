from django.contrib import admin
from .models import Trayecto, Bus, Horario, Chofer, Pasajero, Reserva

admin.site.register(Trayecto)
admin.site.register(Bus)
admin.site.register(Horario)
admin.site.register(Chofer)
admin.site.register(Pasajero)
admin.site.register(Reserva)
