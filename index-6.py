# ## 寄送 Email 的程式
# # 準備訊息物件設定
# import email.message
# msg=email.message.EmailMessage()
# msg["From"]="gtmial9987@gmail.com"  # 寄件人
# msg["TO"]="gtmial9987@gmail.com"  # 收件人
# msg["Subject"]="Hello"

# # 寄送純文字內容
# msg.set_content("測試看看")

# # 寄送比較多樣式的內容(HTML)
# msg.add_alternative("<h3>優惠券</h3>滿五百送一百喔",subtype="html")

# # 連線到 SMTP Server ，見證寄件人身分
# import smtplib
# # 到網路上搜尋 gmail smtp server 或是 yahoo smtp server
# server=smtplib.SMTP_SSL("smtp.gmail.com",465)
# server.login("gtmial9987@gmail.com","fuzu dbfu filb xibi")
# server.send_message(msg)
# server.close()



## 可疊代資料型態
# Iterable 資料型態
# 字串、列表、集合、字典

# for 迴圈
# for 變數名稱 in 可疊代的資料
# dic= {"a":3,"b":4}
# for x in dic:
#     print(x)
#     print(dic[x])

# 內建函式
# max(可疊代資料)
# result=max([10,2,30,52])
# print(result)
# result=max("xuz")
# print(result)
# result=max({10,500,30,1})
# print(result)
# result=max({"x":3,"z":5})
# print(result)

# sorted(可疊代資料)
# result=sorted("cba")
# print(result)

# result=sorted({10,2,200,-5})
# print(result)



## 生成器 Generator

# 定義生成器函式
# def test():
#     print("step1")
#     yield 5
#     print("step2")
#     yield 10

# 呼叫並回傳生成器
# gen=test()

# 搭配 for 迴圈中使用
# for data in gen:
#     print(data)    # 印出5

# def generatorEven(maxnumber):
#     number=0
#     # while True:     # 無限生成偶數
#     #     yield number
#     #     number+=2
    
#     while number<=maxnumber:
#         yield number
#         number+=2

# evenGenerator=generatorEven(10)
# for data in evenGenerator:
#     print(data)



## 回呼函式 Callback Function
# def test(arg):
#     arg("Hello")   # 呼叫回呼函式

# # 回呼函式
# def handle(data):
#     print(data)

# test(handle)

# sample 2
# def add(n1,n2,cb):
#     cb(n1+n2)

# def handlle1(result):
#     print("結果是: ", result)

# add(3,4,handlle1)
# add(5,6,handlle1)



## 裝飾器 Decorator
# 定義裝飾器
# def testDecorator(callback):
#     def innerfunction():
#         print("裝飾器中的程式碼")
#         callback("callback data")   # 這個回呼函式，其實就是被裝飾的普通函式   
#     return innerfunction

# 使用裝飾器
# @testDecorator
# def decoratedFunction(data):
#     print("普通函式程式碼",data)

# decoratedFunction()

# sample 2 
# 定義一個裝飾器，計算1+2+...+50 的總和
# def calculate(callback):
#     def run():
#         result=0
#         for n in range(51):
#             result+=n
#         # 把計算結果透過參數傳到被裝飾的普通函式中
#         callback(result)
#     return run

# @calculate
# def show(data):
#     print("結果為:",data)

# @calculate
# def showEnglish(data):
#     print("Result is:",data)

# show()
# showEnglish()



## 裝飾器工廠 - Decorator Factory
# def myFactory(base):
#     def myDeo(cb):
#         def run():
#             result=base*3
#             cb(result)    
#         return run
#     return myDeo

# @myFactory(3)
# def test(numbers):
#     print("普通函式程式",numbers)

# test()

# sample-2 計算 1+2+3+...+50 的裝飾器

# def addDecorator(data):
#     def mydecorator(callback):
#         def run():
#             total=0
#             for n in range(data):
#                 total+=n
#             callback(total)
#         return run
#     return mydecorator

# @addDecorator(51)
# def function(result):
#     print("總和為:", result)
# function()

# @addDecorator(101)
# def function(result):
#     print("總和為:", result)
# function()



## 錯誤、例外處理 - Syntax Error / Exception Handling
# 例外處理情境: 轉換資料型態失敗
# data=input("請輸入一個數字:")
# try:
#     number=int(data)
# except Exception:
#     number=0
# number=number*2
# print(number)

# sample-2-使用者如果輸入的資料格式不能轉換成數字，請他重新輸入，直到成功為止
# while True:
#     data=input("請輸入一個數字:")
#     try:
#         number=int(data)
#         break
#     except Exception:
#         print("輸入格式錯誤，請重新輸入:")

# number=number*2
# print(number)



# 快速開始、網頁截圖 - Selenium 
#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.binary_location = "D:\\Learning\\python\\chromedriver.exe"

# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome()
driver.maximize_window()    # 視窗最大化
driver.get("https://www.google.com/")
driver.save_screenshot("screenshot-Google.png")     # 做螢幕截圖
driver.close()