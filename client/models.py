import os, datetime, random
from django.conf import settings
from django.core.files import File
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from io import BytesIO
from pathlib import Path


def upload_file_name(instance, filename):
    _, ext = os.path.splitext(filename)

    return "profile/{}/{:%Y-%m-%d-%H-%M-%S}-{}{}".format(
        datetime.datetime.now().strftime("%m%Y"),
        datetime.datetime.now(),
        random.randint(1000, 9999), ext)


class User(AbstractUser):
    photo = models.ImageField(upload_to=upload_file_name)

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def save(self, *args, **kwargs):
        if not self.photo.closed:
            img = Image.open(self.photo)
            img.thumbnail((1024, 1024), Image.ANTIALIAS)

            tmp = BytesIO()
            img.save(tmp, 'PNG')

            self.photo = File(tmp, 't.png')

        return super().save(**kwargs)

    @property
    def image_url(self):
        if self.photo:
            return os.path.join(settings.MEDIA_URL, str(self.photo))



class Category(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0
    admin = models.ForeignKey(User, on_delete=models.RESTRICT, default=None, null=True)
    parent = models.ForeignKey('client.Category',
                               verbose_name="Otasi",
                               on_delete=models.RESTRICT,
                               null=True,
                               default=None,
                               blank=True)
    name_uz = models.CharField(max_length=50, verbose_name="O'zbekcha")
    name_ru = models.CharField(max_length=50, verbose_name="Ruscha")
    status = models.SmallIntegerField( choices=(
        (STATUS_ACTIVE, 'Faol'),
        (STATUS_INACTIVE, 'Nofaol')
    ), default=STATUS_ACTIVE)
    def __str__(self):
        return self.name_uz
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Unit(models.Model):
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    def __str__(self):
        return "Unit: {}".format(self.name_uz)
    class Meta:
        verbose_name = "O'lchov birligi"
        verbose_name_plural = "O'lchov birliklari"