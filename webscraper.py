
# coding: utf-8

# In[1]:

#!/usr/bin/env python


try:
    # Python 3
    from urllib import request
except ImportError:
    # Python 2
    import urllib2 as request

from bs4 import BeautifulSoup


# In[2]:

def main():
    # ブログから Content-Body を取得する
    response = request.urlopen('http://momijiame.tumblr.com')
    body = response.read()

    # HTML をパースする
    soup = BeautifulSoup(body, "lxml")
    
    # 記事タイトルの入った <div> の一覧を取得する ('class' 要素が 'title' のもの)
    title_divs = soup.find_all('div', {'class': 'title'})
    for title_div in title_divs:
        # <div> の中にある <a> を取り出して内容を表示する
        link = title_div.a
        title = link.text
        url = link['href']
        msg = u'{title} <{url}>'.format(title=title, url=url)
        print(msg)

if __name__ == '__main__':
    main()


# In[ ]:



