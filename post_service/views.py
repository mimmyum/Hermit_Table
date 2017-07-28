from django.http.response import HttpResponse
from django.template.loader import get_template

#from post_service.Crawling import crawling_humoruniv, crawling_ruliweb, crawling_freesound
import requests
from bs4 import BeautifulSoup
import os


def crawling_humoruniv(sitename, num,crawl_humoruniv_post,crawl_board):
    crawl_humoruniv_post.append(('1','A'))
    if num == 0 :
        crawl_humoruniv_post.clear()
    global crawl_num
    now_site = sitename
    if num != 0 :
        now_site += "&pg="+str(num)

    #
    crawl_humoruniv_post.append((now_site,now_site))
    #

    now_req = requests.get(now_site)
    now_content = now_req.content

    #
    crawl_humoruniv_post.append((now_req,now_req))
    #

    now_soup = BeautifulSoup(now_content,"html.parser")
    now_result = now_soup.find_all('a',{'class':"li"})

    splitted=[]

    for sub_sites in now_result:
        now_line = str(crawl_board[0])+str(sub_sites.get('href'))
        splitted = str(sub_sites).split('>')
        post_title = splitted[1].split('<')[0]
        post_title = post_title.strip("\t")
        post_title = post_title.strip("\n")
        post_title = post_title.strip("\r")
        post_title = post_title.strip("(웃긴자료) ")

        crawl_humoruniv_post.append(('2','B'))

        if now_line.find('day&page') == -1:

            crawl_humoruniv_post.append((post_title, now_line))

            crawl_humoruniv_post.append(('3','C'))
        else :
            continue
    if num == 0 :
        for page in range(1,9):
            crawling_humoruniv(sitename,page,crawl_humoruniv_post,crawl_board)


def crawling_ruliweb(ruli_board,num,crawl_ruliweb_post) :

    if num == 0 :
        crawl_ruliweb_post.clear()

    now_site = ruli_board
    if num != 0 :
        now_site += "?&page=" + str(num)

    now_req = requests.get(now_site)
    now_content = now_req.content
    now_soup = BeautifulSoup(now_content,"html.parser")
    now_result = now_soup.find_all('td',{'class': "subject"})

    splitted = []
    for sub_sites in now_result :
        now_line = sub_sites.find('a')['href']
        #splitted = str(sub_sites).split('>')
        #post_title = splitted[1].split('<')[0]
        post_title1 = sub_sites.text
        post_title = post_title1[1:-6]

        crawl_ruliweb_post.append((post_title,now_line))

    if num == 0 :
        for page in range(1,5):
            crawling_ruliweb(ruli_board,page,crawl_ruliweb_post)


#only for test
def crawling_freesound(free_board,num,crawl_freesound_post) :

    if num == 0 :
        crawl_freesound_post.clear()

    now_site = free_board

    now_req = requests.get(now_site)
    now_content = now_req.content
    now_soup = BeautifulSoup(now_content,"html.parser")
    now_result = now_soup.find_all('div',{'class': "sound_filename"})

    splitted = []
    for sub_sites in now_result :
        now_line = str(free_board)+ str(sub_sites.find('a')['href'])
        #splitted = str(sub_sites).split('>')
        #post_title = splitted[1].split('<')[0]
        post_title = sub_sites.find('a')['title']

        crawl_freesound_post.append((post_title,now_line))

#only for test


def post_list(request):
    template = get_template('post_list.html')

    crawl_site = []
    crawl_board = []
    crawl_humoruniv_post = list()
    crawl_ruliweb_post = []

    #only for test
    crawl_freesound_post=[]

    crawl_site.append('http://web.humoruniv.com/board/humor/list.html?table=pds')
    crawl_site.append('http://bbs.ruliweb.com/best')
    crawl_board.append('http://web.humoruniv.com/board/humor/')
    crawl_num = 0

    crawling_humoruniv(crawl_site[crawl_num], 0,crawl_humoruniv_post,crawl_board)
    crawling_ruliweb(crawl_site[1], 0,crawl_ruliweb_post)

    #only for test
    crawl_site.append('http://freesound.org/browse/')
    crawling_freesound(crawl_site[2],0,crawl_freesound_post)
    #only for test
    crawl_freesound_post.append(('1','A'))
    crawl_freesound_post.append(('2', 'B'))
    crawl_freesound_post.append(('3', 'C'))

    ctx = {'post_list_humor' : crawl_humoruniv_post, 'post_list_ruli' : crawl_ruliweb_post, 'post_list_free':crawl_freesound_post}
    return HttpResponse(template.render(ctx))