from django.urls import path

from Plan_aula import views

app_name = 'Plan_aula'

urlpatterns = [
  path('', views., name='plan_list'),
  path('new', views., name='plan_new'),
  path('edit/<int:pk>', views., name='plan_edit'),
  path('delete/<int:pk>', views., name='plan_delete'),
]