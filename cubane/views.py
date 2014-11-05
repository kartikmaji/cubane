from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html',{})

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

def login(request):
	return HttpResponse("Login is here")