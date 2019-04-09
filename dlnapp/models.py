from django.db import models
# Сдлетаь две модельки. Одна логотипы, другая отзывы
# Ещё одна модель это для загрузки картинок. Три поля
# created_at updated_ad img 28 минута
# ещё одно поле is_active чтобы показывать и скрывать отдельные картинки
# Create your models here.
class UploadImages(models.Model):
    name = models.TextField()
    img = models.ImageField(upload_to='media/', blank=True)

    def __int__(self):
        return self.id
