from django.contrib import admin
from django.urls import path
from APIview import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stapiview/', views.Hello_world),
]
