// 表单使用ajax提交
function LoginVerify() {
  var username = $('#username').val();
  var mobile = $('#mobile').val();
  var email = $('#email').val();
  var password = $('#password').val();
  var password2 = $('#password2').val();
  $.ajax({
    url: "/login/",
    data: {
      'username': username,
      "mobile": mobile,
      "email": email,
      "password": password,
      "password2": password2
    },
    type: "POST",
    dataType: "json",
    success: function (data) {
      if (data.code == 100) {
        //保存token到local stroge
        //存储id到localStorage  // sessionStorage有相同的API：setItem、getItem、removeItem...
        localStorage.setItem('token', data.token);
        // 拼接url   token=token
        window.location.href = "/?token=" + localStorage.getItem('token')
      } else {
        $('#response_info').html(data.msg);
      }
    },
    error: function (data) {
      $('#response_info').html(data.msg)
    }
  })
}