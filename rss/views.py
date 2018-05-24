from django.shortcuts import render, render_to_response
from django.views.generic.list import ListView

from .fetch_rss import (get_data_from_rss, get_rss_himalayan, rss)
from .models import *
import feedparser
from newspaper import Article
import datetime

def index(request):
        # pastlink = HimalayanTimes.objects.values_list('link')
        # links = list(pastlink)
    url_link = "http://fetchrss.com/rss/5af180de8a93f8d81f8b4567726347788.xml"
    rss = feedparser.parse(url_link)
        
    date = post.published[4:16]
    article = Article(link)
    article.download()
    article.parse()

    news_body = article.text
    news_body = news_body.replace("\n\n", " ")
    content = news_body
    news = HimalayanTimes(source = 'Himalayan Times', date = date, link = link, title = title, content= content,)
    news.save()

    # pastlink = HimalayanTimes.objects.values_list('link')
    # links = list(pastlink)
    # print(links)
    # get_rss_himalayan()
    #
    url_link = "http://fetchrss.com/rss/5af180de8a93f8d81f8b4567402110544.xml"

    rss = feedparser.parse(url_link)
    for post in rss.entries:
        title = post.title
        link = post.link
        date = post.published[4:16]
        article = Article(link)
        article.download()
        article.parse()

        news_body = article.text
        news_body = news_body.replace("\n\n", " ")
        content = news_body
        # if link in pastlink:
        #     continue
        news = HimalayanTimes(source = 'Kathmandu Post', date = date, link = link, title = title, content= content,)
        news.save()

    context = {
        'link':pastlink,
    }
    return render(request,'index.html',context)
