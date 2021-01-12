from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
import re
from .models import User
from pro.utils.return_code import *
from pro.utils.jwts import JWT_Verify


class RegisterView(View):
    #  注册
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get('username')
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        # 判断用户名是否存在 用户名不超过5位不低于20位
        if User.objects.filter(username=username).count() > 0:
            response_data = code_user_exists()
            return JsonResponse(response_data)
        # 判断手机号的格式 是否存在
        elif not re.match(r'^1[3-9]\d{9}', mobile):
            response_data = code_mobile_fromat_No()
            return JsonResponse(response_data)
        elif User.objects.filter(mobile=mobile).count() > 0:
            response_data = code_mobile_exists()
            return JsonResponse(response_data)
        # 判断邮箱格式、是否存在
        elif User.objects.filter(email=email).count() > 0:
            response_data = code_email_exists()
            return JsonResponse(response_data)
        elif not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
            response_data = code_email_format_No()
            return JsonResponse(response_data)
        #  判断密码是否一致
        elif password != password2:
            print(password, password2)
            response_data = code_password_different()
            return JsonResponse(response_data)
        else:
            # 创建
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.mobile = mobile
            user.save()
            #  获取用户id
            user = User.objects.get(username=username)
            jwt_verify = JWT_Verify()
            # 构建payload
            payload = {
                'user_id': user.id,
                'username': username,
                'mobile': mobile
            }
            # 获取token
            token = jwt_verify.encode_token(payload)
            # 构建响应数据
            response_data = code_success()
            response_data['token'] = token
            return JsonResponse(response_data)


class LoginView(View):
    #  登陆
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = ''
            # 判断username格式
            if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', username):
                user = User.objects.get(email=username)
            if re.match(r'^1[3-9]\d{9}', username):
                user = User.objects.get(mobile=username)
            else:
                user = User.objects.get(username=username)
        except:
            response_data = code_info_No_exists()
            return JsonResponse(response_data)
        #  验证密码是否正确  如果正确 返回token 否则返回错误信息
        if user.check_password(password):
            user = User.objects.get(username=username)
            # 构建payload
            payload = {
                'user_id': user.id,
                'username': user.username,
                'mobile': user.mobile,
            }
            # 获取token
            jwt_verify = JWT_Verify()
            token = jwt_verify.encode_token(payload)
            # 构建响应数据
            response_data = code_success()
            response_data['token'] = token
            return JsonResponse(response_data)
        else:
            response_data = code_password_error()
            return JsonResponse(response_data)
