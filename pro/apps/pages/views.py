from django.shortcuts import render
from django.views.generic import View
from pro.utils.jwts import JWT_Verify
from .models import *
from django.http import JsonResponse
from pro.utils.return_code import *
from user.models import User
import json
from django.core.serializers import serialize
from django.http import QueryDict


class IndexView(View):
    #  首页
    def get(self, request):
        token = request.GET.get("token")
        if not token:
            return render(request, 'login.html', code_NO_token())
        jwt_verify = JWT_Verify()
        # 验证token 是否过期 如果过期返回登陆页 else: 返回页面
        verify_result = jwt_verify.render_page(request, token)
        if verify_result:
            #  获取paylaod中用户名密码
            payload = jwt_verify.decode_token(token)
            # 获取当前项目
            # 构建返回项目数据 默认最新五条
            result_queryset = ProjectBaseInfo.objects.filter(is_delete=0).order_by(
                '-update_time')[:5]
            #  queryset序列化输出
            result_json = serialize('json', result_queryset)
            result_dicts = json.loads(result_json)
            for index, result_dict in enumerate(result_dicts):
                user_id = result_dict['fields']['leader']
                user = User.objects.filter(id=user_id)[0]
                result_dicts[index]['fields']['leader'] = user.username
                result_dicts[index]['fields']['status'] = result_queryset[index].status
            payload['data'] = result_dicts
            payload['token'] = token
            # 获取用户组
            user = User.objects.get(username=payload['payload']['username'])
            group_names = ''
            if user.groups.count() != 0:
                for group_name in user.groups.all():
                    group_names += '%s' % group_name + '、'
            else:
                group_names = "NONE"
            payload['groups'] = group_names
            #  输出文档信息
            # 判断如果是管理员 返回
            if user.is_superuser or user.is_staff:
                return render(request, "index_a.html", context=payload)
            else:
                return render(request, "index.html", context=payload)



class ProjectView(View):
    # 项目视图创建查询修改删除
    def get(self, request):
        name = request.GET.get("name")
        leader = request.GET.get("leader")
        status = request.GET.get("status")
        style = request.GET.get("style")
        create_time = request.GET.get("create_time", None)
        update_time = request.GET.get("update_time", None)
        content = {}
        if name:
            content['name__contains'] = name
        if leader:
            content['leader__username__contains'] = leader
        if status:
            content['status__name'] = status
        if style:
            content['style__contains'] = style
        if create_time:
            content['create_time__gte'] = create_time
        if update_time:
            content['update_time__lte'] = update_time
        content['is_delete'] = 0
        results = ProjectBaseInfo.objects.filter(**content)
        #  queryset序列化输出 构建返回成功数据 {code: 100, msg: "success", data: [{},{}]}
        result_json = serialize('json', results)
        result_dicts = json.loads(result_json)
        for index, result_dict in enumerate(result_dicts):
            user_id = result_dict['fields']['leader']
            user = User.objects.filter(id=user_id)[0]
            result_dicts[index]['fields']['leader'] = user.username
            result_dicts[index]['fields']['status'] = results[index].status.name
        response_data = code_success()
        response_data['data'] = result_dicts
        return JsonResponse(response_data)

    def post(self, request):
        project_name = request.POST.get('project_name')
        project_style = request.POST.get('project_style')
        token = request.POST.get('token')
        # 调用render_page()验证 jwt有效性
        jwt_verify = JWT_Verify()
        verify_result = jwt_verify.render_page(request, token)
        user_id = jwt_verify.decode_token(token).get('payload').get('user_id')
        if verify_result:
            try:
                # 获取当前user对象
                user = User.objects.get(id=user_id)
                # 判断项目名称是否存在
                if not ProjectBaseInfo.objects.filter(name=project_name, is_delete=0).count() > 0:
                    ProObject = ProjectBaseInfo()
                    ProObject.name = project_name
                    ProObject.style = project_style
                    ProObject.status = ProjectCategory.objects.get(name='项目获得')
                    ProObject.leader = user
                    ProObject.save()
                else:
                    return JsonResponse(code_porject_name_exists())

                # 构建返回项目数据 默认最新五条
                result_queryset = ProjectBaseInfo.objects.filter(is_delete=0).order_by(
                    '-update_time')[:5]
                #  queryset序列化输出 构建返回成功数据 {code: 100, msg: "success", data: [{},{}]}
                result_json = serialize('json', result_queryset)
                result_dicts = json.loads(result_json)
                for index, result_dict in enumerate(result_dicts):
                    user_id = result_dict['fields']['leader']
                    user = User.objects.filter(id=user_id)[0]
                    result_dicts[index]['fields']['leader'] = user.username
                    result_dicts[index]['fields']['status'] = result_queryset[index].status
                response_data = code_success()
                response_data['data'] = result_dicts
                return JsonResponse(response_data)
            except Exception as e:
                return JsonResponse(code_error(str(e)))

    def put(self, request):
        querydict_request_data = QueryDict(request.body)
        project_id = querydict_request_data.get("project_id")
        modalPutProjectName = querydict_request_data.get('modalPutProjectName')
        modalPutProjectStyle = querydict_request_data.get('modalPutProjectStyle')
        modalPutProjectStatus = querydict_request_data.get('modalPutProjectStatus')
        modalPutProjectLeader = querydict_request_data.get('modalPutProjectLeader')
        #  判断项目是否存在
        if ProjectBaseInfo.objects.filter(name=modalPutProjectName).count() > 0:
            return JsonResponse(code_porject_name_exists())
        else:
            #  判断用户名是否存在
            if not User.objects.filter(username=modalPutProjectLeader).exists():
                return JsonResponse(code_user_No_exists())
            else:
                # 进行项目状态判断 项目状态必须拥有几个文档
                # 更新
                try:
                    ProjectBaseInfo.objects.filter(id=project_id).update(
                        name=modalPutProjectName,
                        status=ProjectCategory.objects.get(name=modalPutProjectStatus),
                        style=modalPutProjectStyle,
                        leader=User.objects.get(username=modalPutProjectLeader).id
                    )
                except Exception as e:
                    return JsonResponse(code_error(str(e)))
                return JsonResponse(code_success())

    def delete(self, request):
        project_ids = QueryDict(request.body)
        try:
            # 逻辑删除  更新is_delete = 1
            for project_id in project_ids.getlist('project_ids[]'):
                ProjectBaseInfo.objects.filter(id=project_id).update(is_delete=1)
        except Exception as e:
            return JsonResponse(code_error(str(e)))
        return JsonResponse(code_success())


