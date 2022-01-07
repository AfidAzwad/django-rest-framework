from django.contrib import admin
from django.urls import path
from CRUD_ClassBased import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentcrud/', views.StudentApi.as_view() ),
]
