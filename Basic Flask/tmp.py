from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name ="shruti"
    return render_template('tmp.html')+ name

if __name__=="__main__":
    app.run(debug=True)
