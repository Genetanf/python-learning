# 基礎使用
print("hello world")

#變數與資料型態
##資料：程式的基本單位

#數字
3456
3.25

#字串
"測試中文"
"hello world"

#布林值
True
False

# List 有順序、可動的列表
[3,4,5]
["what","how"]

#Tuple 有順序、不可動的列表
(33,4,5)
("Hello","World")

# Set 集合
{3,4,5}
{"hello","哈囉"}

# Dictionary 字典
D={"apple":"蘋果","data":"資料"}
print(D)

#變數:用來處存資料的自訂名稱
data=3
note="變數開頭不可為數字"
print(data,note)    #如有重複變數，則新變數資料取代舊變術資料



## 數字、字串基本運算
# 數字運算
x=3+6
print(x)
x=2**4
print(x)

x=6/5       #小數除法
print(x)
x=6//5
print(x)        #整數除法

x=7%3
print(x)        #取餘數


# 字串運算
s="Hello "
y="wor\"ld"
z=s+y
print(z)
print(s+y)

s="Hello\nWorld"    # \n 代表換行
y="""Hello          
World"""            # """""" 也可做到同樣效果
print(s)
print(y)

z="Hello"*3     
print(z)

print(z[1])     #尋照字串索引
print(z[1:4])   #尋找指定範圍內字串
print(z[1:])
print(z[:4])



## 有序列表基本運算 List Tuple
#有序可變動列表 List
grades=[12,65,32,85,250]
print(grades)
print(grades[2])
grades[0]=55        #也可更新列表資料
print(grades[0])

grades[1:4]=[]      #連續刪除列表中 1 到 4(不含) 的資料
length=len(grades)      #取得列表資料長度

#巢狀列表
data=[[3,4,5,],[6,7,8]]
print(data[0][1])


#有序不可變動列表 Tuple
score=(22,55,25,6,35)
print(score[2])
#score[0]=5      # Tuple資料不可改變，會顯示錯誤



### 集合set & 字典 Dictionary
# 集合的運算
s1={3,4,5}
print(3 in s1)
print(10 not in s1)

s2={4,5,6,7}
s3=s1&s2        # 交集：取兩個集合中，相同的資料
s4=s1|s2        # 聯集：取兩個資料中的所有資料，但不重複
s5=s1-s2        # 差集：從 s1 中，減去和 s2 重疊的部分
s6=s1^s2        # 反交集：取兩個資料中，不重疊的部分

s=set("Hello")      # set(字串)：把字串中的字母拆解成集合
print(s)
print("S" in s)


#字典的運算
dic={"apple":"蘋果","key":"鑰匙"}
print(dic["apple"])

print("apple" in dic)       # 判斷 key 是否存在
print("test" in dic)

del dic["apple"]        #刪除字典中的鍵值對 (key-value pair)


dic={x:x**2 for x in [3,4,5]}       #從列表資料中產生字典
print(dic)



### 判斷式
x=input("請輸入數字: ")     #取得字串形式的使用者輸入
x=int(x)        #將字串型態轉換成數字型態
if x>200:
    print("over 200")
elif x>100:
    print("over 100 less than 200")
else:
    print("less than 100")

# sample 2 四則運算
n1=int(input("請輸入數字: "))
n2=int(input("請輸入數字: "))
op=input("請輸入運算( +, -, *, /): ")

if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")



## 迴圈基礎
# While 迴圈
n=1
while n<5:
    print(n)
    n+=1

# 等差級數 相加
n=1
sum=0
while n<=10:
    sum=sum+n
    n+=1
print(sum)


# For 迴圈
for x in [3,5,1]:
    print(x)

for x in "Hello":
    print (x)

for x in range(5):      #range(5) 相當於 [0,1,2,3,4] 的列表
    print(x)
    



## 迴圈進階控制 break continue else
# break sample
n=0
while n<5:
    if n==5:
        break
    print(n)        #印出迴圈中的 n
    n+=1
print("最後的 n:",n)        #印出迴圈結束後的n

# continue sample
n=0
for x in [0,1,2,3]:
    if x%2==0:      # x是偶數
        continue
    print(x)        #只會印出 1、3
    n+=1
print("最後的 n:",n)        #印出 n 被增加的次數

# else sample
sum=0
for n in range(11):
    sum+=n
else:
    print(sum)      # 印出0+1+2+3+.....+10 的結果

# 綜合範例：找出整數平方根
# 輸入9，得到3
# 輸入11，得到 (沒有) 整數平方根
n=input("輸入一個正整數：")
n=int(n)
for i in range(n): # i 從 0~n-1
    if i*i==n:
        print("整數平方根: ", i)
        break       #用 break 強制結束迴圈時，不會執行 else 區塊
else:
    print("沒有整數平方根")



## 函式基礎
#定義函式
def multiply(n1,n2):
    print(n1*n2)

#呼叫函式
multiply(3,4)
multiply(10,8)

#程式的包裝：同意的邏輯可以重複利用
def calculation(n1,n2):
    sum=0
    for n in range(n1,n2):
        sum=sum+n
    print(sum)

calculation(1,80)



### 函式進階
#參數預設資料
def say(msg="hello"):
    print(msg)

say()       #印出預設資料
say("Hello function")       #印出 Hello function

#參數名稱對應
def add(n1,n2):
    result=n1+n2
    print(result)

add(n2=10,n1=5)

#無限/不定 參數
def say(*msgs):         # 無限參數在前方加入 * 標誌
    # 以 Tuple 方式處理
    for msg in msgs:
        print(msg)

say("Hello",5,"Attributes")

# sample 2 - 求平均數
def avg(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n
    print(sum/len(numbers))

avg(3,4)
avg(1,4,-5,-6)



## Module 模組的載入與使用
#載入內建的 sys 模組並取得資訊
import sys
print(sys.platform)
print(sys.maxsize)

#建立 module 模組，載入使用
import module as m
result=m.distance(0,3,0,4)
print(result)
result=m.slope(0,3,0,4)
print(result)

#調整搜尋模組的路徑
print(sys.path)         # 印出模組的搜尋路徑(Python 會依照路徑順序去搜尋模組位置)

sys.path.append("modules.folder")       # 新增模組搜尋路徑


