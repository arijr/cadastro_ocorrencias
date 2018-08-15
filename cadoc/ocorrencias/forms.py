from django import forms

from .models import Ocorrencia,TipoOcorrencia,Endereco,Solicitante

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        # formfield_callback = Endereco
        fields = [ 'motivo', 'descricao','tipo']
        # exclude = ('endereco','solicitante')

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua','cep','numero','bairro','cidade']


class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ("__all__")
