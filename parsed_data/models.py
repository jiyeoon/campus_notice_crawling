from django.db import models
from django.utils import timezone
import requests
from bs4 import BeautifulSoup

# Create your models here.

"""
    크롤링 게시글 하나마다의 모델
    1. 글 제목 = title
    2. 글 내용 = text (html 코드로 불러옴_
    3. 게시한 날짜 = published_date
    4. 글 출처  = source
    5. 원본 링크 = link
    
    게시글마다의 댓글 모델
    1. 유저? -> 그.. 뭐시냐... 익명으로 달 수 있게 할까? (일단 테스트니까)
    2. 원래 원본 글 정보
    3. 댓글 내용
"""

class BlogData(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    published_date = models.CharField(max_length=20, null=True)
    source = models.CharField(max_length=200, null=True)
    link = models.URLField()

    def __str__(self):
        return self.title
