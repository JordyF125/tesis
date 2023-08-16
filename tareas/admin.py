from django.contrib import admin
from .models import deportista, eventodeportivo, representante,parametroevaluacion,evaluacionestadofisico,historicorepresentacion,rendimientoinscripcion, asistencia, fechascontrol
##from .models import eventovacacional

admin.site.register(deportista)
admin.site.register(eventodeportivo)
admin.site.register(representante)
admin.site.register(parametroevaluacion)
admin.site.register(evaluacionestadofisico)
admin.site.register(historicorepresentacion)
admin.site.register(rendimientoinscripcion)
admin.site.register(fechascontrol)
admin.site.register(asistencia)