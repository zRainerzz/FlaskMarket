from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def inscription():
    return render_template("inscription.html")

@app.route("/login")
def login():
    return render_template('login.html')
    #http://127.0.0.1:5000/login
    
@app.route("/first_test")
def file_test():
    return render_template('first_test.html')

@app.route("/navbar")
def navbar():
    return render_template("navbar.html")

@app.route("/project_css")
def project_css():
    return render_template('project_css.html')

@app.route("/try")
def try_():

    items = [
        {'id':1, 'name':'Phone', 'barcode':'5575421658', 'price':'500'},
        {'id':2, 'name':'Laptop', 'barcode':'557542999', 'price':'900'},
        {'id':3, 'name':'Keyboard', 'barcode':'5575420000', 'price':'150'},
        

    ]
    #in the try.html file we write this line of code <p>{{item}}</p>               OUTPUT: the value of item name.
    return render_template('try.html', items=items)






