from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def head():
    return render_template ("index.html", number1=10, number2=20)

@app.route('/<string:num1>/<string:num2>')
def mynums(num1, num2):
    return render_template("index.html", number1=num1, number2=num2)





if __name__== "__main__":
    app.run(debug=True,)
    # app.run(host= '0.0.0.0', port=8081)
    