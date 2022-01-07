from django.contrib import admin
from django.urls import path
from ConcreteViewClass import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stapicrud/', views.StudentLC.as_view()),
    path('stapicrud/<int:pk>', views.StudentRUD.as_view()),
]
