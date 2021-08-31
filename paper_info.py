import json
import requests
from bs4 import BeautifulSoup

def readJson(path):
    file = open(path,"r")
    fileJson = json.load(file)
    result = fileJson['result']
    hits = result["hits"]
    hit = hits['hit']
    return hit


for i in readJson("paper_info.json"):
    #todo：作者，标题已经知道
    info = i['info']
    authors = info['authors']['author']
    name_list = []
    for a in authors:
        name_list.append(a['text'])
    print(name_list)
    title = info['title']

    url = info['ee']
    print(url)
    try:
        kv = {'user-agent': 'Mozilla/5.0'}  # 应对爬虫审查
        r = requests.get(url, headers=kv)
        r.raise_for_status()  # 若返回值不是202，则抛出一个异常
        r.encoding = r.apparent_encoding
    except:
        print("进入网站失败")
    demo = r.text

    soup = BeautifulSoup(demo, "html.parser")
    t = soup.find('time')
    print(t)
    #todo:获取关键字
    keywords = soup.find_all("<span class=\"Keyword\">")
    print(keywords)
    #获取摘要
    # abstract = soup.find(id = 'Par1')
    print('-----------------------------')

