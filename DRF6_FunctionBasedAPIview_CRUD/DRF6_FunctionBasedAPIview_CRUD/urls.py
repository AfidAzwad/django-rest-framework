from django.contrib import admin
from django.urls import path
from APIview_CRUD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stapicrud/', views.student_api),
]
