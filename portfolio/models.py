from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    descripcion = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imágen", upload_to="projects")
    URLField = models.URLField(verbose_name="Link", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha Alta")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha Actualización")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title