from django.urls import include, path
from django.contrib import admin

from theme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books_cbv/', include('books_cbv.urls', namespace='books_cbv')),
    path('books_fbv/', include('books_fbv.urls', namespace='books_fbv')),
    path('books_fbv_user/', include('books_fbv_user.urls', namespace='books_fbv_user')),
    path('planos/', include('Plan_aula.urls', namespace='Plan_aula')),
    path('docentes/', include('docentes.urls', namespace='docentes')),
    path('', views.home, name='home'),
]
