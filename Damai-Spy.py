# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
url = 'https://search.damai.cn/search.html'

def damai(url, currPage=0):
        datas = {
                'ctl':'演唱会',
                'currPage':currPage,
                'order':'1'
                }
        wb_data = requests.post(url,datas)
        soup = BeautifulSoup(wb_data.text, 'html.parser')
        i = 0

        while True:
                try:
                        event = soup.select("#content_list  li  div.search_txt  h3 a")[i].text
                        time = soup.select("#content_list  li div.search_txt  p.search_txt_time.c3")[i].text
                        city = soup.select("#content_list  li div.search_txt  p.c1")[i].text
                        prices = soup.select("#content_list  li  div.search_txt  p.search_txt_piao")[i].text
                        print event, time, city, prices
                        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                        i+=1
                except Exception, e:
                        return

while True:
        j = 1
        while True:
                a = damai(url, j)
                j+=1
                time.sleep(2)
                if a != []:
                        break