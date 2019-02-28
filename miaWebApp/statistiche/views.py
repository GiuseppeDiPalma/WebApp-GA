from django.shortcuts import render

# Create your views here.

def one_page(request):
    return render(request, "firstPage.html")

#creare una nuova funzione def funzione che risponde a quella chiamata post  https://docs.djangoproject.com/en/2.1/ref/request-response/
#gestire con richieste di uno due secondi(vedere node js)
#richiamo qui la function della mia libreria per elaborare i dati con il mio codice python

#la funzione django che gestisce la view deve ritornare un json https://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python

#richiesta post all'endpoint scelto in urls, https://api.jquery.com/jquery.post/ in loop ogni tot di tempo.