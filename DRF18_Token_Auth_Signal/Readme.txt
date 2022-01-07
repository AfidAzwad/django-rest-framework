To generate token for users :

1. using Admin Application - through Admin panel
2. Using Django command line - py manage.py drf_create_token username
3. By exposing an API endpoint - http POST http://127.0.0.1:8000/gettoken/ username="admin" password="admin"
4. Using Signals - token will be generated automatically when an user is created


**GET request with token :
http http://127.0.0.1:8000/studentapi/ 
'Authorization:Token c705e75b21acaabe5233461e5e9d71ad3b4bc3f4'

**POST request with token :
http -f POST http://127.0.0.1:8000/studentapi/ name=Afid roll=22 city=dhaka 
 'Authorization:Token c705e75b21acaabe5233461e5e9d71ad3b4bc3f4'
