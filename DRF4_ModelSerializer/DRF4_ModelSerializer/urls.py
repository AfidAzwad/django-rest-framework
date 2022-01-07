from django.contrib import admin
from django.urls import path
from modelSerializer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentcrud/', views.StudentApi.as_view()),
]
