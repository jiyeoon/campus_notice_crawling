#parser.py

import time
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webcrawling.settings")

import django
django.setup()

from parsed_data.models import BlogData
from collections import namedtuple

CrawlingData = namedtuple("CrawlingData", "title link source published_date")


#메인 공지 크롤링 하는 함수
def parse_blog():
    base_link = 'https://www.yonsei.ac.kr/wj/support/notice.jsp'
    req = requests.get(base_link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select('ul.board_list > li > a')
    data = [] #리스트 형태로 내용 받아옴

    for i in range(len(my_titles)):
        if (my_titles[i].text == '첨부파일'): #첨부파일은 빼버림
            continue

        cd_title = my_titles[i].select('strong')[0].text
        cd_title = cd_title.strip().replace('\t', '').replace('\r', '').replace('\n', '')
        cd_title = " ".join(cd_title.split())
        cd_source = my_titles[i].select('span.tline')[0].text
        cd_published = my_titles[i].select('span.tline')[1].text
        cd_link = base_link + my_titles[i].get('href')
        cd = CrawlingData(cd_title, cd_link, cd_source, cd_published)
        data.append(cd)
    return data


if __name__ == '__main__':
    while(True):
        blog_data = parse_blog()

        for one_data in blog_data:
            req = requests.get(one_data.link)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.select('div.cont_area')
            text1 = text[0]
            print("title :" + one_data.title)
            print("link : " + one_data.link)
            print(str(text1))
            BlogData(title=one_data.title, link=one_data.link, published_date=one_data.published_date, source=one_data.source, text=str(text1)).save() #왜 갑자기 안되냐~~
        time.sleep(12000)


"""
def parse_blog():
    base_link = 'https://www.yonsei.ac.kr/wj/support/notice.jsp'
    req = requests.get(base_link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select('ul.board_list > li > a')
    data = {}  #딕셔너리 key => title, link, source, published_date

    for title in my_titles:
        data[title.text] = title.get('href')
    return data

if __name__=='__main__':
    blog_data_dic = parse_blog()
    for t, l in blog_data_dic.items():
        BlogData(title=t, link=l).save()
        
        오케이 제대로 받는다!!!!
        
"""