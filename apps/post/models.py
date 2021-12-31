from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50, null=False)
    header = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=False, unique=True)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return f"{self.name}"
