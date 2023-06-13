from django.urls import path
from .views import cookies_sesion, cookie_delete, create_sesion, access_sesion, delete_sesion

app_name = 'sesiones_app'

urlpatterns = [
    path('testcookie/', cookies_sesion),
    path('deletecookie/', cookie_delete),
    path('create/', create_sesion),
    path('access/', access_sesion),
    path('delete/', delete_sesion),

]