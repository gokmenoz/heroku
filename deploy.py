from flask import Flask
import os

app=Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__=="__main__":
    app.debug=False
    app.run(host="0.0.0.0")
