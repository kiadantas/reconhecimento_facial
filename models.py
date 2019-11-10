from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Dados(models.Model):
    name = models.CharField(max_length=255)
    matricula = models.IntegerField()
    curso = models.CharField(max_length=255)
    periodo = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    modifield = models.DateField('Modificado em', auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Picture(models.Model):
    picture = models.ForeignKey(Dados, on_delete=models.CASCADE, related_name='images')
#    image = CloudinaryField('Imagem', blank=True, null=True)
    description = models.CharField('Descrição', max_length=200, blank=True, default='')

    def __self__(self):
        return self.picture.name

class Meta:
    verbose_name = 'Imagem Face'
    verbose_name = 'Imagem da face'

