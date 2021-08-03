from django.contrib import admin
from django.urls import path, include
from calc import views as C

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', C.home, name='home'),
]
