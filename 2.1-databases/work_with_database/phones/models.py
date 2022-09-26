from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(max_length=150, verbose_name='Модель')
    image = models.TextField(verbose_name='Фото')
    price = models.IntegerField(verbose_name='Цена')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(verbose_name='LTE')
    slug = models.SlugField(verbose_name='URL', max_length=150, unique=True)

    def __str__(self):
        return f"{self.name} цена {self.price}"

    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        self.slug = slugify(self.name)
