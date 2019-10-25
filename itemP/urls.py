from django.urls import path, include

from itemP import views

app_name = 'itemP'

urlpatterns = [
  path('<int:pk>', views.itemP_list, name='itemp_list'),#pk do plano de aula
  path('new/<int:pk>', views.itemP_create, name='itemp_new'), #pk do plano de aula
  path('edit/<int:pkI>', views.itemP_update, name='itemp_edit'), #pk do item de plano de aula
  #path('delete/<int:pk>', views.itemP_delete, name='itemP_delete'),
]
