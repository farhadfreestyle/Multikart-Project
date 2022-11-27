from urllib import request
from django.shortcuts import render, redirect
from users.models import User
from users.forms import RegsiterForm, LoginForm
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from users.services.users import create_user_if_not_exist
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from verify_email.email_handler import send_verification_email


oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)



def login_auth(request):
    print(settings.AUTH0_CLIENT_SECRET)
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("users:auth_callback"))
    )


def auth_callback(request:HttpRequest)->HttpResponse:
    user: dict = oauth.auth0.authorize_access_token(request)
    print(user)
    if 'email' in user["userinfo"]:
        
        create_user_if_not_exist(
            first_name=user["userinfo"]["given_name"],
            last_name=user["userinfo"]["family_name"],
            email=user["userinfo"]["email"]
        )
        email = user["userinfo"]["email"]
    else:
        create_user_if_not_exist(
            first_name=user["userinfo"]["given_name"],
            last_name=user["userinfo"]["family_name"],
            email= user["userinfo"]["given_name"] + '@' + user["userinfo"]["family_name"] + user["userinfo"]["picture"]
        )

        email = user["userinfo"]["given_name"] + '@' + user["userinfo"]["family_name"] + user["userinfo"]["picture"]

    
    request.session["user"] = user
    login(request, User.objects.get(email = email))
    return redirect(request.build_absolute_uri(reverse("core:index")))



def logout_auth(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("core:index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )


            

def register(request):
    if request.method == 'POST':
        form = RegsiterForm(request.POST)
        
        if form.is_valid():
            
            inactive_user = send_verification_email(request, form)
            user = User.objects.filter(email=form.cleaned_data['email'])
            user.username = form.cleaned_data['email']
            
            return redirect('users:login')

        
    else:
        form = RegsiterForm()
    return render(request,'users/register.html', {'form':form})
    

def login_user(request):
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form)
            
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email = email)
            if not User.objects.filter(email = email).exists():
                messages.error(request, "You do not have an account with this email. Try to create account!")

                
            
            elif User.objects.get(email = email).check_password(password):
                user = User.objects.get(email = email)
                login(request, User.objects.get(email = email))
                
                return redirect('core:index')
            else :
                 messages.error(request, "Wrong password. Try again!")
                 

    form = LoginForm()
    user = User

    return render(request, 'users/login.html', {"form":form, 'user':user})



def password_reset_request(request):
   
	if request.method == "POST":
        
		password_reset_form = PasswordResetForm(request.POST)
       
		if password_reset_form.is_valid():
            
			data = password_reset_form.cleaned_data['email']
            
			associated_users = User.objects.filter(email=data)
            
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "users/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email])
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("users:password_reset_done")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="users/forget_pwd.html", context={"password_reset_form":password_reset_form})

@login_required(login_url='users:login')
def logout_user(request):
    logout(request)
    return redirect("core:index")


@login_required(login_url='users:login')
def wishlist(request):
    return render(request, 'users/wishlist.html')



@login_required(login_url='users:login')
def profile(request):
    
    return render(request, 'users/profile.html')             

       
