This project showing from Rest Framework:

1. Basic Authentication - from rest_framework.authentication import BasicAuthentication
2. Permission - from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
3. Globally set the Authentication - declare in settings.py
   example : REST_FRAMEWORK = { 
                'DEFAULT_AUTHENTICATED_CLASSES':['rest_framework.authentication.BasicAuthentication'],
                'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated'],
                }
