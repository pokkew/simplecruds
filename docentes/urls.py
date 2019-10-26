from django.urls import path, include

from docentes import views

app_name = 'docentes'

urlpatterns = [
  path('', views.docente_list, name='docentes_list'),
  #path('new', views.PlanA_create, name='plan_new'),
  #path('edit/<int:pk>', views.PlanA_update, name='plan_edit'),
  #path('delete/<int:pk>', views.PlanA_delete, name='plan_delete'),
  #path('item/', include('itemP.urls', namespace='itemP')),
]
