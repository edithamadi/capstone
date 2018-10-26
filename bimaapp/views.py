from django.shortcuts import render
from django.http  import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import *
from django.contrib import messages

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


@login_required(login_url='/login')
def details(request):
   profile =Profile.objects.filter(user=request.user.id)
   lifeassured =Lifeassured.objects.filter()
   bankers_order = Bankers_Order.objects.filter()
   proposer =Proposer.objects.filter()
   address =Address.objects.filter()
   occupation =Occupation.objects.filter()
   premiumpaymethod =Premiumpaymethod.objects.filter()
   context = {"lifeassured":lifeassured,"proposer":proposer,"address":address,"occupation":occupation,"premiumpaymethod":premiumpaymethod,"bankers_order":bankers_order, "profile": profile}
   return render(request, 'details.html', context)

def images(request):
    images = Image.objects.filter()
    print(images)
    return render(request, 'welcome.html', {"images":images})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Bima Assurance account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login to your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    profile_details = get_user_profile(cls ,username)

    return render(request,'profile.html',locals())

def edit_profile(request):

    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/uprofile.html', context)



@login_required(login_url='/login')
def new_proposer(request):
   current_user = request.user
   if request.method == 'POST':
       form = ProposerForm(request.POST, request.FILES)
       if form.is_valid():
           proposer = form.save(commit=False)
           proposer.user = current_user
           proposer.save()
       return redirect('lifeassured')

   else:
       form = ProposerForm()
   return render(request, 'application_form.html', {"form": form})

@login_required(login_url='/login')
def new_lifeassured(request):
   current_user = request.user
   if request.method == 'POST':
       form = LifeassuredForm(request.POST, request.FILES)
       if form.is_valid():
           lifeassured = form.save(commit=False)
           lifeassured.user = current_user
           lifeassured.save()
       return redirect('address')

   else:
       form = LifeassuredForm()
   return render(request, 'lifeassured_form.html', {"form": form})

@login_required(login_url='/login')
def new_address(request):
   current_user = request.user
   if request.method == 'POST':
       form = AddressForm(request.POST, request.FILES)
       if form.is_valid():
           address = form.save(commit=False)
           address.user = current_user
           address.save()
       return redirect('occupation')

   else:
       form = AddressForm()
   return render(request, 'address_form.html', {"form": form})

@login_required(login_url='/login')
def new_occupation(request):
   current_user = request.user
   if request.method == 'POST':
       form = OccupationForm(request.POST, request.FILES)
       if form.is_valid():
           occupation = form.save(commit=False)
           occupation.user = current_user
           occupation.save()
       return redirect('premiumpaymethod')

   else:
       form = OccupationForm()
   return render(request, 'occupation_form.html', {"form": form})

@login_required(login_url='/login')
def new_premiumpaymethod(request):
   current_user = request.user
   if request.method == 'POST':
       form = PremiumpaymethodForm(request.POST, request.FILES)
       if form.is_valid():
           premiumpaymethod = form.save(commit=False)
           premiumpaymethod.user = current_user
           premiumpaymethod.save()
       return redirect('bankers_order')

   else:
       form = PremiumpaymethodForm()
   return render(request, 'premiumpaymethod_form.html', {"form": form})

@login_required(login_url='/login')
def new_bankers_order(request):
   current_user = request.user
   if request.method == 'POST':
       form = Bankers_OrderForm(request.POST, request.FILES)
       if form.is_valid():
           bankers_order = form.save(commit=False)
           bankers_order.user = current_user
           bankers_order.save()
       return redirect('welcome')

   else:
       form = Bankers_OrderForm()
   return render(request, 'bankers_order_form.html', {"form": form})