from django.contrib import admin
from .models import ProjectBaseInfo, FileBaseInfo, Log
# Register your models here.

admin.site.register(ProjectBaseInfo)
admin.site.register(FileBaseInfo)
admin.site.register(Log)

