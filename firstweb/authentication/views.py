from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")



def signup(requset):
    if requset.method == "POST":
        #username = requset.POST.get('username')
        username = requset.POST['username']
        fname    = requset.POST['fname']
        lname    = requset.POST['lname']
        email    = requset.POST['email']
        pass1    = requset.POST['pass1']
        pass2    = requset.POST['pass2']
        

        
        myuser   = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name  = lname



        myuser.save()

        messages.success(requset, "Your Account has been successfully created!")


        return redirect('signin')

    return render(requset, "authentication/signup.html")



def signin(requset):
    if requset.method == "POST":
        username = requset.POST['username'] 
        pass1    = requset.POST['pass1']

        user     = authenticate(username = username, password= pass1)

        if user is not None: 
            login(requset, user)
            fname = user.first_name
            return render(requset, "authentication/index.html", {'fname': fname})
        else:
            messages.error(requset, "Bad credentials!")
            return redirect(home)

    return render(requset, "authentication/signin.html")



def signout(requset):
    logout(requset)
    messages.success(requset, "You have been successfully signed out!")
    return redirect(home)


