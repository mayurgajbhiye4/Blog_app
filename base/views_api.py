from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data 

            if data.get('username') is None:
                response['message'] = 'Key username not found'
                raise Exception('Key username not found')
            
            if data.get('password') is None:
                response['message'] = 'Key password not found'
                raise Exception('Key password not found')
            
            check_user = User.objects.filter(username=data.get('username')).first()

            if not check_user:
                response['message'] = 'Invalid Username, User not found'
                raise Exception('Invalid Username, User not found')
            
            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            if user_obj:
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'Invalid Password'
                raise Exception('Invalid Password')       
        
        except Exception as e:
            print(e)

        return Response(response)
    

class RegisterView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data 

            if data.get('username') is None:
                response['message'] = 'Username required'
                raise Exception('Username required')
            
            if data.get('password') is None:
                response['message'] = 'Password required'
                raise Exception('Password required')
            
            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user:
                response['message'] = 'Username already taken'
                raise Exception('Username already taken')
            
            user_obj = User.objects.create(username= data.get('username'))
            user_obj.set_password(data.get('password')) 
            user_obj.save()    
            response['message'] = 'Account successfully created' 
            response['status'] = 200
        
        except Exception as e:
            print(e)

        return Response(response)