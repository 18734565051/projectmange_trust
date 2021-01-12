def code_success():
    return {"code": 100, "msg": "success"}


def code_error(e):
    return {"code": 500, "msg": e}


def code_user_exists():
    return {"code": 101, "msg": "用户名已存在"}


def code_user_Ordinary_user():
    return {'code': 1012, 'msg': '您是普通用户'}


def code_user_No_exists():
    return {"code": 1011, 'msg': "用户名不存在"}


def code_email_exists():
    return {"code": 102, "msg": "邮箱已存在"}


def code_email_format_No():
    return {"code": 1021, "msg": "邮箱格式不正确"}


def code_mobile_exists():
    return {"code": 103, "msg": "手机号已存在"}


def code_mobile_fromat_No():
    return {"code": 1031, "msg": "手机号格式不正确"}


def code_info_No_exists():
    return {'code': 1032, "msg": "没有账户,请注册"}


def code_password_different():
    return {"code": 104, "msg": "密码不一致"}


def code_password_error():
    return {"code": 1041, "msg": "密码错误"}


def code_jwt_invalid():
    return {"code": 201, "msg": "登陆过期,请重新登陆"}


def code_NO_token():
    return {"code": 203, "msg": "请重新登录"}


def code_jwt_verify():
    return {"code": 200, "msg": "验证有效"}


def code_jwt_illegal():
    return {"code": 202, "msg": "非法篡改"}


def code_porject_name_exists():
    return {"code": 301, "msg": '项目名称已存在'}


def code_files_upload_fail():
    return {"code": 401, "msg": "文件上传失败"}
