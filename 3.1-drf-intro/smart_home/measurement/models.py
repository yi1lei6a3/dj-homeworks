from django.db import models


def image_path(instance, filename):
    return '/'.join([
        'sensors_images',
        f'sensor_id_{instance.sensor.id}',
        filename,
    ])


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements',
    )
    temp = models.FloatField()
    image = models.ImageField(upload_to=image_path, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
