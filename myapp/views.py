from django.shortcuts import *

from myapp.forms import *

# Create your views here.
def inicio(request):
    anuncios = Anuncios.objects.all()
    return render (request, 'index.html',{"anuncios": anuncios})

def sobre(request):

    return render (request, 'sobre.html')

def detalhes(request,id):
    anuncio = Anuncios.objects.get(pk=id)
    return render (request, 'detalhes.html',{"anuncio":anuncio})

def form(request):

    return render (request, 'form.html')

def crud(request):
    form = AnunciosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    pacote = {"formAnuncio": form}
    return render(request, "create.html", pacote)