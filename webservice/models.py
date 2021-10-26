from django.db import models
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    image = models.ImageField(verbose_name="Картинка",  null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('index')


class Comment(models.Model):
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description}'
    
    def get_absolute_url(self):
        return reverse('index')

class Message(models.Model):
    title = models.CharField(max_length=250, verbose_name="Subject",  null=True, blank=True  )
    body= models.TextField(verbose_name="Body")


    def __str__(self):
        return f'{self.title}'
    
    # def get_absolute_url(self):
    #     return reverse('index')
