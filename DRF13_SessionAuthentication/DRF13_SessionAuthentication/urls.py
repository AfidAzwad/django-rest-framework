from django.contrib import admin
from django.urls import path, include
from SessionAuthentication import views
from rest_framework.routers import DefaultRouter

# Create Router Object
router = DefaultRouter()

# Register StudentModelViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    # to login in the API and it will create a session by default
    path('auth/', include('rest_framework.urls', namespace= 'rest_framework')),
]
