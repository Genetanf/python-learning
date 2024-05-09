
## 網路爬蟲 Web Crawler - 基本篇
# 連線到特定網址，抓取資料
# 解析資料，取得實際想要的部分

# 抓取 PTT 電影版的網頁原始碼 (HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一個 Request 物件，附加 Request Headers 的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")


#解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser")      # 讓 beautifulsoup 幫助我們解析 html 套件

titles=root.find_all("div",class_="title",)     # 尋找 class 為 title 的 div 標籤

# for title in titles:
#     if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除)，印出來
#         print(title.a.string)



## Web Crawler 網路爬蟲 - Cookie
# 抓取 PPT 八卦版的網頁原始碼 (HTML)
import urllib.request as req

def getData(url):
    #建立一個 Request 物件，附加 Request Headers 的資訊
    request=req.Request(url,headers={
        "cookie":"over18=1",        # 通過 cookie 的年齡限制網頁，並抓取資料
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.360"
    })
    with req.urlopen(request)as response:
        data=response.read().decode("utf-8")

    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")

    titles=root.find_all("div",class_="title")

    for title in titles:
        if title.a !=None:
            print(title.a.string)

    # 抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁")     # 找到內文是 < 上頁 的 a 標籤
    return nextLink["href"]

# 主程序：抓取一個頁面的標題
# pageUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
# count=0
# while count<5:
#     pageUrl="https://www.ptt.cc"+getData(pageUrl)   
#     count+=1



## Web Crawler 網路爬蟲 - AJAX
# 抓取 Medium.com 的文章資料
import urllib.request as req
durl="https://consentcdn.cookiebot.com/consentconfig/27519fe0-0eb2-49e6-9942-da471d64320a/settings.json"
#建立一個 Request 物件，附加 Request Headers 的資訊
request=req.Request(durl,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
})
with req.urlopen(request) as respons:
    data=respons.read().decode("utf-8")    # 根據觀察，取得的資料為 JSON 格式


#解析 JSON 格式資料，取得每篇文章的標題f
import json
data=json.loads(data)   # 把原始的解析成字典 / 列表的表示形式


# 取得 JSON 資料中的文章標題
# posts=data["widget"]["position"]
# for key in posts:
#     post=posts[key]
#     print(post)



## 網路爬蟲 Web Crawler - Request Data
# 抓取網站資料，加入 Request Data 的概念
# import urllib.request as req

# # 建立連線網址
# url="https://medium.com/_/graphql"

# # 建立一個 Request 物件，附上 Request Data 和 Request Headers 資訊
# request=req.Request(url,headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# })

# with req.urlopen(request) as response:
#     data=response.read().decode("utf-8")
    
# # 解析 JSON 格式資料
# import json
# result=json.loads(data)
# posts=result["0"]["data"]["webRecommendedFeed"]["items"]
# for key in posts:
#     post=posts[key]
    

