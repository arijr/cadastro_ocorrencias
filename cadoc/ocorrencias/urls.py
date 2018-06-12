from django.urls import path
from .views import *

#TODO: limpar resto de codigo
urlpatterns = [
    path('', OcorrenciaListView.as_view(),name='occ_list'),
    path('occ_detail/<int:pk>/',OcorrenciaUpdateView.as_view(), name='occ_detail'),
    path('new', OcorrenciaCreateView.as_view(), name='occ_create'),
    path('delete/<int:pk>',OcorrenciaDeleteView.as_view(),name='occ_delete'),
    # path('',list_occ, name='list_occ'),
    # path('update/<int:id>/', update_occ, name='update_occ'),
    # path('delete/<int:id>/', delete_occ, name='delete_occ'),

    ]
