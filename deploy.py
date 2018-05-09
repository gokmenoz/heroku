from flask import Flask
app=Flask(__name__)
@app.route("/")
import pandas
def index():
    return "hello"
if __name__=="__main__":
    app.run()
