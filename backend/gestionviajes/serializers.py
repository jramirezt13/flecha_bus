from rest_framework import serializers
from .models import Trayecto, Bus, Horario, TrayectoBusHorario, Chofer, Pasajero, Reserva

# se serializa la información para acceder a ella
class TrayectoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trayecto
        fields='__all__'
        
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bus
        fields='__all__'
        
class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Horario
        fields='__all__'
        
class Chofer(serializers.ModelSerializer):
    class Meta:
        model=Chofer
        fields='__all__'
        
class Reserva(serializers.ModelSerializer):
    class Meta:
        model=Reserva
        fields='__all__'
        
class Pasajero(serializers.ModelSerializer):
    class Meta:
        model=Pasajero
        fields='__all__'
        
class TrayectoBusHorario(serializers.ModelSerializer):
    class Meta:
        model=TrayectoBusHorario
        fields='__all__'