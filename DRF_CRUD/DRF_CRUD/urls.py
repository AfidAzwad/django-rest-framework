from django.contrib import admin
from django.urls import path
from CRUD import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentcrud/', views.student_api),
]
