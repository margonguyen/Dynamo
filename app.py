from flask import Flask,render_template          # import flask
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return render_template('index.html')         # which returns "hello world"

@app.route("/about")
def about():
    return render_template('about-us.html')
if __name__ == "__main__":        # on running python app.py
    app.run()                    # run the flask app