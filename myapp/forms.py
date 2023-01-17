from django.forms import ModelForm
from myapp.models import*

class AnunciosForm(ModelForm):
    class Meta:
        model = Anuncios
        fields = ["titulo", "anuncio", "valor", "responsavel", "celular", "cidade", "endereco", "categoria"]