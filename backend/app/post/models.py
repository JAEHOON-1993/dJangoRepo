from django.db import models

from app.base.models import BaseModel


class Post(models.Model):
    user = models.ForeignKey('user.User', verbose_name="사용자", on_delete=models.CASCADE)
    title = models.CharField(verbose_name='제목', max_length=64, null=False, blank=True) #널은 허용하지 않지만 블랭크는 허용 이건 기본값이기도 함 default="??"
    content = models.TextField(verbose_name="본문")
    created = models.DateTimeField(verbose_name="생성일", auto_now_add=True) #auto_now_add=True 생성시간을 자동으로 넣어줌. 생성 됬을 때만 첫 입력됨.
    updated = models.DateTimeField(verbose_name="수정일", auto_now=True)  #auto_now=True 저장을 할 때마다 바뀜.

    class Meta:
        verbose_name ="게시글"
        verbose_name_plural = "게시글들"

    def __str__(self):
        return self.title # 보기 편하게 하기 위함. 포스트 출력 시, 타이틀로 나오게 됨. (어드민이나 쉘 등에서)