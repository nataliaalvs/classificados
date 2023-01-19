from django.forms import ModelForm
from myapp.models import*

class AnunciosForm(ModelForm):
    class Meta:
        model = Anuncios
        fields = ["titulo", "anuncio", "valor", "responsavel", "celular", "cidade", "endereco", "categoria"]
        labels = {
            "titulo": "Nome do classificado",
            "anuncio": "Anúncio do classificado",
            "valor":"Valor",
            "responsavel": "Responsavel",
            "celular": "Celular",
            "cidade": "Cidade",
            "endereco": "Endereço",
            "categoria": "Categoria",
        }