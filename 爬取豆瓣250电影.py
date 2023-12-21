'''爬取豆瓣250电影'''
import requests
import csv
from bs4 import BeautifulSoup


def db250_craw(url,sum):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
    #请求对象的定制
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_items = soup.find_all('div', class_="item")
    i = sum +1
    for item in movie_items:
        title = item.select_one('.title').text
        rating = item.select_one('.rating_num').text
        data = item.select('.db p')[0].text.split('\n')
        time = data[2].replace(' ','').split('/')[0]
        country = data[2].replace(' ','').split('/')[1]
        print(str(i)+'.'+title+','+rating+','+country+','+time)#
        i += 1
        '''     
        '''



url_base = 'https://movie.douban.com/top250'
sum = 0 
for a in range(0,10):
    if sum == 0:
        db250_craw(url_base, sum)
        sum += 25
    else:
        url = url_base+ '?start=' + str(sum) + '&filter='
        db250_craw(url, sum)
        sum += 25
        