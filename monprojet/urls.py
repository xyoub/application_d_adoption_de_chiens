"""
URL configuration for monprojet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from monapplication import views



               

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('about/', views.about, name='about'),
    path('menu/',views.menu, name='menu'),
    path('Acceuil/',views.Acceuil,name='Acceuil'),
    path('mesannonces/',views.mesannonces,name='mesannonces'),
    path('home/',views.home,name='home'),
    path('Ajouterannonce/',views.Ajouterannonce,name='Ajouterannonce'), 
    path('Ajouteran/',views.Ajouterann,name='Ajouterann'),  
    path('modifier/<int:aid>',views.modifier,name='modifier'), 
    path('Modifier/<int:aid>',views.Modifier,name='Modifier'),
    path('details/<int:id>',views.details,name='details'), 
    path('delete/<int:rowid>',views.delete, name='delete'),  
    path('Adds/', views.Adds, name='Adds'),

]



from django.conf import settings

from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)