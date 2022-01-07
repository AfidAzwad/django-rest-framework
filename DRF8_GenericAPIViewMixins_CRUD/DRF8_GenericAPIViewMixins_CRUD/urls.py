from django.contrib import admin
from django.urls import path
from GenericAPIViewMixin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stapicrud/', views.StudentListCreate.as_view()),
    path('stapicrud/<int:pk>', views.StudentRUD.as_view()),

]
