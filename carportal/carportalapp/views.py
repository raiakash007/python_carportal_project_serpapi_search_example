from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from carportalapp.models import insertinContactMethod
from carportalapp.models import insertinSignupMethod
from carportalapp.models import CheckloginuserExists
from carportalapp.models import getRegisterduserModel
from carportalapp.models import insertinaddProductmethod
from carportalapp.models import insertinaddProductmethodUser
from carportalapp.models import getUserDataModel
from carportalapp.models import getProductListingModel
from carportalapp.models import getCarDetailsByIdModel
from serpapi import GoogleSearch


# Create your views here.
def homemethod(request):
	return render(request,'home.html')

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def indexmethod(request):
   	return render(request,'index.html')

def carsmethod(request):
   	return render(request,'cars.html')

def contactusmethod(request):  
	name = request.POST['name']
	subject = request.POST['subject']
	email = request.POST['email']
	message = request.POST['message']
	insertinContactMethod(name,subject,email,message)
	return render(request,'contact.html',{"success":"Thank You For Contacting Us"})

def contactusrender(request):
	return render(request,'contact.html',{"success":""})

def userlogin(request):  
	return render(request,'login.html')

def userloginmethod(request):
	email=request.POST['email']
	password=request.POST['password']

	checkloginUserFlag = CheckloginuserExists(email,password)

	if checkloginUserFlag >= 1:
		userData = getUserDataModel(email)
		#create session
		request.session['user_email'] = email
		request.session['user_id'] = userData[0]

		return render(request,'customerdashboard.html',{"success1":"user login successfully","user_email":email})
	elif checkloginUserFlag == 0:
		return render(request,'login.html',{"error_message":"Invalid login details"})

def userdashboard(request):
	if request.session['user_email']=="":
		return render(request,'login.html',{"error_message":"Invalid login details"})
	else:
		return render(request,'cars.html',{"success":""})	
def adminmethod(request): 
	username= request.POST['username'] 
	password = request.POST['password'] 

	if username == "admin" and password=="admin":
		#create session
		request.session['user_email'] = username
		return render(request,'admindashboard.html',{"success1":"Logged-in successfully","user_email":username})
	else:
		return render(request,'admin.html',{"error_message":"Invalid login details"})

def admindashboard(request):
	if request.session['user_email']=="":
		return render(request,'admin.html',{"error_message":"Invalid login details"})
	else:
		return render(request,'admindashboard.html',{"success":""})

def adminlogin(request):
	return render(request,'admin.html',{})

def signupmethod(request):
	#get form data within python method as defined in the route of the form
	firstname = request.POST['fname']
	lastname = request.POST['lname']
	email = request.POST['email']
	mobile = request.POST['mobile_no']
	password=request.POST['password']
	address=request.POST['address']
   	#call insertDataModel
	insertinSignupMethod(firstname,lastname,email,mobile,password,address)
	return render(request,'signup.html',{"success":"Thank You"})

def signuprender(request):
		return render(request,'signup.html',{"success":""})

def adminlogout(request):
	request.session['user_email'] = ""
	return render(request,'admin.html',{"success_message":"Logged-out successfully"})

def registeredusers(request):
	result=getRegisterduserModel()
	username = request.session['user_email']
	return render(request,'registereduser.html',{'result':result,"user_email":username})

def addProductmethod(request):
	product_name = request.POST['product_name']
	product_price = request.POST['product_price']
	product_description = request.POST['product_description']
	product_quantity = request.POST['product_quantity']
	product_location= request.POST['product_location']
	product_model=request.POST['product_model']
	manufacturing_date=request.POST['manufacturing_date']
	product_condition = request.POST['product_condition']
	#product_video = request.POST['product_video']
	#product_image = request.POST['product_image']
	product_color = request.POST['product_color']
	product_url=request.POST['product_url']
	if username == "admin":
	   	#call insertDataModel
	   	insertinaddProductmethod(product_name,product_price,product_description,product_quantity,product_location,product_model,manufacturing_date,product_condition,product_color,product_url)
	username = request.session['user_email']
	return render(request,'addproduct.html',{"user_email":username,"success":"thank you"})

def addproductrender(request):
		username = request.session['user_email']
		return render(request,'addproduct.html',{"success":"","user_email":username})
def addProductbycustomermethod(request):
	product_name = request.POST['product_name']
	product_price = request.POST['product_price']
	product_description = request.POST['product_description']
	product_quantity = request.POST['product_quantity']
	product_location= request.POST['product_location']
	product_model=request.POST['product_model']
	manufacturing_date=request.POST['manufacturing_date']
	product_condition = request.POST['product_condition']
	#product_video = request.POST['product_video']
	#product_image = request.POST['product_image']
	product_color = request.POST['product_color']
	product_url=request.POST['product_url']
	#call insertDataModel
	username = request.session['user_email']
	user_id = request.session['user_id']

	insertinaddProductmethodUser(product_name,product_price,product_description,product_quantity,product_location,product_model,manufacturing_date,product_condition,product_color,product_url,user_id)
	return render(request,'addproductbycustomer.html',{"user_email":username,"success":"thank you"})

def addproductrenderbycustomer(request):
		username = request.session['user_email']
		return render(request,'addproductbycustomer.html',{"success":"","user_email":username})


def productlisting(request):
	result=getProductListingModel()
	return render(request,'cars.html',{'result':result})

def cardetailmethod(request):
	id = request.GET['id']
	getCarDetails = getCarDetailsByIdModel(id)
	return render(request,'car-details.html',{'result':getCarDetails})

def servicecentermethod(request):
	return render(request,'servicecenter.html',{"success":""})

def serviceprocess(request):
	search_query=request.POST['search']
	
	params = {
	  "api_key": "17487d86d74faf8eb5556574b6f10063018fd4780f00492ff9574b148b302582",
	  "engine": "google",
	  "q": search_query,
	  "location": "Austin, Texas, United States",
	  "google_domain": "google.com",
	  "gl": "us",
	  "hl": "en"
	}

	search = GoogleSearch(params)
	results = search.get_dict()
	return render(request,'servicecenter.html',{"result":results["organic_results"],"search_query":search_query})