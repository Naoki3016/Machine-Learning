import json
import requests
import time
from bs4 import BeautifulSoup

# 最初の処理と、共通の処理を定義しておく
next_url=''
top_url = 'http://review-movie2021.herokuapp.com/'
movie_titles=[]
movie_images=[]

while True:
    # プログラム適用処理
    url=top_url+next_url
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'lxml')
    
    next_link=soup.find('span',class_='next')
    
        
    titles = soup.find_all('h2')
    img_urls = []
        # タイトルを配列に追加し、、画像のUrlをaタグのhrefから読み取り、それをimg_urlsへと格納していく
    for title in titles:
        movie_title=title.get_text()
        movie_titles.append(movie_title.replace('\u3000','').strip('\n'))
        for a in title.find_all('a'):
            img_urls.append(a.get('href'))
    # 画像を配列に追加していく
    for img_url in img_urls:
        # 先ほど読み取った画像のhref要素とホーム画面のurlを組み合わせて作品別のurlを作成。それをプログラムできるようにする
        img_link = top_url+img_url
        img_html = requests.get(img_link)
        imgs = BeautifulSoup(img_html.text,'lxml')
        # 作品別の紹介ページから、img要素を、そしてhrefを指定してmovie_imagesへ格納していく
        movie_url = imgs.find('img',class_= 'alignleft')
        movie_images.append(movie_url.get('src'))
    # ページ遷移の際に２秒間休憩。サーバーの負荷を減らすため                        
    time.sleep(2)   
    if next_link != None:
        next_url = next_link.a.get('href')             
    else:
        break

json_data = {}
for n,(title,image) in enumerate(zip(movie_titles,movie_images)):
    json_data[n]=[title,image]
with open('movie.json', 'w', newline = '', encoding = 'utf-8')as f:
    json.dump(json_data, f, ensure_ascii=False)