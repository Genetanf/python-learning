from flask import Flask
app=Flask(__name__)     # __name__ 帶鰾目前執行的模組

@app.route("/")     # 函式的裝飾 (Decorateor): 以函式為基礎，提供附加功能
def home():
    return "Hello Flask"

@app.route("/test")     # 代表我們要處理的網站路徑
def test():
    return "This is Test"

if __name__=="__main__":    # 如果以主程式進行
    app.run()   # 立刻啟動伺服器



