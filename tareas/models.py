##tareas/models.py
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django import forms
from  django.db import IntegrityError


##TablaMaestra1
class deportista(models.Model):
    ##Para elección de sexo
    MASCULINO = "M"
    FEMENINO = "F"
    SEXO_OPCIONES = [
        (MASCULINO, "Masculino"),
        (FEMENINO, "Femenino"),
    ]
    ##Para elección de tipo de deportista
    MASTER="MASTER"
    EVENTUAL="EVENTUAL"
    TIPODEPORTISTA_OPCIONES = [
        (MASTER, "Master"),
        (EVENTUAL, "Eventual"),
    ]

    ##PARA ELECCIÓN TIPO DE SANGRE
    APOSITIVO="A+"
    ANEGATIVO="A-"
    BPOSITIVO="B+"
    BNEGATIVO="B-"
    ABPOSITIVO="AB+"
    ABNEGATIVO="AB-"
    OPOSITIVO="O+"
    ONEGATIVO="O-"
    TIPODESANGRE_OPCIONES = [
        (APOSITIVO, "A+"),
        (ANEGATIVO, "A-"),
        (BPOSITIVO, "B+"),
        (BNEGATIVO, "B-"),
        (ABPOSITIVO, "AB+"),
        (ABNEGATIVO, "AB-"),
        (OPOSITIVO, "O+"),
        (ONEGATIVO, "O-"),
    ]

    ##foto=ImageField(upload_to='tareas/images',blank=True)
    ##foto=ImageField(upload_to='media/tareas/images/',blank=True)
    foto=ImageField(null=True,blank=True,upload_to='images/')
    ceduladeportista =models.CharField("Cédula",max_length=10, unique=True)

    tipodeportista=models.CharField("Tipo de deportista",
        max_length=8,
        choices=TIPODEPORTISTA_OPCIONES ,
        default=EVENTUAL,
    )
    
    sexo = models.CharField("Sexo",
        max_length=1,
        choices=SEXO_OPCIONES,
        default=MASCULINO,
    )

    tiposangre=models.CharField("Tpo de sangre",
        max_length=3,
        choices=TIPODESANGRE_OPCIONES ,
        default=OPOSITIVO,
    )
    apellidosdeportista=models.CharField("Apellidos",max_length=100)
    nombresdeportista=models.CharField("Nombres",max_length=100)
    fecnacdeportista = models.DateField("Fecha de nacimiento",null=True,default='1990-01-01')
    email=models.EmailField("Email",max_length=254, blank=True,default="sincorreo@sincorreo.com")
    direcciondeportista=models.TextField("Dirección",max_length=200, blank=True)
    telefonofijo=models.CharField("Teléfono fijo",max_length=20, blank=True)
    telefonomovil=models.CharField("Teléfono movil",max_length=20, blank=True)
    usuario=models.CharField("Usuario",max_length=100, unique=True)
    clave=models.CharField("Contraseña",max_length=100)

    def __str__(self):
        return self.apellidosdeportista +' '+ self.nombresdeportista

##TablaMaestra2
class eventodeportivo(models.Model):
    ##PARA ELECCIÓN TIPO DE EVENTO
    COMPETENCIA="COMPETENCIA"
    CURSO="CURSO"
    VACACIONAL="VACACIONAL"
    TIPOEVENTO_OPCIONES = [
        (COMPETENCIA, "COMPETENCIA"),
        (CURSO, "CURSO"),
        (VACACIONAL, "VACACIONAL"),
    ]

    fechainicioevento = models.DateField("Fecha de inicio",null=True)
    fechafinevento = models.DateField("Fecha de fin",null=True)
    descripcion=models.CharField("Descripción",max_length=100)
    tipoevento=models.CharField("Tipo de evento",
        max_length=12,
        choices=TIPOEVENTO_OPCIONES ,
        default=VACACIONAL,
    )
    estado = models.BooleanField("Activo/Inactivo",default=True)

    def __str__(self):
        return self.descripcion 

##TablaMaestra3
class representante(models.Model):
    cedularepresentante =models.CharField("Cédula",max_length=10, unique=True)    
    apellidosrepresentante=models.CharField("Apellidos",max_length=100)
    nombresrepresentante=models.CharField("Nombres",max_length=100)
    telefonofijo=models.CharField("Teléfono fijo",max_length=20, blank=True)
    telefonomovil=models.CharField("Teléfono móvil",max_length=20, blank=True)
    email=models.EmailField("Email",max_length=254, blank=True,default="sincorreo@sincorreo.com")
    direccionrepresentante=models.TextField("Dirección",max_length=200, blank=True)
    def __str__(self):
        return self.apellidosrepresentante +' '+ self.nombresrepresentante

