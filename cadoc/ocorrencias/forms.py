from django import forms
# from django.forms import modelformset_factory
from .models import Ocorrencia,TipoOcorrencia,Endereco,Solicitante

class OcorrenciaForm(forms.ModelForm):
    # def __init__(self,*args,**kwargs):
    #     super(OcorrenciaForm,self).__init__(*args,*kwargs)
    class Meta:
        model = Ocorrencia
        fields = [ 'motivo', 'descricao']


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua','cep','numero','bairro','cidade']

class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ("__all__")
