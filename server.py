from flask import Flask

app=Flask(__name__)

@app.route('/ /<a>',methods=["GET"] )
def hello(a):
    if(a==''):
        return "Hello World"
    else:
        return "Sorry! No response. Try again."


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    output = ''
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output


if __name__=="__main__":
    app.run(debug=True)