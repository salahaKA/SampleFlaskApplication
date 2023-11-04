from trace import Trace
from flask import Flask,render_template,request,make_response
import csv
from werkzeug.utils import secure_filename
import sqlite3

app=Flask(__name__)                                               

@app.route('/')                                                      
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/uploaddata')
def uploaddata():
    return render_template("dataloader.html")

@app.route('/uploadajax',methods=['POST'])
def uploadajax():
    if request.method=='POST':

        conn=sqlite3.connect('database.db')
        cur=conn.cursor()

        prod_mas=request.files['prod_mas']
        filename=secure_filename(prod_mas.filename)
        prod_mas.save('./static/upload/'+filename)

        fields=[]
        rows=[]
        fn='./static/upload/'+filename
        with open(fn,'r') as csvfile:
            csvreader=csv.reader(csvfile)
            for row in csvreader:
                rows.append(row)
                print(row)

        try:
            for row in rows[1:]:
                if row[0][0]!="":
                    query="";
                    query="insert into dataset values("
                    for col in row:
                        query=query+"'"+col+"',"
                    query=query[:-1]
                    query=query+");"
                    print(query)
                    cur.execute(query)
                    conn.commit()
        except:
            print("Query excecution")
        msg="sucess"
        return render_template("dataloader.html",data=msg)
        






if __name__=='__main__':
    app.run(debug=True)                                                           

