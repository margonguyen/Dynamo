from flask import Flask,render_template,request,session          # import flask
from dynoDb import dynoDb
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def index():                      # call method hello
    
    return render_template('index.html')         # which returns "hello world"

@app.route("/about")
def about():
    return render_template('about-us.html')

@app.route("/index.html")
def hello():
    return render_template('index.html')

@app.route("/category", methods=['GET'])
def category():
    if request.method == "GET":
        a = request.args.get('category')
        data = dynoDb().getJobs(a)
    return render_template('category.html', data = data, category = a)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        d = request.form['search'].split(" ")
        newString = ""
        for i in d:
            newString += "\w*" + i + "\w*|"
            if(newString.endswith("|")):
                 newString = newString[:-1]
        group = (dynoDb().findInfo(newString,request.form['category']))
        print(group)
        return render_template('search.html', group = group)
    return render_template('search.html')
    

@app.route("/single", methods=['GET', 'POST'])
def single():
    if request.method == 'GET':
        a = request.args.get('pid')
        data = dynoDb().getJobPid(a)
    return render_template('single.html',data = data, cert = cert)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        db = request.form
        dynoDb().LogInUser(db)
        session['loggedin'] = True
        return render_template('index.html')
    return render_template('login.html')


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        db = request.form
        dynoDb().RegisterUser(db)
        return render_template('index.html')
    return render_template('signup.html')

@app.route("/logout", methods=[ 'GET'])
def logout():
    session.pop('loggedin', None)
    return render_template('index.html')

if __name__ == "__main__":        # on running python app.py
    app.secret_key = "Bitch im a cow"

    app.run(debug=False)                    # run the flask app