from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=200, blank=True, null=True)
    creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre or ''} {self.apellido or ''}".strip()


class Curso(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    creacion = models.DateField(auto_now_add=True)
    estudiantes = models.ManyToManyField(
        Estudiante,
        related_name='cursos',
        blank=True
    )

    def __str__(self):
        return f"{self.nombre or ''}".strip()


class Telefono(models.Model):
    TIPO_TELEFONO = (
        ('C', 'Casa'),
        ('M', 'Celular'),
        ('T', 'Trabajo'),
    )

    telefono = models.CharField(max_length=13, blank=True, null=True)
    creacion = models.DateField(auto_now_add=True)
    tipo = models.CharField(
        max_length=1,
        choices=TIPO_TELEFONO,
        default='C',
    )
    estudiante = models.ForeignKey(
        Estudiante,
        related_name='telefonos',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.telefono or ''}".strip()


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    # Relaciones: autor y autorizador (ambos son estudiantes distintos)
    autor = models.ForeignKey(
        Estudiante,
        related_name='publicaciones_autor',
        on_delete=models.CASCADE
    )
    autorizador = models.ForeignKey(
        Estudiante,
        related_name='publicaciones_autorizador',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo
