To generate token for users :

1. using Admin Application - through Admin panel
2. Using Django command line - py manage.py drf_create_token username
3. By exposing an API endpoint - http POST http://127.0.0.1:8000/gettoken/ username="admin" password="admin"
    needed : pip install httpie
4. Using Signals - token will be generated automatically when an user is created