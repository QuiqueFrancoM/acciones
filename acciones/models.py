from django.db import models
class persona(models.Model):
    alias = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    foto = models.ImageField(upload_to='./static/images/personas', null=True, blank=True)
    correo = models.EmailField()
    telefono = models.IntegerField(null=True, blank=True)
    def __str__(self):
        ali = self.nombre + " ("+self.alias+")"
        return ali

class acciones(models.Model):
    titulo = models.CharField(max_length=50)
    origen = models.CharField(max_length=50, null=True)
    creador = models.ForeignKey(persona, on_delete=models.DO_NOTHING, null=True, related_name='creador')
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    responsable = models.ForeignKey(persona, on_delete=models.DO_NOTHING, null=True, related_name='responsable')
    descripcion = models.TextField(null=True, blank=True)
    terminada = models.BooleanField(default=False)
    prioridad = models.IntegerField(default=10, null=True)
    fecha_prog_inicio = models.DateField(null=True, blank=True)
    fecha_prog_fin = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='./static/images/acciones', null=True, blank=True)
    def __str__(self):
        a =  str(self.pk) + ".- "+ self.titulo
        return a