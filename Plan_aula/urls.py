from django.urls import path

from Plan_aula import views

app_name = 'Plan_aula'

urlpatterns = [
  path('', views.PlanA_list, name='plan_list'),
  path('new', views.PlanA_create, name='plan_new'),
  path('edit/<int:pk>', views.PlanA_update, name='plan_edit'),
  path('delete/<int:pk>', views.PlanA_delete, name='plan_delete'),
]