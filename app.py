from flask import Flask,render_template          # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return render_template('index.html')         # which returns "hello world"

@app.route("/about")
def about():
    return render_template('about-us.html')

@app.route("/blog-home")
def blogHome():
    return render_template('blog-home.html')

@app.route("/blog-single")
def blog():
    return render_template('blog-single.html')

@app.route("/category")
def category():
    return render_template('category.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/elements")
def element():
    return render_template('elements.html')

@app.route("/price")
def price():
    return render_template('price.html')

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/single")
def single():
    return render_template('single.html')

if __name__ == "__main__":        # on running python app.py
    app.run()                    # run the flask app