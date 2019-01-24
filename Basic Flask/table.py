from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
def index():
    dic={
        'Maths':85,
        'science':95
        }
    print(dic)
    return render_template('table.html',result=dic)

if __name__=="__main__":
    app.run(debug=True)

