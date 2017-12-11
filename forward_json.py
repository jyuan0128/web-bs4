
# coding: utf-8

# In[ ]:


#python 2.7

import json
import requests
from elasticsearch import Elasticsearch

# Elasticsearchをインストール済みのサーバのアドレス
server_address = "xxx.xxx.xxx.xxx"
# インストール済みで標準の設定だとポートは9200
port = str(9200)
# Elasticsearchのインスタンスを生成
es = Elasticsearch("%s:%s" % (server_address, port))
# エンドポイント
endpoint = 'https://qiita.com/api/v2/items'
for p in range(1, 11): # 1ページから10ページまで同様に以下の処理を行う
    payload = {'page': p, 'per_page': '100'} #1ページあたり100個のデータを入手
    r =  requests.get(endpoint, params=payload).json() #結果をjson形式で受け取る
    '''
    #参考までに
    print type(r)
    # => <type 'list'>
    print r[0].keys() 
    # => [u'body', u'group', u'rendered_body', u'url', u'created_at', u'tags', u'updated_at', u'private', u'coediting', u'user', u'title', u'id']
    '''
    for it in r: #結果のリスト内をループ
        # 全データをぶち込む！！
        # 今回はindexをqiitaという名前にしてみました
        es.index(index='qiita', doc_type='qiita', id=it['id'], body=it)

