
# coding: utf-8

# In[1]:

#!/usr/bin/env python


import time

try:
    # Python 3
    from urllib import request
except ImportError:
    # Python 2
    import urllib2 as request

from bs4 import BeautifulSoup


def main():
    baseurl = 'http://momijiame.tumblr.com'
    path = '/'

    while True:
        # 各ページの処理を始めた時間
        start_time = time.time()

        url = '{baseurl}{path}'.format(baseurl=baseurl, path=path)
        # Content-Body を取得する
        response = request.urlopen(url)
        body = response.read()

        # HTML をパースする
        soup = BeautifulSoup(body)

        # ページネーションのリンクが入った <li> を取得する
        next_page = soup.find('li', {'class': 'next'})
        next_page_link = next_page.a

        if 'href' not in next_page_link.attrs:
            # 次のページが見つからなかったので終了
            break

        # 取得したリンクを表示する
        path = next_page_link['href']
        print(path)

        # 各ページの取得には最低でも 1 秒間のディレイをはさむ
        end_time = time.time()
        sleep_time = 1 - (end_time - start_time)
        if sleep_time > 0:
            time.sleep(1)

if __name__ == '__main__':
    main()


# In[ ]:



