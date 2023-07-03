from django.db import models

from api_ikamet.models import Il, Ilce, Mahalle


class Property(models.Model):
    external_id = models.CharField(verbose_name='Внешний id', max_length=10, unique=True)
    name = models.CharField(verbose_name="Заголовок", max_length=1000, null=True, blank=True)
    min_price_in_euro = models.IntegerField(verbose_name="Минимальная стоимость, €")
    max_price_in_euro = models.IntegerField(verbose_name="Максимальная стоимость, €")
    latitude = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Широта WGS 84, градусы")
    longitude = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="Долгота WGS 84, градусы")
    il = models.ForeignKey(Il, on_delete=models.PROTECT, verbose_name='Il')
    ilce = models.ForeignKey(Ilce, on_delete=models.PROTECT, verbose_name='Ilce')
    mahalle = models.ForeignKey(Mahalle, on_delete=models.PROTECT, verbose_name='Mahalle')
    deal_types = models.CharField(verbose_name="Тип сделки", max_length=100)
    min_area_in_sq_meters = models.IntegerField(verbose_name="Минимальная площадь, м²", null=True, blank=True)
    max_area_in_sq_meters = models.IntegerField(verbose_name="Максимальная площадь, м²", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", max_length=2000)
    building_start = models.CharField(verbose_name="Дата начала строительства", max_length=10, null=True, blank=True)
    building_end = models.CharField(verbose_name="Дата окончания строительства", max_length=10, null=True, blank=True)
    blocks_number = models.IntegerField(verbose_name="Количество блоков (корпусов)", null=True, blank=True)
    storeys_number = models.IntegerField(verbose_name="Количество этажей", null=True, blank=True)
    sea_distance = models.IntegerField(verbose_name="Расстояние до моря, м", null=True, blank=True)
    center_distance = models.IntegerField(verbose_name="Расстояние до центра, м", null=True, blank=True)
    airport_distance = models.IntegerField(verbose_name="Расстояние до аэропорта", null=True, blank=True)
    url = models.CharField(verbose_name="URL-ссылка", max_length=1000)
    sold = models.BooleanField(verbose_name="Продано?", default=False)
    partner = models.ForeignKey('Partner', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Партнер', default=1)
    manager = models.ForeignKey('Manager', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Менеджер', default=4)
    property_type = models.ForeignKey('Type', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Тип недвижимости')
    layouts = models.ManyToManyField('Layout', blank=True, null=True, verbose_name='layouts')
    features = models.ManyToManyField('Feature', blank=True, null=True, verbose_name='features')
    priority_number = models.IntegerField(verbose_name='Приоритет', default=0)
    vip = models.BooleanField(verbose_name='Вип', default=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name_plural = "Properties"


class Partner(models.Model):
    name = models.CharField(verbose_name='Наименование партнера', max_length=100)
    url = models.CharField(verbose_name='Сайт партнера', max_length=100, blank=True, null=True)
    image = models.CharField(verbose_name='Логотип', max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name_plural = "Partners"

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(verbose_name='Имя менеджера', max_length=100)
    url_whatsapp = models.CharField(verbose_name='Ссылка на whatsapp', max_length=100)
    url_telegram = models.CharField(verbose_name='Ссылка на telegram', max_length=100, blank=True)
    partner = models.ForeignKey('Partner', on_delete=models.PROTECT, blank=True, verbose_name='Партнер',
                                default=1)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name_plural = "Managers"

    def __str__(self):
        return self.name


class Image(models.Model):
    property_id = models.ForeignKey('Property', on_delete=models.PROTECT, blank=True)
    image_url = models.CharField(verbose_name='URL картинки', max_length=200)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name_plural = "Images"

    def __str__(self):
        return self.image_url


class Type(models.Model):
    name = models.CharField(verbose_name='Тип недвижимости', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(verbose_name='Feature', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name_plural = "Features"

    def __str__(self):
        return self.name


class Layout(models.Model):
    name = models.CharField(verbose_name='Layout', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:
        verbose_name_plural = "Features"

    def __str__(self):
        return self.name