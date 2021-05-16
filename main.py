#-*- coding:utf-8 -*-
import requests, datetime, os

from bs4 import BeautifulSoup

files = os.listdir("jihuoma/")

def findFile(filename):
    return filename.find('2018.2')


with open("jihuoma/" + list(filter(findFile, files))[0], 'r') as fs:
    res = requests.get("http://idea.medeming.com/jets/")
    res.encoding = 'utf-8'

    soup = BeautifulSoup(res.text,features="html.parser")

    updateText = soup.find_all('div')[1].text
    activeKey = fs.readlines()[0]

    os.mkdir("dist")

    with open('dist/index.html', 'w+', encoding="utf-8") as ws:

        html = """
        <html>
            <head>
                <meta charset="utf-8">
                <title>jets key</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
            </head>
            
            <body>
                <textarea id="key" style="margin: 0px; width: 1102px; height: 526px;">{}</textarea>
                <div id="updateText">{}</div>
                <div>编译时间：{}</div>
            </body>
        </html>
        """

        print(datetime.datetime.now())

        ws.writelines(html.format(activeKey, updateText, datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(hours=8),'%Y-%m-%d %H:%M:%S')))
