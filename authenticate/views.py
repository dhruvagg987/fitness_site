from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import signup_form ,edit_form, password_changeform ,userprofileForm ,edit_profileform
from django.http import JsonResponse

# Create your views here.
def home(request):
    # logger=logging.getLogger(__name__)
    # logger.log("ddcd vfxfcbfcbcfhgcngvngvgcnvngngvgcnvgjgvjgvjvgj******************************")
    return render(request,  'templates/home.html',  {})
    # return JsonResponse(request)    


def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been Logged in !'))
            return redirect('home')
        else:
            messages.success(request, ('Error logging in - please try again !'))
            return redirect('login')
    else:
        return render(request,  'templates/login.html',  {})
        # return JsonResponse(request)    


def logout_user(request):
    messages.success(request, ('You have been Logged Out !'))
    logout(request)
    return redirect('home')

def register_user(request):

    if request.method=='POST':
        form=signup_form(request.POST)
        profile_form=userprofileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            profile=profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request, user)
            messages.success(request, ('You have been successfully Registered !'))
            return redirect('home')            
    else:
        form=signup_form()
        profile_form=userprofileForm()
    context={'form':form ,'profile_form':profile_form}        
    return render(request,  'templates/register.html',  context)  

def edit_profile(request):
    if request.method=='POST':
        form=edit_form(request.POST, instance=request.user)
        form2=edit_profileform(request.POST, instance=request.user.userprofile)
        if form.is_valid() and form2.is_valid():
            # form.save()
            # form2.save()
            user=form.save()
            profile=form2.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, ('You have successfully eddited !'))
            return redirect('home')            
    else:
        form=edit_form(instance=request.user)
        form2=edit_profileform(request.POST, instance=request.user.userprofile)
    context={'form':form ,'form2' :form2}        
    return render(request, 'templates/edit_profile.html',context)

def change_password(request):
    if request.method=='POST':
        form=password_changeform(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('Your Password Has Been Changed successfully !'))
            return redirect('home')            
    else:
        form=password_changeform(user=request.user)
    context={'form':form}        
    return render(request, 'templates/change_password.html',context)

def workout(request):
    return render(request,  'templates/workout.html',  {})

def programs(request):
    return render(request,  'templates/programs.html',  {})

def health_living(request):
    return render(request,  'templates/health_living.html',  {})

def about(request):
    return render(request,  'templates/about.html',  {})

def contact(request):
    return render(request,  'templates/contact.html',  {})        
