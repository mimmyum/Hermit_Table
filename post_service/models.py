from django.contrib.auth.models import User
from django.db import models
from .Crawling import crawl_humoruniv_post, crawl_ruliweb_post

class Post(models.Model):
    #게시글 제목 : 크롤링해 온 제목
    #title_humor = crawl_humoruniv_post[0]
    #title_ruli = crawl_ruliweb_post[0]
    #게시글 옆에 어디에서 작성된 글인지 표시
    #body_humor = crawl_humoruniv_post[1]
    #게시글 앞에는 이미지가 있을경우의 썸네일 표시

    #하단부에 페이지 표
    title_humor = 0