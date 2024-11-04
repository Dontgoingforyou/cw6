from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blogs/img/', verbose_name='Изображение')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = "Запись в блоге"
        verbose_name_plural = "Записи в блоге"

    def __str__(self):
        return self.title

