from bs4 import BeautifulSoup
import requests

url = 'https://search.damai.cn/search.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select('div.search_txt > h3 > a')
# 标题
describes = soup.select('div.search_txt > p.search_txt_cut c3')
# 描述
times = soup.select('div.search_txt > p.search_txt_time c3')
# 演出时间
prices = soup.select('div.search_txt > p.search_txt_piao > em')
# 价格
print(titles, describes, times, prices)
