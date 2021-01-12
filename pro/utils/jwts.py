import jwt
import time
import datetime
from django.conf import settings
from pro.utils.return_code import *
from django.shortcuts import render


class JWT_Verify(object):
    def __init__(self):
        self.salt = settings.SECRET_KEY
        # self.salt = 'wo-bt(d0pom#-8p^v631l^o_#sxgjz4omqo$_ng=h^s#zhcftu'

    def encode_token(self, payload, exp=1):
        # salt =  'wo-bt(d0pom#-8p^v631l^o_#sxgjz4omqo$_ng=h^s#zhcftu'

        headers = {
            "alg": "HS256",
            "typ": "JWT"
        }
        if exp is None:
            token = jwt.encode(payload=payload, key=self.salt,
                               headers=headers).decode("utf-8")
        else:
            payload["exp"] = datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=24*60)
            token = jwt.encode(payload=payload, key=self.salt,
                               headers=headers).decode("utf-8")
        return token

    def decode_token(self, token):
        #  传入token 获得结果 1608626644
        result = jwt.decode(token, self.salt,  False)
        return {'payload': result}

    def check_jwt(self,token):
        client_sign = token.split('.')[2]
        # 验证token是否有效
        # 获取payload
        client_payload = self.decode_token(token).get('payload')
        # 过期时间与当前时间做判断 if 小于 有效
        if not client_payload.get('exp') > int(time.time()):
            return code_jwt_invalid()
        # 取出客户端发送过来的token header payload 私钥进行加密 生成sign
        generate_token_sign = self.encode_token(
            client_payload, exp=None).split('.')[2]
        # 与client发送过来的sign进行对比
        if not generate_token_sign == client_sign:
            return code_jwt_illegal()
        else:
            return code_jwt_verify()

    def render_page(self, request, token):
        jwt_verify = JWT_Verify()
        # 验证token 是否过期 如果过期返回登陆页 else: 返回页面
        verify_result = jwt_verify.check_jwt(token)
        if verify_result.get('code') != 200:
            return render(request, 'login.html', context=verify_result)
        else:
            return True


if __name__ == "__main__":
    jwt_ = JWT_Verify()
    token = jwt_.encode_token({'name': 'zt', 'age': '11'})
    print(token)
    payload = jwt_.decode_token(token)
    print(payload)
