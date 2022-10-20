from django.shortcuts import render
#from datetime import date
from django.utils import timezone
from myapp.models import User, Message

def myview(request):
	return render(request, "index.html")
	
def login(request):
	
	user_name = request.POST["user"]
	user_pass = request.POST["password"]
	
	if User.objects.filter(name=user_name):
		db_user = User.objects.get(name=user_name)
		# user found!
		if db_user.password != user_pass:
			# incorrect password
			notice = "oops " + db_user.name + ", this password is incorrect!"
			action = "please try again."	
			return render(request, "index.html", {"notice": notice, "action": action, "user": db_user })
	else:
		# user not found!
		notice = "oops, no such user was found!"
		action = "please sign up below."
		return render(request, "index.html", {"notice": notice, "action": action })

	messages = Message.objects.all()	
	return render(request, "chat.html", {"chat": messages, "user": db_user})

def send_chat(request):
	print("received message")
	
	msg = request.POST["msg"]
	user = request.POST["user_name"]

	db_user = User.objects.get(name=user)
	
	m = Message(message=msg, time=timezone.now(), user=db_user)
	m.save()

	messages = Message.objects.all()	
	return render(request, "chat.html", {"chat": messages, "user": db_user })

def sign_up(request):
	return render(request, "signup.html")

def create_user(request):
	#add message area in index
	user = request.POST["user"]
	password = request.POST["password"]
	password_conf = request.POST["password_conf"]

	if User.objects.filter(name=user):
		# bad username
		notice = "oops! username is already taken"
		action = "please choose a differtent name"
		return render(request, "signup.html", {"notice": notice, "action": action})
	else:
		if password == password_conf:
			create_user = User(name=user, password=password)
			create_user.save()
			notice = "new user was successfully crerated!"
			action = "please log in."
			return render(request, "index.html", {"notice": notice, "action": action})
		else:
			# bad password
			notice = "oops, password fields don't match!"
			action = "please try again."
			return render(request, "signup.html", {"notice": notice, "action": action})
	