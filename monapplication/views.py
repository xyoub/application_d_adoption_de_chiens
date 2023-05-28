# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import InscriptionForm, ConnexionForm 
# from .forms import ProductForm
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContactForm


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Change this line
            user.set_password(form.cleaned_data['password'])  # Add this line
            user.save()  # Add this line
            login(request, user)
            return redirect('/menu/')
    else:
        form = InscriptionForm()
    return render(request, 'monapplication/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
            form = ConnexionForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/menu/')  # Replace 'dashboard' with your desired URL name or path
    else:
        form = ConnexionForm()
        
    return render(request,'monapplication/connexion.html', {'form': form})
   
@login_required
def accueil(request):
    return render(request,'monapplication/accueil.html')



def deconnexion(request):
    logout(request)
    return redirect('/connexion/')


def home(request):
    
    return render(request,'monapplication/home.html')

  
@login_required
def about(request):
    return render(request,'monapplication/about.html')

@login_required
def menu(request):
   # x={'name':'iliass','age':'21'}
   return render(request,'monapplication/menu.html')


def Acceuil(request):
   # x={'name':'iliass','age':'21'}
   return render(request,'monapplication/Acceuil.html')

def mesannonces(request):
   # x={'name':'iliass','age':'21'}
   return render(request,'monapplication/mesannonces.html')

def annonces(request):
   return render(request,'monapplication/annonces.html')

def contact(request):
   return render(request,'monapplication/contact.html')
#-------------------------------------------------------------------
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_message = EmailMessage(
                subject,
                "Message de {name} <{email}> :\n\n{message}".format(name=name, email=email, message=message),
                email,
                ["boujemaoui.ayoub654@gmail.com"],  # changez ceci à votre propre email
            )
            try:
                email_message.send()
                messages.success(request, 'Votre message a été envoyé avec succès. Nous vous répondrons bientôt.')
            except:
                messages.error(request, 'Une erreur est survenue lors de l\'envoi du message. Veuillez réessayer plus tard.')

        return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

#------------------------------------------------------------------



# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('products')
#     else:
#         form = ProductForm()

#     return render(request, 'add_product.html', {'form': form})
