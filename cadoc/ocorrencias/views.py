from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.views import generic
# from django.forms import modelformset_factory
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.views.generic.list import ListView

from .models import *
from .forms import *



class OcorrenciaListView(ListView):
    model = Ocorrencia

class OcorrenciaCreateView(CreateView):

    def get_context_data(self, **kwargs):
        context  = super(OcorrenciaCreateView,self).get_context_data(**kwargs)
        if self.request.POST:
            context['endereco_form'] = EnderecoForm(self.request.POST)
            context['requerente_form'] = SolicitanteForm(self.request.POST)
            # context['ocorrencia_form'] = OcorrenciaForm(self.request.POST)

        else:
            context['endereco_form'] = EnderecoForm()
            context['requerente_form'] = SolicitanteForm()
            # context['ocorrencia_form'] = OcorrenciaForm()

        return context

    def form_valid(self,form):

        self.object = form.save(commit= False)
        context = self.get_context_data()
        FormEndereco = context['endereco_form']
        FormSolicitante = context['requerente_form']
        # FormOcorrencia = context['ocorrencia_form']
        # if FormEndereco.is_valid() and FormSolicitante.is_valid():

        if FormEndereco.is_valid() :
            endereco = FormEndereco.save()
            self.object.endereco = endereco

        if FormSolicitante.is_valid():
            solicitante = FormSolicitante.save()
            self.object.solicitante = solicitante
        # if FormOcorrencia.is_valid():
            # ocorrencia = FormOcorrencia.save(commit=False)
            # ocorrencia.endereco = endereco
            # ocorrencia.solicitante = solicitante
            # self.object.endereco = endereco

        # ocorrencia.save()
        # self.object.Ocorrencia = ocorrencia
        # self.object.save()

        return super(OcorrenciaCreateView,self).form_valid(form)

    model = Ocorrencia
    # fields = ['motivo', 'descricao']
    get_success_url = OcorrenciaListView
    form_class = OcorrenciaForm

class OcorrenciaUpdateView(UpdateView):
    model = Ocorrencia
    fields = '__all__'
    template_name_suffix = '_form'

class OcorrenciaDeleteView(DeleteView):
    model = Ocorrencia
    success_url = reverse_lazy('occ_list')

#TODO: limpar rastro de codigo antigo e de teste

# Create your views here.
# def list_occ(request):
#     ocorrencias = Ocorrencia.objects.all()
#     enderecos = Endereco.objects.all()
#     solicitantes = Solicitante.objects.all()
#     return render(request, 'index.html',{'ocorrencias': ocorrencias, 'enderecos': enderecos, 'solicitantes': solicitantes})

    # template_name = 'ocorrencias-form.html'
    # form_class = OcorrenciaForm
    # success_url = ''
    #
    # def form_valid(self,form):
    #     form.save()
    #     return super().form_valid(form)
# def create_occ(request):
#     formset = OcorrenciaForm(request.POST or None)
#     if request.method == 'POST':
#         if formset.is_valid():
#
#             formset.save()
#             return redirect('list_occ')
#     else:
#         formset = OcorrenciaForm()
#
#     return render(request, 'ocorrencias-form.html',{'formset': formset})
    # EndForm  = EnderecoForm(request.POST or None)
    # OccForm = OcorrenciaForm(request.POST or None)
#     OccFormSet = OcorrenciaFormSet()
#     # SolForm = SolicitanteForm(request.POST or None)
# # EndForm.is_valid() and SolForm.is_valid() and
#     if request.method == 'POST':
#         OccForm = OccFormSet(request.POST)
#         if OccForm.is_valid():
#
#             # EndForm.save()
#             # SolForm.save()
#             OccForm.save()
#
#             return redirect('list_occ')
#         else:
#             OccForm = OccFormSet
# # ,'EndForm':EndForm,'SolForm': SolForm
#     return render(request, 'ocorrencias-form.html',{'OccForm': OccForm})

# def update_occ(request, id):
#     ocorrencia = Ocorrencia.objects.get(id=id)
#     OccForm = OcorrenciaForm(request.POST or None, instance=ocorrencia)
#     EndForm = EnderecoForm(request.POST or None, instance=ocorrencia.endereco)
#
#     if OccForm.is_valid() and EndForm.is_valid():
#         OccForm.save()
#         EndForm.save()
#         return redirect('list_occ')
#
#     return render(request, 'ocorrencias-form.html',{'OccForm': OccForm, 'EndForm': EndForm, 'ocorrencia': ocorrencia})
#
# def delete_occ(request, id):
#     ocorrencia = Ocorrencia.objects.get(id=id)
#
#     if request.method == 'POST':
#         ocorrencia.delete()
#         return redirect('list_occ')
#
#     return render(request, 'occ-delete-confirm.html', {'ocorrencia': ocorrencia})
