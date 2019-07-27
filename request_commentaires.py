import jieba
import requests
import pandas as pd
import time

import random
from lxml import etree

def get_comments(eachComment):
    commentlist = []
    #user = eachComment.xpath("./h3/span[@class='comment-info']/a/text()")[0]  # 用户
    #watched = eachComment.xpath("./h3/span[@class='comment-info']/span[1]/text()")[0]  # 是否看过
    #rating = eachComment.xpath("./h3/span[@class='comment-info']/span[2]/@title")  # 五星评分
    #if len(rating) > 0:
        #rating = rating[0]

    #comment_time = eachComment.xpath("./h3/span[@class='comment-info']/span[3]/@title")  # 评论时间
    #if len(comment_time) > 0:
        #comment_time = comment_time[0]
    #else:
        # 有些评论是没有五星评分, 需赋空值
        #comment_time = rating
        #rating = ''

    #votes = eachComment.xpath("./h3/span[@class='comment-vote']/span/text()")[0]  # "有用"数
    content = eachComment.xpath("./p[@class='comment-content']/span/text()")[0]  # 评论内容

    #commentlist.append(user)
    #commentlist.append(watched)
    #commentlist.append(rating)
    #commentlist.append(comment_time)
    #commentlist.append(votes)
    commentlist.append(content.strip())
    # print(list)
    return commentlist

file = open("corpuscommentaires.txt","a")

htmlbase="https://book.douban.com/subject/10763902/comments/hot?p="
for i in range(102,1255):
    url=htmlbase+str(i)
    html=requests.get(url)
    if html.status_code == 200:
        print("html.status_code == 200")
        selector = etree.HTML(html.text)
        comments=selector.xpath("//div[@class='comment']")
        
        for each in comments:
            for k in get_comments(each):
                file.write(k)
                file.write("\n") # Pas un très bon séparateur, car il y a des commentaires avec retour à la ligne, ils seront coupés ainsi. C'est mieux%%%%%%%% car ensuite on va appliquer text.split(); mais bon, il n'y a pas baucoup.
            #file.write([k for k in get_comments(each)])
        print("done",i)

file.close()


"""
def start_spider():
    base_url = 'https://movie.douban.com/subject/24773958/comments'
    start_url = base_url + '?start=0' 

    number = 1
    html = request.get(start_url) 

    while html.status_code == 200:
        # 获取下一页的 url
        selector = etree.HTML(html.text)
        nextpage = selector.xpath("//div[@id='paginator']/a[@class='next']/@href")
        nextpage = nextpage[0]
        next_url = base_url + nextpage
        # 获取评论
        comments = selector.xpath("//div[@class='comment']")
        marvelthree = []
        for each in comments:
            marvelthree.append(get_comments(each))

        data = pd.DataFrame(marvelthree)
        # 写入csv文件,'a+'是追加模式
        try:
            if number == 1:
                csv_headers = ['用户', '是否看过', '五星评分', '评论时间', '有用数', '评论内容']
                data.to_csv('./Marvel3_yingpping.csv', header=csv_headers, index=False, mode='a+', encoding='utf-8')
            else:
                data.to_csv('./Marvel3_yingpping.csv', header=False, index=False, mode='a+', encoding='utf-8')
        except UnicodeEncodeError:
            print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

        data = []

        html = request_get(next_url)

"""
