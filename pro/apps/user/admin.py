from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserProfileAdmin(UserAdmin):
    #  每页显示多少条
    list_per_page = 2
    #  顶部显示属性信息
    actions_on_top = True
    #  指定显示的列
    list_display = ['id', 'username', 'date_joind', 'group']
    # 搜索框
    search_fields = ['username']
    # 过滤器
    # list_filter = ['is_superuser']
    # 页头
    admin.site.site_header = '项目全生命周期管理'
    # 首页标语
    admin.site.site_title = '项目全生命周期管理'
    #
    admin.site.index_title = '项目全生命周期管理'
    # 详情页显示的字段
    # fields = ['password', 'last_login']
    fieldsets = (
        ('基本信息', {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),

        ('个人信息', {'fields': ('mobile', 'image')}),

        ('权限信息', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),

        ('登录信息', {'fields': ('last_login', 'date_joined')})
    )


admin.site.register(User, UserProfileAdmin)
