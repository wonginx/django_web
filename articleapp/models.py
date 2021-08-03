from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null = True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True) #DB에 저장되는 순간에 시간을 찍어줌
    # models 수정 후엔 마이그레이트 진행

