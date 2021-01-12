from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    image = models.ImageField(upload_to='user', verbose_name='头像', null=True)

    #  admin 返回时间
    def date_joind(self):
        return self.date_joined.strftime('%Y年%m月%d日 %H时%M分%S秒')
        # 模型类表头名字 、 指定排序

    date_joind.short_description = "创建日期"
    date_joind.admin_order_field = 'date_joined'

    #  关联对象组
    def group(self):
        group_str = ''
        for group_name in self.groups.all():
            group_str += '%s' % group_name + '、'
        return group_str

    group.short_description = '组'

    class Meta:
        db_table = "tb_user"
        verbose_name = '用户'
        verbose_name_plural = verbose_name