##TablaMaestra4
class parametroevaluacion(models.Model):
    descripcionparametro=models.CharField("Descripción del parámetro",max_length=100)
    ponderacionminima=models.DecimalField("Mínimo normal",max_digits=5, decimal_places=2)
    ponderacionmaxima=models.DecimalField("Máximo normal",max_digits=5, decimal_places=2)
    unidadmedida=models.CharField("Unidad de medida",max_length=20)
    
    def __str__(self):
        return self.descripcionparametro 

##TablaMaestra5
class fechascontrol(models.Model):
    fecha = models.DateField("Fecha")
    def __str__(self):
        return str(self.fecha)

##TablaOperacional1
class evaluacionestadofisico(models.Model):
    parametroevaluacion = models.ForeignKey('parametroevaluacion', on_delete=models.CASCADE, null=True)
    deportista = models.ForeignKey('deportista', on_delete=models.CASCADE, null=True)
    fecha = models.DateField("Fecha")
    valor=models.DecimalField("Valor",max_digits=5, decimal_places=2)
    observacion=models.TextField("Observación",max_length=200)
    def __str__(self):
        return self.deportista.apellidosdeportista +' '+self.deportista.nombresdeportista + ':' + str(self.valor)


##TablaOperacional2
class historicorepresentacion(models.Model):
    representante = models.ForeignKey('representante', on_delete=models.CASCADE, null=True)
    deportista = models.ForeignKey('deportista', on_delete=models.CASCADE, null=True)
    periodorepresentacion=models.CharField("Período de representación",max_length=100)
    observacion=models.TextField("Observación",max_length=100)
    def __str__(self):
        return self.deportista.apellidosdeportista +' '+self.deportista.nombresdeportista + ' representado por :' + self.representante.apellidosrepresentante + ' ' + self.representante.nombresrepresentante

##TablaOperacional3
class rendimientoinscripcion(models.Model):
    ##PARA ELECCIÓN TIPO DE ESTILO
    PECHO="PECHO"
    MARIPOSA="MARIPOSA"
    ESPALDA="ESPALDA"
    LIBRE="LIBRE"
    AGUAS_ABIERTAS="AGUAS_ABIERTAS"
    VACACIONAL="VACACIONAL"

    TIPOESTILO_OPCIONES = [
        (PECHO, "PECHO"),
        (MARIPOSA, "MARIPOSA"),
        (ESPALDA, "ESPALDA"),
        (LIBRE, "LIBRE"),
        (AGUAS_ABIERTAS, "AGUAS_ABIERTAS"),
        (VACACIONAL, "VACACIONAL"),
    ]
    evento = models.ForeignKey('eventodeportivo', on_delete=models.CASCADE, null=True)
    deportista = models.ForeignKey('deportista', on_delete=models.CASCADE, null=True)
    fecha = models.DateField("Fecha")
    posicion=models.CharField("Posición",max_length=20, blank=True)
    tiempominutos=models.DecimalField("Minutos para llegar",max_digits=5, decimal_places=2)
    tiemposegundos=models.DecimalField("Segundos para llegar",max_digits=5, decimal_places=2)
    tipoestilo=models.CharField("Estilo evaluado",
        max_length=15,
        choices=TIPOESTILO_OPCIONES ,
        default=VACACIONAL,
    )
    observacion=models.TextField("Observación",max_length=100)
    def __str__(self):
        return self.deportista.apellidosdeportista +' '+self.deportista.nombresdeportista + ':' + self.evento.descripcion

##TablaOperacional4
class asistencia(models.Model):
    deportista = models.ForeignKey('deportista', on_delete=models.CASCADE, null=True)
    fechacontrol = models.ForeignKey('fechascontrol', on_delete=models.CASCADE, null=True)
    controlasiste = models.BooleanField("Asistencia/inasistencia",default=True)
    observacion=models.TextField("Observación/Justificación",max_length=100, blank=True)
    def __str__(self):
        return self.deportista.apellidosdeportista +' '+self.deportista.nombresdeportista + ' ; ' + str(self.fechacontrol.fecha) + ' ; ' + str(self.controlasiste)
    