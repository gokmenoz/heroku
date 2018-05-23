from flask import Flask,render_template,request
app_lulu = Flask(__name__)

@app_lulu.route('/index_lulu',methods=['GET','POST'])
def index_lulu():
    if request.method == "GET":
        return render_template('userinfo_lulu.html')
    else:
        if request.form["price"]=="CS":
            return app_lulu.send_static_file('index.html')
        if request.form["price"]=="PUBG":
            return app_lulu.send_static_file('index1.html')

if __name__ == "__main__":
    app_lulu.run(debug=True)
