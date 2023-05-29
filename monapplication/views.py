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
    return redirect('/Acceuil/')


def home(request):
    
    return render(request,'monapplication/Acceuil.html')

  
@login_required
def about(request):
    return render(request,'monapplication/about.html')

def menu(request):
   # x={'name':'iliass','age':'21'}
   return render(request,'monapplication/menu.html')

def Acceuil(request):
   # x={'name':'iliass','age':'21'}
   return render(request,'monapplication/Acceuil.html')



def Ajouterannonce(request):
    return render (request, 'monapplication/Ajouterannonce.html')

def annonces(request):
    return render (request, 'monapplication/annonces.html')




def Adds(request):
   AN =Annonce.objects.all()
   context={'Annonces': AN}
     # Retrieve all  objects from the database
   return render(request, 'monapplication/annonces.html', context)


# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('products')
#     else:
#         form = ProductForm()

#     return render(request, 'add_product.html', {'form': form})



from .models import Annonce
from django.contrib import messages

def Ajouterann(request):
    if request.method == "POST":
        prod = Annonce()
        if request.user.is_authenticated:
         prod.user=request.user
         prod.nomanimal= request.POST.get('animalname')
         prod.age= request.POST.get('age')
         prod.race = request.POST.get('race')
         prod.type = request.POST.get('type')
         prod.sex = request.POST.get('sex')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image1']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return redirect('mesannonces')
    return render(request, 'monapplication/Ajouterannonce.html')

def mesannonces(request):
    if request.user.is_authenticated:
        annonce = Annonce.objects.filter(user=request.user)
      
        context = {'adds': annonce}
        return render(request, 'monapplication/mesannonces.html', context)
    

def modifier(request,aid):
   AN  = Annonce.objects.get(id=aid)
   context={'a': AN}
    # Retrieve all  objects from the database
   return render(request, 'monapplication/Modifier.html',context)


def Modifier(request, aid):
    # Fetch the specific Annonce object to modify
    annonce = Annonce.objects.get(id=aid)

    if request.method == 'POST':
        # Retrieve the modified data from the form
        nom_animal = request.POST['animalname']
        type  = request.POST['type']
        race = request.POST['race']
        age = int(request.POST['age'])
        sex = request.POST['sex']

        # Update the fields of the Annonce object
        annonce.nomanimal = nom_animal
        annonce.type= type
        annonce.race = race
        annonce.age = age
        annonce.sex = sex

        # Save the modified object
        annonce.save()

        # Redirect to a success page or another view
        return redirect('mesannonces')
    

    
def details(request, id):
    # Retrieve the Annonce object with related user information
    annonce = Annonce.objects.select_related('user').get(id=id)

    context = {
        'an': annonce,
        # Other context data
    }

    return render(request, 'monapplication/details.html', context)


def delete(request,rowid):
    # Retrieve the object you want to delete
   try:
    Annonce.objects.get(id=rowid).delete()


    return redirect('mesannonces')
   except Annonce.DoesNotExist:
        # Handle the case where the Annonce object with the provided id does not exist
        # Redirect to an error page or display an error message
        return redirect('mesannonces')
   


   