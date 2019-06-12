from django.shortcuts import render , redirect
from acoounts.forms import (
    RegistrationForm , 
    EditProfileForm , 
    ProfileForm,
    
)

from forum.models import Bang

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
#from acoounts.forms import handle_uploaded_file



def register(request):

    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login')
        else:
           return HttpResponseRedirect('/accounts/register')
    else:
        form=RegistrationForm()
        args={'form':form}
        return render(request,'acoounts/register.html',args)

@login_required
def profile(request):

    horse=Bang.objects.filter(user=request.user)
    args={'user': request.user, 'horse':horse}
    return render(request, 'acoounts/profile.html', args)

@login_required
def edit_profile(request):
        if request.method == "POST":
            form = EditProfileForm(request.POST, instance = request.user)
            form1 = ProfileForm( request.POST, request.FILES, instance=request.user.userprofile)
            if form.is_valid() and form1.is_valid():
                 form.save()
                 form1.save()
                 
                 return redirect('/accounts/profile')
            
            else:
                return HttpResponseRedirect('/accounts/profile/edit')
   

        else:
            form = EditProfileForm(instance = request.user)
            form1 = ProfileForm( instance=request.user.userprofile)
            return render(request, 'acoounts/edit.html', {'form':form,'form1':form1})     

@login_required    
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return HttpResponseRedirect('/accounts/profile/change_pass')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form' : form}
        return render(request,'acoounts/chpass.html',args)






		
