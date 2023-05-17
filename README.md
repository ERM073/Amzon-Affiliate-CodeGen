# Amzon-Affiliate-CodeGen
AmazonアソシエイトURLを一瞬で、WordPressにも対応のHTMLに変換します。画像と値段とリンクボタン

対応しているURL形式

https://amzn.to/42AXYul

https://www.amazon.co.jp/dp/B00TMYO5LK?th=1&linkCode=ll1&tag=anon05-22&linkId=51c59b5a7215b82925dd7d8b143f5563&language=ja_JP&ref_=as_li_ss_tl

等の短縮URLや通常URLにも対応しています。

生成されるHTMLコードの例

 ```
 <style>.product-container{display:flex;align-items:center;justify-content:center;flex-direction:column;max-width:200px;margin:0 auto;padding:20px;border:1px solid #ccc;border-radius:5px;}.product-image{max-width:50%;height:auto;margin-bottom:10px;}.product-price{font-weight:bold;margin-bottom:10px;}.product-button{background-color:#ff9900;padding:10px 20px;color:white;text-decoration:none;border-radius:5px;}</style><div class=product-container><img src=https://m.media-amazon.com/images/I/51KbFr5AACL.__AC_SY300_SX300_QL70_ML2_.jpg alt=商品画像 class=product-image><p class=product-price>商品の値段: ￥640</p><a href=https://amzn.to/3BuXyKd class=product-button>Amazon</a></div>
 ```
 
 表示結果
 
 ![Image](https://raw.githubusercontent.com/ERM073/Amzon-Affiliate-CodeGen/main/2023-05-17_22h45_07.png)
 
 
 # 使用方法
 
 Windowsの場合は、以下からexeファイルをダウンロードしてダブルクリックして起動完了
 
 https://github.com/ERM073/Amzon-Affiliate-CodeGen/releases/download/release/amazon.exe
 
 Linux及びその他OS
 ```
 git clone https://github.com/ERM073/Amzon-Affiliate-CodeGen
 cd Amzon-Affiliate-CodeGen
 
 pip install requests
 pip install BeautifulSoup
 pip install htmlmin
 
 python amazon.py
 ```
