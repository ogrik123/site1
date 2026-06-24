from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def blog():
    return render_template("blog.html")
@app.route("/ind/")
def index():
    return render_template("index.html")
@app.route("/planet/")
def minecraftindex():
    return render_template("minecraftindex.html")
@app.route("/subnutica/")
def subnaticaindex():
    return render_template("subnuticaindex.html")
@app.route("/bye/")
def bye():
    return "bye"
@app.route("/mark/")
@app.route("/Mark/")
def hello1():
    return "hello Mark"
@app.route("/max/")
@app.route("/Max/")
def hello2():
    return "hello Max"
@app.route("/bob/")
@app.route("/Bob/")
def hello3():
    return "hello Bob"

@app.route("/name/<name>/")
def sayname(name=None):
    if name == None:
        return "enter is locked"
    else:
        return f"hello, {name.title()}"
# @app.route("/<number>/")
# def saynum(number):
#     return f":{number}"
@app.route("/goodday/")
def day():
    return "good day"
if __name__ == "__main__":
    app.run()
#                                       сделать файл и стр 39 9 тема
