from django.shortcuts import *

from myapp.forms import *

# Create your views here.
def inicio(request):
    anuncios = Anuncios.objects.all()
    return render (request, 'index.html',{"anuncios": anuncios})

def listagem(request):
    lista = Anuncios.objects.all()
    return render(request,'listagem.html', {'lista':lista})

def sobre(request):

    return render (request, 'sobre.html')

def busca(request):
    return render (request, 'busca.html') 

def resbusca(request):
    buscar = request.GET.get('busca')
    res= Anuncios.objects.filter(titulo__icontains=buscar)
    return render(request, 'res-busca.html', {"anuncios":res})

def detalhes(request,id):
    anuncio = Anuncios.objects.get(pk=id)
    return render (request, 'detalhes.html',{"anuncio":anuncio})

def form(request):

    return render (request, 'form.html')

def crud(request):
    if request.user.is_authenticated == False:
        return redirect("/account/login")
    form = AnunciosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    pacote = {"formAnuncio": form}
    return render(request, "create.html", pacote)

def update(request, id):
    if request.user.is_authenticated == False:
        return redirect("/account/login")
    anuncio = Anuncios.objects.get(pk=id)
    formAnuncio = AnunciosForm(request.POST or None, instance=anuncio)
    if formAnuncio.is_valid():
        formAnuncio.save()
        return redirect("/") 
    return render(request, "create.html", {"formAnuncio": formAnuncio})

def delete(request, id):
    if request.user.is_authenticated == False:
        return redirect("/account/login")
    anuncio = Anuncios.objects.get(pk=id)
    anuncio.delete()
    return redirect("/")