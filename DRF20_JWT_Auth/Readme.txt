JWT - JSON Web Token

It's a third party web token package. It will not create any table in database like buit-in Token Authentication.
JWT Authentication doesn't need to use a database to validate a token.

To use Simple JWT :
 pip install djangorestframework-simplejwt

Token parts : Header, Payload and Signature

access token lifetime : 5 minutes
refresh token lifetime : 1 day

Get : 
http POST http://127.0.0.1:8000/gettoken/ username="admin" password="admin"

Verify :
http POST http://127.0.0.1:8000/verifytoken/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQxNTM1ODYwE2NDE1MzU1NjAsImp0aSI6IjZlZGEzNjNiYjdlZjRiYzJiNTVlU4YzljIiwidXNlcl9pZCI6MX0.eeQMF0_DWNizCrtCWOIJZnaaJqDsq8fHI"

Refresh :
http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1Nilbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MTYyMTk2MCwiaxNTM1NTYwLCJqdGkiOiIxYzM3N2FlNzZmYzc0N2RhYjUyNTEyY3MiIsInVzZXJfaWQiOjF9.P_vfHBsZO-890SZloN0bpu5LSfEIJ-vPo" 