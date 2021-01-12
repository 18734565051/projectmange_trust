from fdfs_client.client import Fdfs_client

client = Fdfs_client('client.conf')
result = client.upload_by_filename('/home/baixin/Desktop/装备修理能力认证评估管理系统20180612 -TDG.doc')
print(result)
'''
docker run -d --name storage --net=host -e TRACKER_IP=<your tracker server address>:22122 -e GROUP_NAME=<group name> morunchang/fastdfs sh storage.sh

'''