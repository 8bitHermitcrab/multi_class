from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    title = models.CharField("제목", max_length=255)
    contents = models.TextField("내용")
    # 정수 : models.IntegerField
    # 실수 : models.DecimalField

# Board의 댓글 기능 구현
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    contents = models.CharField("댓글", max_length=255, null=False)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="comment_list")
    user_like = models.ManyToManyField(User, related_name="like_comments")


# Board와 Comment의 관계는? (1:N vs N:N)
# 1:N 관계, Foreign Key는 N쪽에.

# User가 Comment에 '좋아요' 버튼 기능
# N:N