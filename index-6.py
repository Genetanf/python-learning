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
def calculate(callback):
    def run():
        result=0
        for n in range(51):
            result+=n
        # 把計算結果透過參數傳到被裝飾的普通函式中
        callback(result)
    return run

@calculate
def show(data):
    print("結果為:",data)

@calculate
def showEnglish(data):
    print("Result is:",data)

show()
showEnglish()