import uuid
from django.db import models
from django_resized import ResizedImageField



class DrawingModel(models.Model):
    """   """
    DRAWNING_STATUS = (
        ('queue', 'В очереди'),
        ('progress', 'Выполняется'),
        ('completed', 'Выполнен'),
    )

    uuid = models.UUIDField(verbose_name="UUID", primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=15, default='queue', choices=DRAWNING_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    order_by = models.PositiveIntegerField(default=0)

    link = models.CharField(blank=True, null=True, max_length=255)
    pdf = models.FileField(upload_to='pdf/', max_length=255, blank=True, null=True)
    prw = ResizedImageField(size = [420, None], max_length=255, upload_to='prw/', quality=80, null=True, blank=True, force_format='WEBP',)    
    webp = models.ImageField(upload_to='webp/', max_length=255, blank=True, null=True)
    webp_size = models.JSONField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чертеж в производстве'
        verbose_name_plural = 'Чертежи в производстве'
        ordering = ['order_by',]



class FileModel(models.Model):
    """ Список файлов в хранилище """

    name = models.CharField(max_length=255)
    link = models.CharField(blank=True, null=True, max_length=255)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'