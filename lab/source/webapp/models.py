from django.db import models
STATUS = [("active", "Активно"),
          ("blocked", "Заблокировано")]




class Book(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='имя')
    email = models.EmailField(max_length=40, null=False, blank=False, verbose_name='email')
    text = models. TextField(max_length=300, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    edit_time = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=20, verbose_name='Тема', default=STATUS[0][0], choices=STATUS)

    def __str__(self):
        return self.name
