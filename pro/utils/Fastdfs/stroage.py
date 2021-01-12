from django.conf import settings
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client


class FdfsStorage(Storage):
    def __init__(self):
        # 客户端配置文件
        self.client_conf = settings.FDFS_CLIENT

    def open(self, name, mode='rb'):
        pass

    def save(self, name, content, max_length=None):
        # 创建对象
        client = Fdfs_client(self.client_conf)
        # 保存
        result = client.upload_by_buffer(content.read())
        # 返回文件名
        return result
        
