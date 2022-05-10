from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField("제목", max_length=255)
    contents = models.TextField("내용")


    # 정수 : models.IntegerField
    # 실수 : models.DecimalField