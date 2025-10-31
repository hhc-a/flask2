from flask import Flask,request,render_template 
# 匯入 Flask 套件中的 Flask 類別 # 匯入 Flask 與 request 模組 # 匯入 render_template
app = Flask(__name__) # 建立 Flask 應用程式物件
# 定義一個路由與對應函式
@app.route("/")
def home():
    #return "Hello FlaskBook!" # 回傳給瀏覽器顯示的文字
    homepage = "<h1>Flask 範例主選單 </h1>"
    homepage += "<a href='/user/ 梓 '> 使用動態路由 </a><br>"
    homepage += "<a href='/search?keyword=flask&limit=5'>GET傳遞參數 </a><br>"
    homepage += "<a href='/poster'>POST 表單傳值 </a><br>"
    homepage += "<a href='/hello/zi?score=90'> 模板渲染（ Template ） </a><br>"
    return homepage

@app.route("/user/<string:name>")
def user(name):
    return f"<H1> 哈囉， {name} ！歡迎來到 我的網頁～ </H1>"

# 範例：使用 GET 傳遞參數
@app.route("/search", methods=["GET"])
def search():
# 使用 request.args.get() 取得網址中的參數
    keyword = request.args.get("keyword") # 取得搜尋關鍵字
    limit = request.args.get("limit") # 取得筆數限制
    # 若未提供參數則顯示提示
    if not keyword:
        return " 請輸入搜尋關鍵字，例如： /search?keyword=flask"
    # 顯示取得的參數內容
    return f" 搜尋關鍵字： {keyword}<br> 顯示筆數限制： {limit or ' 未指定 '}"

# --- POST 表單頁面 ---
@app.route('/poster', methods=['GET', 'POST'])
def poster():
    if request.method == 'POST':
        # 使用 request.values.get() 取得表單資料
        username = request.values.get('username', ' 未輸入 ')
        password = request.values.get('password', ' 未輸入 ')
        return f"<h3>POST 接收到的使用者： {username} ，密碼： {password}</h3>"
    else:
        # 顯示輸入表單
        return '''
        <h2>Flask POST 傳送資料範例 </h2>
        <form action="#" method="post">
            <p> 姓名： <input type="text" name="username"></p>
            <p> 密碼： <input type="password" name="password"></p>
            <p><button type="submit"> 送出 </button></p>
        </form>
        '''
    
# 建立動態路由，接收 name 參數
@app.route('/hello/<string:name>')
def hello(name):
    score = request.args.get("score", default=80, type=int)
    user = {"name": name, "email": "aaa@example.com"}
    items = ["Flask", "Jinja", "Blueprint", "WTForms"]
    # 傳送參數給模板， **locals() 代表傳送所有本地變數
    return render_template('hello.html', **locals())

# 主程式進入點
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000) # 啟動 Flask 開發伺服器