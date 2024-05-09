## 封包的設計與使用 - 用來整理、分類模組程式
# -專案資料夾
#   -主程式.py
#   -封包資料夾
#       -_init_.py
#       -模組一.py
#       -模組二.py

#主程式
import 封包資料夾.point
result=封包資料夾.point.diestance(3,4)
print("距離: ",result)
import 封包資料夾.line
result=封包資料夾.line.slope(0,0,3,4)
print("斜率: ", result)