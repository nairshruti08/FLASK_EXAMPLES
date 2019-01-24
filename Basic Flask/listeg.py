from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
def index():
    numlist= ['shruti','rohini','puja']
    dict1 = {'m':'mca','s':'shruti'}
    return render_template('tmp1.html',numlist=numlist,dict1=dict1)
if __name__=="__main__":
    app.run(debug=True)
