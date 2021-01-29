from django.db import models
from user.models import User
import uuid
from pro.utils import model
# from approval.models import FlowModel


#  项目阶段表
class ProjectCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='类别编号', help_text="类别编号")
    name = models.CharField(max_length=20, null=True, verbose_name='当前项目状态',
                            help_text='{"0": "项目获得", "1": "项目启动", "2": "项目策划", "3": "项目实施", "4": "项目测试", "5": "项目结项", "6": "其他"}')

    class Meta:
        db_table = 'tb_ProjectCategory'
        verbose_name = '项目阶段表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#  项目基本信息表
class ProjectBaseInfo(model.BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='项目编号', help_text="项目编号")
    name = models.CharField(max_length=20, verbose_name='项目名称', help_text="项目名称")
    leader = models.ForeignKey(User, verbose_name='负责人', on_delete=models.CASCADE, help_text="负责人")
    style = models.CharField(null=True, max_length=20, verbose_name="项目类型", help_text="项目类型")
    is_delete = models.BooleanField(default=0, verbose_name='是否删除', help_text="逻辑删除")
    status = models.ForeignKey(ProjectCategory, null=True, on_delete=models.CASCADE, verbose_name='状态外键')

    # manage = models.ForeignKey(User, verbose_name='审批人', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_ProjectBaseInfo'
        verbose_name = '项目基本信息表'
        verbose_name_plural = verbose_name


# 文档基本信息表

class FileBaseInfo(model.BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="文档编号", help_text="文档编号")
    name = models.CharField(max_length=50, verbose_name="文件名称", help_text="文档名字")
    trial_status = models.CharField(max_length=20, verbose_name="审核状态", help_text="未审核、已审核、正在审核")
    founder = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建人", help_text="创建人")
    leader = models.CharField(max_length=50, verbose_name='审批人', null=True, blank=True, help_text='审批人')
    file_router = models.FileField(verbose_name='文件存储路径', help_text="文件存储路径",
                                   upload_to="upload/%Y/%m/%d/")
    file_project = models.ForeignKey(ProjectBaseInfo, null=True, on_delete=models.CASCADE, verbose_name='隶属项目',
                                     help_text='隶属项目')
    project_status = models.CharField(max_length=50, null=True, verbose_name='文档隶属项目状态', help_text='文档隶属项目状态')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除', help_text='是否删除')
    # flow_name = models.ForeignKey(FlowModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='流程对象',
    #                               help_text='流程对象')

    class Meta:
        db_table = "tb_filebaseInfo"
        verbose_name = '文档基本信息表'
        verbose_name_plural = verbose_name


# 日志表
class Log(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名', help_text="用户名")
    time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    content = models.TextField(verbose_name="内容", help_text="内容")
    project = models.ForeignKey(ProjectBaseInfo, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'tb_log'
        verbose_name = '日志表'
        verbose_name_plural = verbose_name
