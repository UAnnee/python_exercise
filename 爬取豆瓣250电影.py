'''爬取豆瓣250电影'''
import requests
import csv
from bs4 import BeautifulSoup


def db250_craw(url,sum):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
    #发送请求
    response = requests.get(url, headers = headers)

    #解析html
    soup = BeautifulSoup(response.text, 'html.parser')

    #find_all函数获取所有名为div且class = 'item'的标签. 由于class为python关键字, 故用class_
    movie_items = soup.find_all('div', class_='item')
    i = sum +1
    for item in movie_items:
        #查找名为title的类(标签 .类 #id )并转化为文本
        title = item.select_one('.title').text
        rating = item.select_one('.rating_num').text
        #p是bd类的下一级节点, 加空格
        #split(以换行符\n为界)分割字符串返回列表
        data = item.select_one('.bd p').text.split('\n')
        data1 = data[2].split('/')
        #去除\xa0空格
        time = data1[0].strip(' ').replace(u'\xa0','')
        country = data1[1].replace(u'\xa0','')
        print(str(i)+'.'+title+','+rating+','+country+','+time)
        #写入txt文件
        with open('DB250.txt', 'a') as f:
            f.write(str(i)+'.'+title+','+rating+','+country+','+time+'.\n')
        
        i += 1




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
        