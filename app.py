
from flask import Flask,render_template,jsonify,request
from second import second
app= Flask(__name__)
@app.route('/',methods=['GET','POST'])
def game():
    if(request.method=='GET'):
        data="hello world,welcome the the computer world"
        return jsonify({'data':data})
@app.route("/")
def my():
    return render_template('index.html')
@app.route("/index")
def Home():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/contact")
def contact():

    return render_template('contact.html')
@app.route("/post")
def post():
    return render_template('post.html')
@app.route("/layout")
def layout():
    return "<h1>Thander Code</h1>"
@app.route("/lay")
def lay():
    return "<h1>Test</h1>"


app.run(debug=True)