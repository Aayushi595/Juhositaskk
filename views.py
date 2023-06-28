from flask import Flask, render_template,redirect,url_for,request
import mysql.connector as connector


#ESTABLISHING CONNECTION WITH MYSQL DB and creating cursor object

con=connector.connect(host='localhost',port='3307', user='root', password='', database='Juhosidb')
cur = con.cursor()
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def login():

    if request.method == "POST":
        identity=request.form['id']
        password=request.form['pass']
        con = connector.connect()

        query="SELECT * FROM auth WHERE identity= %s AND password=%s"
        cur=con.cursor()
        con.commit()
        cur.execute(query,(identity,password))
        auth=cur.fetchone()
        

   
        if auth is None:
         return "invalid user"
        elif identity=='customer1' and password=='pass1' or identity=='customer2' and password=='pass2':
           return redirect(url_for('customerdetails'))
        else:
           return redirect(url_for('adminpage'))
        
    return render_template('login.html')
    
              
    
@app.route('/customerdetails', methods=['GET','POST'])
def customerdetails(): 
      if request.method == "POST":
        result=None
        OrderDate = request.form['ordt']
        company = request.form['cmpny']
        owner = request.form['ownr']
        item= request.form['itm']
        quantity = request.form['qntity']
        weight = request.form['wght']
        requestForShipment = request.form['reqForShipmnt']
        TrackingId= request.form['trkngId']
        ShipmentSize= request.form['ShpmtSiz']
        BoxCount = request.form['bxCt']
        specification = request.form['specification']
        checklistquantity = request.form['chklstqntity']

        query = "INSERT INTO customertable (ORDERDATE,COMPANY,OWNER,ITEM,QUANTITY,WEIGHT,REQUESTFORSHIPMENT,TRACKINGID,SHIPMENTSIZE,BOXCOUNT,SPECIFICATION,CHECKLISTQUANTITY) VALUES (%s, %s, %s,%s, %s, %s,%s,%s,%s,%s,%s,%s)"
        values = (OrderDate, company,owner,item,quantity,weight,requestForShipment,TrackingId,ShipmentSize,BoxCount,specification,checklistquantity)
        cur.execute(query, values)
        con.commit()
        cur.close()  
      return render_template('customerdetails.html')
    
    
@app.route('/adminpage',methods=["POST","GET"])
def adminpage():
  
  con = connector.connect()

  query = "SELECT QUANTITY, WEIGHT,BOXCOUNT FROM customerdetails"
  cur=con.cursor()
  cur.execute(query)
  item=("QUANTITY","WEIGHT","BOXCOUNT")
  data = cur.fetchall()
  

  return render_template('adminpage.html', data=data , item=item)





      

         
        
        