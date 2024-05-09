## 文字檔案的讀取和儲存
# 儲存檔案
# 基本運用
# file=open("data.txt",mode="w",encoding="utf-8")
# file.write("Hello File \n Second Line")
# file.write("測試中文")
# file.close()    #關閉

# 最佳實務
# with open("data.txt",mode="w",encoding="utf-8")as file:
#     file.write("5\n3")

# 讀取檔案
# with open("data.txt",mode="r",encoding="utf-8")as file:
#     data=file.read()
#     print(data)

# 讀取檔案，並將檔案中的數字資料讀取出來總和
# sum=0
# with open("data.txt",mode="r",encoding="utf-8")as file:
#     for numbers in file:    #一行一行讀取
#         sum=sum+int(numbers)
# print(sum)

# 使用 JSON 格式讀取、複寫檔案
import json
with open("config.json",mode="r") as file:
    data=json.load(file)

print(data)     # data 是一個字典資料   
print("name: ",data["name"])
print("version:", data["version"])

data["name"]="Jason"    #修改變數中的資料

#把最新資料複寫回檔案中
with open("config.json",mode="w")as file:
    json.dump(data,file)




## 亂術與統計模組
import random
# 隨機模組
data=random.choice([5,25,66,95])        #隨機選取一個資料
data2=random.sample([11,55,69,54,23,15],2)       #隨機選取負數資料
print(data)
print(data2)

data3=[1,5,8,20]
random.shuffle(data3)       #洗牌的概念
print(data3)

data4=random.random()       # 0 ~ 1 之間的隨機亂數
data5=random.uniform(60,100)       # 60 ~ 100 之間的隨機亂數
print(data4)
print(data5)

data6=random.normalvariate(100,10)      # 取得常態分配亂數 ─ 平均數100、標準差10
print(data6)

# 統計模組
import statistics as stat
data7=stat.mean([1,5,8,9])      #取得平均數
data8=stat.median([1,5,9,10])       #取得中位數
print(data7)
print(data8)

data8=stat.stdev([1,2,3,4,5,8,10,55])       #取得標準差
print(data8)



## 網路連線程式、公開資料串接
# 網路連線
# import urllib.request as quest
# src="https://tw.stock.yahoo.com/quote/2486.TW"
# with quest.urlopen(src)as response:
#     data=response.read().decode("utf-8")        #取得網站原始碼
# print(data)

# 串接、擷取公開資料
import urllib.request as quest
import json
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with quest.urlopen(src)as response:
    data=json.load(response)        # 利用 json 模組處理 json 資料格式


# 將公司名稱列表出來
clist=data["result"]["results"]
with open("company-data.txt",mode="w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")



## 類別的定義與使用
# 定義類別、與類別屬性 (封裝在類別中的變數和函式)
# 定義一個類別 IO ，有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from",src)
    
# 使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("Internet")



## 實體物件的建立與使用 - 上 - 實體屬性
# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

# 建立第一個實體物件
p1=Point(3,4)
print(p1.x,p1.y)

# 建立第二個實體物件
p2=Point(5,6)
print(p2.x,p2.y)


# FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class FullName:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

name1=FullName("Gene","Tang")
print(name1.firstName,name1.lastName)
name2=FullName("Allan","Kuo")
print(name2.firstName,name2.lastName)



## 實體物件的建立與使用 - 下 - 實體方法 (封裝在實體物件中的函式)
# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # 定義實體方法
    def show(self):
        print(self.x,self.y)

    def distance(self,targetX,targetY):
        return(((self.x-targetX)**2+(self.y-targetY)**2)**0.5)
    

p=Point(3,4)
p.show()        #呼叫實體方法

result=p.distance(0,0)      # 計算座標 (0,0) 和座標 (3,4) 之間的距離
print(result)


# File 實體物件的設計: 包裝檔案讀取的程式
class File:
    def __init__(self,name):
        self.name=name
        self.file=None  # 尚未開啟檔案: 初期是 None
    
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    
    def read(self):
        return self.file.read()

# 讀取第一個檔案
f1=File("file1.txt")
f1.open()
data=f1.read()
print(data)
# 讀取第二個檔案
f2=File("file2.txt")
f2.open()
data2=f2.read()
print(data2)


