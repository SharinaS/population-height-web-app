from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgre123@localhost/height_collector'

app.config['SQLALCHEMY_DATABASE_URI']='''postgres://zvoobimopippgl:25999a5a699
82e89adcbfd3e7d0614aa4679f94839e31d783425d7f32d54db4b@ec2-54-227-241-179.compu
te-1.amazonaws.com:5432/d35n1fmkkdofcl?sslmode=require'''

db=SQLAlchemy(app)


class Data(db.Model):
	__tablename__="data"
	id=db.Column(db.Integer, primary_key=True)
	email_=db.Column(db.String(120), unique=True)
	height_=db.Column(db.Integer)

	def __init__(self, email_, height_):
		self.email_=email_
		self.height_=height_ 


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
	if request.method=='POST':
		email=request.form["email_name"]
		height=request.form["height_name"]
		if db.session.query(Data).filter(Data.email_==email).count() == 0:
			data=Data(email,height)
			db.session.add(data)
			db.session.commit()
			average_height=db.session.query(func.avg(Data.height_)).scalar() 
			average_height=round(average_height,1)
			count=db.session.query(Data.height_).count()
			send_email(email, height, count, average_height) 
			return render_template("success.html")
	return render_template('index.html', 
		text="That email address has already been used. Please submit a different email address.")


if __name__=="__main__":
	app.debug=True
	app.run()