from django.urls import path, include

from . import views

app_name = 'docentes'

urlpatterns = [
  path('', views.DocenteList.as_view(), name='docente_list'),
  path('new', views.DocenteCreate.as_view(), name='docente_create'),
  path('edit/<int:pk>', views.DocenteUpdate.as_view(), name='docente_update'),
  path('delete/<int:pk>', views.DocenteDelete.as_view(), name='docente_delete'),
  path('item/', include('itemP.urls', namespace='itemP')),
]
