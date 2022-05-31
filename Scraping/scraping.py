# ライブラリのインポート
import requests
from bs4 import BeautifulSoup

# htmlの情報を収集
url = "https://app-mooovi2021.herokuapp.com/works/initial_scraping"
html= requests.get(url)

# textをlxmlで解析し、プログラミングで使えるように。また、pタグの取得
soup=BeautifulSoup(html.text,'lxml')
elements=soup.find_all('p')

# pタグのテキスト部分のみをfor文を使って表示させる
for element in elements:
    print(element.get_text())