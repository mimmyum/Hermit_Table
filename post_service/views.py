from django.http.response import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from post_service.static.Crawling import crawling_humoruniv, crawling_ruliweb


def post_list(request):
    template = get_template('post_list.html')

    crawl_site = []
    crawl_board = []
    crawl_humoruniv_post = []
    crawl_ruliweb_post = []

    crawl_site.append('http://web.humoruniv.com/board/humor/list.html?table=pds')
    crawl_site.append('http://bbs.ruliweb.com/best')
    crawl_board.append('http://web.humoruniv.com/board/humor/')
    crawl_num = 0

    crawl_humoruniv_post = crawling_humoruniv(crawl_site[crawl_num], 0)
    crawl_ruliweb_post = crawling_ruliweb(crawl_site[1], 0)

    ctx = {'post_list_humor' : crawl_humoruniv_post, 'post_list_ruli' : crawl_ruliweb_post}
    return HttpResponse(template.render(ctx))