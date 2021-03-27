from django.db import models

class Review(models.Model):
    user = models.ForeignKey('client.User', on_delete=models.RESTRICT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'

class Category(models.Model):
    parent = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True, default=None)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

class Unit(models.Model):
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    class Meta:
        verbose_name = "O'lchov birligi"
        verbose_name_plural = "O'lchov birliklari"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    availability_unit = models.ForeignKey(Unit, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    content_uz = models.TextField()
    content_ru = models.TextField()
    anons_uz = models.CharField(max_length=50)
    anons_ru = models.CharField(max_length=50)
    price = models.BigIntegerField
    discount_percent = models.SmallIntegerField(default=0)
    discount_start = models.DateTimeField(default=None, null=True)
    discount_end = models.DateTimeField(default=None, null=True)
    availability = models.ImageField(default=0)
    vendor_code = models.CharField(max_length=15)
    photo0 = models.ImageField()
    photo1 = models.ImageField()
    photo2 = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

class ProductView(models.Model):
    user = models.ForeignKey('client.User', on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    star = models.SmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mahsulot izohi'
        verbose_name_plural = 'Mahsulot izohlari'


class PromoCode(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    availability = models.ImageField(default=0)
    used = models.ImageField(default=0)
    discount = models.SmallIntegerField(default=10)

    class Meta:
        verbose_name = 'Promo kod'
        verbose_name_plural = 'Promo kodlar'

class Setting(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    value = models.TextField()

    class Meta:
        verbose_name = 'Sozlash'
        verbose_name_plural = 'Sozlanmalar'

class Post(models.Model):
    subject_uz = models.CharField(max_length=100)
    subject_ru = models.CharField(max_length=100)
    content_uz = models.TextField()
    content_ru = models.TextField()
    photo = models.ImageField()
    status = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

class PostComment(models.Model):
    parent = models.ForeignKey('PostComment', on_delete=models.RESTRICT, null=True, default=None)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Maqola izohi'
        verbose_name_plural = 'Maqola izohlari'
