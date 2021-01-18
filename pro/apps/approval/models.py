from django.db import models
import uuid
from user.models import User

'''流程节点表'''


class FlowNodeModel(models.Model):
    node_id = models.UUIDField(default=uuid.uuid4, verbose_name='节点id', help_text='节点id')
    node_name = models.CharField(max_length=200, verbose_name='节点名称', help_text='节点名称')
    Flower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='审批人', help_text='审批人')

    class Meta:
        db_table = 'tb_flownode'
        verbose_name = '流程节点表'
        verbose_name_plural = verbose_name


'''流程表'''


class FlowModel(models.Model):
    flow_no = models.CharField(max_length=200, default=uuid.uuid4, verbose_name='流程号', help_text='流程号')
    flow_name = models.CharField(max_length=200, verbose_name='流程名称')
    node = models.ForeignKey(FlowNodeModel, on_delete=models.CASCADE, verbose_name='节点', help_text='节点')

    class Meta:
        db_table = 'tb_flow'
        verbose_name = '流程表'
        verbose_name_plural = verbose_name
