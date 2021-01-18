from user.models import User
from django.views import View
from django.http.response import JsonResponse
from pro.utils.return_code import *

'''
审核文档
'''


class Approval_File(View):
    def get(self, request):
        # 返回有权限的管理员名单
        try:
            user = [{manage.id: manage.username} for manage in User.objects.filter(is_superuser__exact=1)]
            code = code_success()
            code['data'] = user
            return JsonResponse(code)
        except Exception as e:
            return JsonResponse(code_error(e))

    def post(self, request):
        pass
