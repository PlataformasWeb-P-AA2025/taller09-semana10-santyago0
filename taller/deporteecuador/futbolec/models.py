from django.db import models

# Create your models here.

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=5)
    username_twitter = models.CharField(max_length=30)

    campeonatos = models.ManyToManyField('Campeonato', through='CampeonatoEquipos')

    def __str__(self):
        return "%s (%s) - %s" % (self.nombre,
                self.siglas,
                self.username_twitter)


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    posicion_campo = models.CharField(max_length=30)
    numero_camiseta = models.IntegerField()
    sueldo = models.IntegerField()

    equipo = models.ForeignKey(EquipoFutbol, related_name='jugadores',
            on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s (%d) - %s | $%d" % (self.nombre,
                self.numero_camiseta,
                self.posicion_campo,
                self.sueldo)


class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=30)
    nombre_auspiciante = models.CharField(max_length=30)

    equipos = models.ManyToManyField(EquipoFutbol, through='CampeonatoEquipos')

    def __str__(self):
        return "%s - %s" % (self.nombre_campeonato, self.nombre_auspiciante)
    

class CampeonatoEquipos(models.Model):
    equipo_futbol = models.ForeignKey(EquipoFutbol, related_name='campeonatoequipos',
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey('Campeonato', related_name='campeonatoequipos',
            on_delete=models.CASCADE)
    
    anio = models.IntegerField()
    
    def __str__(self):
        return "%d | Campeonato: (%s) - Participante: %s" % (self.anio,
                self.campeonato,
                self.equipo_futbol.nombre)
