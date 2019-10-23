from django.urls import path, include

from itemP import views

app_name = 'itemP'

urlpatterns = [
  path('<int:pk>', views.itemP_list, name='itemp_list'),
  #path('new', views.itemP_create, name='itemP_new'),
  #path('edit/<int:pk>', views.itemP_update, name='itemP_edit'),
  #path('delete/<int:pk>', views.itemP_delete, name='itemP_delete'),
]