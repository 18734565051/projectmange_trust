from django.db import models
from django.contrib.auth.models import Group
from user.models import User
from pro.utils.model import BaseModel
from pages.models import ProjectBaseInfo

'''任务表'''


class Task(models.Model):
    #  重要性
    degrees = (
        ('info', '一般'),
        ('warning', '警告'),
        ('error', '严重'),
        ('critical', '非常严重')
    )
    name = models.CharField(max_length=200, verbose_name='任务名', help_text='任务名')
    style = models.CharField(null=True, max_length=100, verbose_name='任务类型', help_text='任务')
    status = models.CharField(null=True, max_length=100, verbose_name='任务状态', help_text='任务状态')
    leaders = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='发布人', help_text='发布人')
    start_time = models.DateTimeField(null=True, verbose_name='指定开始时间', help_text='指定截止时间')
    end_time = models.DateTimeField(null=True, verbose_name='指定截止时间', help_text='指定截止时间')
    handler = models.CharField(null=True, max_length=50, verbose_name='处理人', help_text='处理人')
    handle_time = models.DateTimeField(null=True, verbose_name='承接时间', help_text='承接时间')
    degree = models.CharField(max_length=20, null=True, choices=degrees)
    project = models.CharField(max_length=20, null=True, verbose_name='隶属项目阶段', help_text='隶属项目阶段')
    handler_team = models.ForeignKey(Group, null=True, on_delete=models.CASCADE, verbose_name='选择团队')
    description = models.TextField(null=True, verbose_name='任务描述', help_text='任务描述')

    class Meta:
        db_table = 'tb_task'
        verbose_name = '任务表'
        verbose_name_plural = verbose_name


'''审批管理员表'''


class ApprovalManager(models.Model):
    manager = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    remarks = models.TextField(null=True, verbose_name='备注', help_text='备注')

    class Meta:
        db_table = 'tb_approvalmanager'
        verbose_name = '审批管理员表'
        verbose_name_plural = verbose_name


'''审批负责人表'''


class ApprovalLeaders(models.Model):
    leader = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(ApprovalManager, on_delete=models.CASCADE, null=True)
    remarks = models.TextField(null=True, verbose_name='负责人备注', help_text='备注')

    class Meta:
        db_table = 'tb_ApprovalLeaders'
        verbose_name = '审批负责人表'
        verbose_name_plural = verbose_name


'''审批基本信息表'''


class ApprovalBaseInfo(models.Model):
    is_manger = models.BooleanField(default=0, verbose_name='是否需要管理员审批', help_text='是否需要管理员审批')
    leader = models.ForeignKey(ApprovalLeaders, null=True, on_delete=models.CASCADE)
    task = models.OneToOneField(Task, null=True, on_delete=models.CASCADE, verbose_name='任务审核')

    class Meta:
        db_table = 'tb_approvalbaseinfo'
        verbose_name = '审批基本信息表'
        verbose_name_plural = verbose_name
