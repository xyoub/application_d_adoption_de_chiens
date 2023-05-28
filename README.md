# application_d_adoption_de_chiens_2023
explication pour le code de contact..

```python
from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm

```

- La première ligne importe la fonction `render` du module `django.shortcuts` qui est utilisée pour afficher les modèles HTML.
- La deuxième ligne importe la classe `EmailMessage` du module `django.core.mail` qui est utilisée pour envoyer des messages électroniques.
- La troisième ligne importe la classe `ContactForm` du fichier `forms.py`.

```
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

```

- Ce bloc de code définit une fonction nommée `contact_view` qui gère la soumission du formulaire.
- Il vérifie si la méthode de la requête est `POST`, ce qui signifie que l'utilisateur a soumis le formulaire.
- Il initialise ensuite une nouvelle instance de `ContactForm` avec les données soumises par l'utilisateur.
- Il vérifie si le formulaire est valide en appelant la méthode `is_valid()`. Si le formulaire est valide, il extrait le nom, l'e-mail et le message des données nettoyées du formulaire.

```
            email = EmailMessage(
                "Nouveau message de: {}".format(name),
                message,
                "{name} <{email}>".format(name=name, email=email),
                ["votre_email@exemple.com"],  # changez ceci à votre propre email
            )
            email.send()

```

- Ce bloc de code crée une instance de la classe `EmailMessage` et définit les champs du sujet, du message, de l'expéditeur et du destinataire.
- La méthode `send()` est ensuite appelée pour envoyer le message électronique.

```
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

```

- Si le formulaire est soumis avec succès et que le message électronique est envoyé, la fonction renvoie un message de réussite en affichant le modèle `contact_success.html`.
- Si la méthode de la requête n'est pas `POST`, cela signifie que l'utilisateur accède à la page pour la première fois et la fonction affiche le modèle `contact.html` avec une instance de formulaire vide.