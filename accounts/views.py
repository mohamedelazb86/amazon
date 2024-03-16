from django.shortcuts import render,redirect
from .forms import SignupForm,ActivateForm
from django.core.mail import send_mail
from .models import Profile
from django.contrib.auth.models import User

def signup(request):

    ''' 
    - create new user
    - stop activate this user  علشان نمنع المستخدم من الدخول مباشرة على الموقع قبل تفعيل الكود
    - send email to this user with code
    - redirect activate page
    '''
    if request.method =='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']

            user=form.save(commit=False)
            user.is_active=False

            form.save()
            profile=Profile.objects.get(user__username=username)
            # sendemail
            send_mail(
                "Activate code",
                f"welcome mr {username} \n use this code {profile.code}",
                "r_mido99@yahoo.com",
                [email],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')

    else:
        form=SignupForm()

    return render(request,'accounts/signup.html',{'form':form})

def activate(request,username):
    
    '''
    - activate user
    - use this code
    - rediect login page
    '''
    profile=Profile.objects.get(user__username=username)
    if request.method=='POST':
        form=ActivateForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code==profile.code:
                profile.code=''

                user=User.objects.get(username=username)
                user.is_active=True

                user.save()
                profile.save()
                
                return redirect('/accounts/login')
    else:
        form=ActivateForm()

    return render(request,'accounts/activate.html',{'form':form})
