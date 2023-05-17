import requests
from bs4 import BeautifulSoup
import htmlmin

while True:
    # URLの入力を求める
    url = input("アソシエイトURLを入力してください: ")

    # User-Agentを指定することでブラウザからのアクセスとみなす
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # 商品ページのHTMLを取得
    response = requests.get(url, headers=headers)
    html = response.text

    # BeautifulSoupを使ってHTMLを解析
    soup = BeautifulSoup(html, "html.parser")

    # 商品の画像URLを取得
    image_element = soup.find("img", {"id": "landingImage"})
    image_url = image_element["src"]
    

    # 商品の価格を取得
    price_element = soup.find("span", {"class": "a-offscreen"})
    price = price_element.text
    

    # HTMLコードを生成
    html_code = f"""
    <style>.product-container{{display:flex;align-items:center;justify-content:center;flex-direction:column;max-width:200px;margin:0 auto;padding:20px;border:1px solid #ccc;border-radius:5px;}}.product-image{{max-width:50%;height:auto;margin-bottom:10px;}}.product-price{{font-weight:bold;margin-bottom:10px;}}.product-button{{background-color:#ff9900;padding:10px 20px;color:white;text-decoration:none;border-radius:5px;}}</style><div class="product-container"><img src="{image_url}" alt="商品画像" class="product-image"><p class="product-price">商品の値段: {price}</p><a href="{url}" class="product-button">Amazon</a></div>
    """

    # HTMLコードをminifyして一行で出力
    minified_html = htmlmin.minify(html_code, remove_comments=True, remove_empty_space=True)
    print("HTMLコード:")
    print("--------------------------------------------------------------------------------")
    print(minified_html)
    print("--------------------------------------------------------------------------------")
    # ユーザーに再度実行するかどうかを尋ねる
    answer = input("他のアフィリエイト用コードを作成しますか？ (y/n): ")
    if answer.lower() != "y":
        break
