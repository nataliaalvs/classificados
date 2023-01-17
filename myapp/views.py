from django.shortcuts import *

from myapp.forms import *

# Create your views here.
def inicio(request):

    return render (request, 'index.html')

def sobre(request):

    return render (request, 'sobre.html')

def detalhes(request):

    return render (request, 'detalhes.html')

def form(request):

    return render (request, 'form.html')

def crud(request):

    return render (request, 'create.html')

def createAnuncio(request):
    form = AnunciosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    pacote = {"formAnuncio": form}
    return render(request, "createAnuncio.html", pacote)