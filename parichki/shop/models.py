from django.db import models

# таблица БД

class Category(models.Model):
    name = models.CharField('Категория парика', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField('Название парика', max_length=100, db_index=True)
    image = models.ImageField(default='no_image.jpg', upload_to='', blank=True)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = ('id',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name



#'http://localhost/parichki/media/parichki/images/1.jpg'


