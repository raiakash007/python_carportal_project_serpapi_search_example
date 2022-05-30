from django.db import models
# Create your models here.
from django.db import connection
from django.core.files.storage import FileSystemStorage
# Create your models here.
def insertinContactMethod(name,subject,email,message):
	cursor = connection.cursor()
	sql = ("insert into contact_us(name,subject,email,message) values('%s','%s','%s','%s')" % (name,subject,email,message))
	cursor.execute(sql)
	connection.close()
def insertinSignupMethod(first_name,last_name,email,mobile_no,password,address):
	cursor = connection.cursor()
	sql = ("insert into sign_up(first_name,last_name,email,mobile_no,password,address) values('%s','%s','%s','%s','%s','%s')" % (first_name,last_name,email,mobile_no,password,address))
	cursor.execute(sql)
	connection.close()
def CheckloginuserExists(email,password):
	cursor=connection.cursor()
	sql=("select * from sign_up where email ='%s'and password='%s'"%(email,password))
	cursor.execute(sql)
	rows_effected = cursor.rowcount
	return rows_effected
	connection.close()
def getRegisterduserModel():
	cursor=connection.cursor()
	sql=("select *from sign_up")
	cursor.execute(sql)
	rows_effected = cursor.fetchall()
	return rows_effected
	connection.close()
def insertinaddProductmethod(product_name,product_price,product_description,product_quantity,product_location,product_model,manufacturing_date,product_condition,product_color,product_url):
	cursor = connection.cursor()
	sql = ("insert into product(product_name,product_price,product_description,product_quantity,product_location,product_model,manufacturing_date,product_condition,product_color,product_url) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (product_name,product_price,product_description,product_quantity,product_location,product_model,manufacturing_date,product_condition,product_color,product_url))
	cursor.execute(sql)
	connection.close()

def insertinaddProductmethodUser(product_name,product_price,product_description,product_quantity,product_location,product_model,manufacturing_date,product_condition,product_color,product_url,user_id,uploaded_file_url,final_urlVideo):
	cursor = connection.cursor()
	sql = ("insert into product(product_name,product_price,product_description,product_quantity,product_location,product_model,manufacturing_date,product_condition,product_color,product_url,created_by,product_image,product_video) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (product_name,product_price,product_description,product_quantity,product_location,product_model,manufacturing_date,product_condition,product_color,product_url,user_id,uploaded_file_url,final_urlVideo))
	cursor.execute(sql)
	connection.close()

def getUserDataModel(email):
	cursor=connection.cursor()
	sql=("select *from sign_up where email='%s'"%(email))
	cursor.execute(sql)
	rows_effected = cursor.fetchone()
	return rows_effected
	connection.close()

def getProductListingModel():
	cursor=connection.cursor()
	sql=("select *from product")
	cursor.execute(sql)
	rows_effected = cursor.fetchall()
	return rows_effected

def getCarDetailsByIdModel(id):
	cursor=connection.cursor()
	sql=("select *from product where id='%s'"%(id))
	cursor.execute(sql)
	rows_effected = cursor.fetchall()
	return rows_effected
	connection.close()
