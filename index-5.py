## Python Pandad 資料分析
# 載入 Pandas 模組
import pandas as pd

# 建立 Series
# data=pd.Series([20,10,15])
# 基本 Series 操作
# print(data)
# print("Max",data.max())
# print("Median",data.median())

# data=data*2
# print(data)

# data=data==20
# print(data)

# 建立 DataFrame
# data=pd.DataFrame({
#     "name":["Amy","John","Bob"],
#     "salary":[30000,50000,60000]
# })

# # 基本 DataFrame 操作
# # print(data)

# # print(data["name"])     # 取得特定的欄位
# print(data.iloc[0])     # 取得特定的列，印出第一列



## Series 單維度資料
# 資料索引
data=pd.Series([20,50,30,-2,-7],index=["a","b","c","d","g"])
# print("資料型態: ", data.dtype)
# print("資料數量: ", data.size)
# print("資料索引: ", data.index)

# 取得資料: 根據順序、根據索引
# print(data[2],data[0])
# print(data["c"],data["g"])

# 數字運算: 基本、串接、搜尋、取代
# print("最大值: ", data.max())
# print("總和: ", data.sum())
# print("標準差: ", data.std())
# print("中位數: ", data.median())
# print("最大的三個數: ",data.nlargest(3))
# print("最小的三個數: ",data.nsmallest(3))

# 字串運算: 基本、串接、搜尋、取代
data=pd.Series(["您好","Python","Pandas"])
# print(data.str.lower())     # 全部變小寫
# print(data.str.len())   # 計算字串長度
# print(data.str.cat(sep=","))    # 把字串串接，可以自訂串接符號
# print(data.str.contains("P"))   # 確認字串是否包含大寫 P
# print(data.str.replace("您好","Hello"))



## DataFrame - 雙維度資料
# 資料索引: pd.DataFrame(字典, index=索引列表)
# data=pd.DataFrame({
#     "name":["Amy","Bob","Jason"],
#     "salary":[50000,10000,3000]
# },index=["a","b","c"])
# print(data)
# print("------------------------")

# 觀察資料
# print("資料數列: ",data.size)
# print("資料形狀(列,欄): ", data.shape)
# print("資料索引: ", data.index)

# 取得列 (Row/橫向) 的 Series 資料: 根據順序、根據索引
# print("取得第二列:", data.iloc[1],sep="\n")
# print("取得第c列:", data.loc["c"],sep="\n")

# 取得欄 (Column/直向) 的 Series 資料: 根據欄位的名稱
# print("取得 name 欄位", data["name"],sep="\n")
# names=data["name"]      # 取得單維度的 Series 資料
# print("把 name 全部轉大寫", names.str.upper(),sep="\n")

# 計算薪水的平均值
# salaries=data["salary"]
# print("薪水的平均值", salaries.mean())

# 建立新的欄位
# data["revenue"]=[50000,90000,70000]     # data[新欄位的名稱]=列表
# data["rank"]=pd.Series([3,6,1],index=["a","b","c"])     # data[新欄位的名稱]= Series 的資料
# data["cp"]=data["revenue"]/data["salary"]
# print(data)



### 篩選資料
# sample-1
# data=pd.Series([30,20,15])
# condition=[True,False,True]
# filteredData=data[condition]
# print(filteredData)

# sampel-2
# condition=data>18
# filteredData=data[condition]
# print(filteredData)

# sample-3
# data=pd.Series(["你好","Pandas","Python"])
# condition=data.str.contains("P")
# filteredData=data[condition]
# print(filteredData)


# 篩選練習 - DataFrame
# data=pd.DataFrame({
#     "name":["Amy","Bob","Jason"],
#     "salary":[40000,50000,60000]
# })
# condition=data["salary"]>45000
# filteredData=data[condition]
# print(filteredData)

# condition=data["name"]=="Amy"
# filteredData=data[condition]
# print(filteredData)



## 資料分析 - 實務演練
# 讀取資料
data=pd.read_csv("googleplaystore.csv")

# 觀察資料
# print("資料數量: ", data.shape)
# print("資料欄位: ", data.columns)

# 分析資料: 評分的各種統計數據
# condition=data["Rating"]<=5 
# data=data[condition]        # 篩選出評分小於等於 5 的評分

# print("平均數:",data["Rating"].mean())
# print("中位數", data["Rating"].median())
# print("取得嫌一百個應用程式的平均", data["Rating"].nlargest(100).mean())

# 分析資料: 安裝數量的各種統計數據
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","",regex=True).replace("Free",""))
print("平均數:", data["Installs"].mean())
condition=data["Installs"]>100000
print("安裝數量大於 100000 的應用程式有幾個",data[condition].shape[0])

# 基於資料的應用: 關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字: ")
condition=data["App"].str.contains(keyword, case=False)
# print(data[condition]["App"])
print("包含關鍵字的應用程式數量", data[condition].shape[0])