from django.contrib import admin

# Register your models here.

from futbolec.models import *

# Agregar la clase EquipoFutbol para administrar desde interfaz de administración
# Se crea una clase que hereda de ModelAdmin para el modelo EquipoFutbol
class EquipoFutbolAdmin(admin.ModelAdmin):
    # Listado de atributos que se mostrará por cada registro
    # Dejamos de usar la representación (str) de la clase
    list_display = ('nombre', 'siglas', 'username_twitter')
    search_fields = ('nombre', 'username_twitter')
    exclude = ("campeonatos",)

admin.site.register(EquipoFutbol, EquipoFutbolAdmin)

# Agregar la clase Jugador para administrar desde interfaz de administración
# Se crea una clase que hereda de ModelAdmin para el modelo Jugador
class JugadorAdmin(admin.ModelAdmin):
    # Listado de atributos que se mostrará por cada registro
    # Dejamos de usar la representación (str) de la clase
    list_display = ('nombre', 'posicion_campo', 'numero_camiseta', 'sueldo', 'get_equipo')
    search_fields = ('nombre', 'numero_camiseta', 'equipo__nombre')

    def get_equipo(self, objt):
        return objt.equipo.nombre

admin.site.register(Jugador, JugadorAdmin)

# Agregar la clase Campeonato para administrar desde interfaz de administración
# Se crea una clase que hereda de ModelAdmin para el modelo Campeonato
class CampeonatoAdmin(admin.ModelAdmin):
    # Listado de atributos que se mostrará por cada registro
    # Dejamos de usar la representación (str) de la clase
    list_display = ('nombre_campeonato', 'nombre_auspiciante')
    search_fields = ('nombre_campeonato',)
    exclude = ('equipos',)

admin.site.register(Campeonato, CampeonatoAdmin)

# Agregar la clase CampeonatoEquipos para administrar desde interfaz de administración
# Se crea una clase que hereda de ModelAdmin para el modelo CampeonatoEquipos
class CampeonatoEquiposAdmin(admin.ModelAdmin):
    # Listado de atributos que se mostrará por cada registro
    # Dejamos de usar la representación (str) de la clase
    list_display = ('anio', 'equipo_futbol', 'campeonato')
    search_fields = ('equipo_futbol__nombre',)

admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)