class ProjectDetailView(View):

    def get(self, request):
        token = request.GET.get("token")
        id = request.GET.get('id')
        if not token:
            return render(request, 'login.html', code_NO_token())
        jwt_verify = JWT_Verify()
        # 验证token 是否过期 如果过期返回登陆页 else: 返回页面
        verify_result = jwt_verify.render_page(request, token)

        if verify_result:
            user_login_id = jwt_verify.decode_token(token)['payload'].get('user_id')
            project_info = ProjectBaseInfo.objects.get(id=id)
            response_data = {}
            response_data['id'] = project_info.id
            response_data['status'] = project_info.status.name
            response_data['leader'] = project_info.leader.username
            response_data['style'] = project_info.style
            response_data['create_time'] = project_info.create_time
            response_data['update_time'] = project_info.update_time
            result_queryset = FileBaseInfo.objects.filter(is_delete=0).order_by('-update_time')[:5]
            #  queryset序列化输出
            result_json = serialize('json', result_queryset)
            result_dicts = json.loads(result_json)
            data = {}
            for index, result_dict in enumerate(result_dicts):
                data['id'] = result_dict['pk']
                data['name'] = result_dict['fields']['name']
                data['trial_status'] = result_dict['fields']['trial_status']
                data['create_time'] = result_dict['fields']['create_time']
                data['update_time'] = result_dict['fields']['update_time']
                data['username'] = result_queryset[index].founder.username
                data['leader'] = result_dict['fields']['leader']
                # data['project_status'] = result_dict['fields']['']
                # user = User.objects.filter(id=user_id)[0]
                # result_dicts[index]['fields']['leader'] = user.username
                # result_dicts[index]['fields']['file_project'] =
            response_data['result_dicts'] = result_dicts
            response_data['user_id'] = user_login_id
            return render(request, 'project_details.html', context=response_data)

    def post(self, request):
        #  上传项目文档
        # data = {'id': file.id, "name": file.name, 'trial_status': file.trial_status,'founder':file.founder,'file_router':file.file.url,'file_project':file.file_project.name, }
        file = request.FILES.get('file')
        #  获取项目id与用户id
        style_username = request.POST.get('file_project').split('.')
        if not file:
            return JsonResponse(code_error('no files for upload'))
        else:
            file_object = FileBaseInfo(name=file, trial_status='未审核', founder=User.objects.get(id=style_username[1]),
                                       file_router=file,
                                       file_project=ProjectBaseInfo.objects.get(id=style_username[0]), is_delete=0)
            file_object.save()
        return JsonResponse(code_success())
