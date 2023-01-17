from django.db import models

# Create your models here.
class Anuncios(models.Model):
    categoria_choice = (
        ("EMP","Empregos"),
        ("IMO","Imóveis"),
        ("AUT","Automóveis"),
        ("SER","Serviços"),
        ("PER","Perdidos"),
        ("OUT","Outros"),
    )
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    anuncio = models.CharField(max_length=400)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    responsavel = models.CharField(max_length=40)
    celular = models.IntegerField()
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=80)
    categoria = models.CharField(max_length=3, choices=categoria_choice)