# coding:utf-8

import requests


def crawl(url):
    # text = requests.get(url).text.encode('utf-8').decode('utf-8')
    text = requests.get(url).text.encode('utf-8').decode('utf-8')
    with open('/Users/yibwu/Desktop/test1.html', 'w') as f:
        f.write(text)

if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    crawl(url)