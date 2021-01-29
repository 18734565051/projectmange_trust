from .models import Task
from user.models import User
from django.views import View
from django.http.response import JsonResponse
from pro.utils.return_code import *
from pages.models import FileBaseInfo
from django.shortcuts import render

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
        user_id = request.POST.get('user_id')
        file_ids = request.POST.getlist('file_ids[]')
        print(user_id, file_ids)
        try:
            #  修改文档审核状态 修改审批人
            # 获取用户对象
            leader = User.objects.get(id=user_id)
            for file_id in file_ids:
                FileBaseInfo.objects.filter(id=file_id).update(trial_status='正在审核', leader=leader.username)
            return JsonResponse(code_success())
        except Exception as e:
            return JsonResponse(code_error(e))


class TaskView(View):
    def get(self, request):
        task = request.GET.get('task_id', None)
        print(task)
        if task is None:
            taskobject = Task.objects.get(id=task)
            print(taskobject)
        return render(request, 'task_list.html', context={})
