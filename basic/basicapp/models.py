from django.db import models

# Create your models here.

class CharactorModel(models.Model):
    name = models.CharField(verbose_name="名前", max_length=100, default='')
    gender = models.CharField(verbose_name="性別",max_length=50, choices = {('man', '男'), ('woman', '女')}, default="man")
    feature = models.TextField(verbose_name="特徴", default='')
    image_link = models.TextField(verbose_name="画像リンク", default='')
    page_link = models.TextField(verbose_name="ページリンク", default='')

    def __str__(self) -> str:
          return self.name