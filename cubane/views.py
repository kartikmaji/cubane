from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from django.contrib.auth import login,authenticate
from django.template import RequestContext
def home(request):
    if not request.user.is_authenticated():
        return render(request,'index.html',{})
    else:
        return render(request,'welcome.html',{})

def signup(request):
    if not request.user.is_authenticated():
        if request.method=="POST":
            form= SignupForm(request.POST,request.FILES)
            if form.is_valid():
                password=request.POST['password']
                password1=request.POST['password1']
                if(password==password1):
                    #new_user = MyUser.objects.create_user(**form.cleaned_data)
                    email=request.POST['email']
                    firstname=request.POST['firstname']
                    lastname=request.POST['lastname']
                    username = request.POST['username']
                    mobile=request.POST['mobile']
                    new_user = MyUser.objects.create_user(email,firstname,lastname,mobile,date_of_birth,password)
                    MyUser.backend='django.contrib.auth.backends.ModelBackend'
                    authenticate()
                    login(request,new_user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Your password don't match please try again")
            else:
                return render(request,'adduser.html',{'form':form})
        else:
            form = SignupForm()
        return render(request,'adduser.html',{'form':form})
    else:
        return HttpResponseRedirect('/')    

def user_login(request):
    if not request.user.is_authenticated():
        context = RequestContext(request)
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    authenticate()
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Your account is disabled")
            else:
                return HttpResponse("Invalid login")
        else:	
            return render_to_response("login.html",{},context)
    else:
        return HttpResponseRedirect('/')
	#return HttpResponse("Login is here")