from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from MyUser.models import MyUser,Channels
from django.contrib.auth import login,authenticate
from django.template import RequestContext
from MyUser.forms import SignupForm,NewChannelForm
def home(request):
    if not request.user.is_authenticated():
        return render(request,'index.html',{})
    else:
    	user=request.user
    	channels = Channels.objects.order_by('name')
        return render(request,'welcome.html',{'user':user,'channels':channels})

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
                    new_user = MyUser.objects.create_user(email,firstname,lastname,username,mobile,password)
                    MyUser.backend='django.contrib.auth.backends.ModelBackend'
                    authenticate()
                    login(request,new_user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Your password don't match please try again")
            else:
                return render(request,'signup.html',{'form':form})
        else:
            form = SignupForm()
        return render(request,'signup.html',{'form':form})
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
            return render_to_response("welcome.html",{},context)
    else:
        return HttpResponseRedirect('/')
	#return HttpResponse("Login is here")

def newchannel(request):
    if request.user.is_authenticated():
        if request.method=="POST":
            form= NewChannelForm(request.POST)
            if form.is_valid():
                owner=request.user
                name=form.cleaned_data['name']
                #message=form.cleaned_data['message']
                newchannel=Channels(name=name,owner=owner)
                newchannel.save()
                return HttpResponseRedirect('/')
        else:
            form = NewChannelForm()
        return render(request,'addchannel.html',{'form':form})
    else:
        return HttpResponseRedirect('login') 

def showchannel(request):
    if request.user.is_authenticated():
        return render(request,'welcome.html',{})
    else:
        return HttpResponseRedirect('login') 