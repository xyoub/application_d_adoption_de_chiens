# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import InscriptionForm, ConnexionForm
# from .forms import ProductForm


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


@login_required
def about(request):
    return render(request,'monapplication/about.html')

def menu(request):
   # x={'name':'iliass','age':'21'}
   return render(request,'monapplication/menu.html')

def Acceuil(request):
   # x={'name':'iliass','age':'21'}
   return render(request,'monapplication/Acceuil.html')



# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('products')
#     else:
#         form = ProductForm()

#     return render(request, 'add_product.html', {'form': form})
