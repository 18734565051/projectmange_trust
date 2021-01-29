//  创建项目
function modalCreateProject() {
  let projectStyle = $('#modalCreateProjectStyle').val();
  let projectName = $('#modalCreateProjectName').val();
  let token = localStorage.getItem('token');
  if (token == undefined) {
    window.location.href = "/login/"
  } else {
    $.ajax({
      url: "/ProjectInfo/",
      data: {
        'project_name': projectName,
        "project_style": projectStyle,
        "token": token
      },
      type: "POST",
      dataType: "json",
      success: function (data) {
        if (data.code != 100) {
          $('#modalErrorMsg').html(data.msg)
        } else {
          $.each(data.data, function (k, v) {
            let createProjectContent = "<tr><td>";
            createProjectContent += "<input type='checkbox' value=" + v['pk'] + "></td><td>";
            createProjectContent += v['pk'] + "</td><td>";
            createProjectContent += v['fields']['name'] + "</td><td>";
            createProjectContent += v['fields']['style'] + "</td><td>";
            createProjectContent += v['fields']['create_time'] + "</td><td>";
            createProjectContent += v['fields']['update_time'] + "</td><td>";
            createProjectContent += v['fields']['status'] + "</td><td>";
            createProjectContent += v['fields']['leader'] + "</td></tr>";
            $('#createProjectContent').append(createProjectContent)
          });
          $('#modalCreate').modal('hide')
        }
      },
      error: function (data) {
        $('#response_info').html(data.msg)
      }
    })
  }
}


function alertModalPut() {
//  if选中多个或者0个弹出提示 否则 弹出修改模态框
  let checked_count = $("input[type='checkbox']:checked").length;
  if (checked_count != 1) {
    alert("当前选中" + checked_count + "个，只能选中一个")
  } else {
    // 手动显示模态框
    $('#modalProjectId').html($("input[type='checkbox']:checked").val());
    $('#modalPut').modal('toggle');
  }
}

// 更新
function BtnModalPut() {
  let modalPutProjectName = $('#modalPutProjectName').val();
  let modalPutProjectStyle = $('#modalPutProjectStyle').val();
  let modalPutProjectStatus = $('#modalPutProjectStatus').val();
  let modalPutProjectLeader = $('#modalPutProjectLeader').val();
  $.ajax({
    url: "/ProjectInfo/",
    dataType: "json",
    type: 'PUT',
    data: {
      'project_id': $("input[type='checkbox']:checked").val(),
      "modalPutProjectName": modalPutProjectName,
      "modalPutProjectStyle": modalPutProjectStyle,
      "modalPutProjectStatus": modalPutProjectStatus,
      "modalPutProjectLeader": modalPutProjectLeader,
    },
    success: function (data) {
      if (data.code != 100) {
        $('#response_update_info').html(data.msg)
      } else {
        // 返回成功 关闭模态框 更改选中表格的项目信息
        $('#modalPut').modal('hide');
        $("input[type='checkbox']:checked").parent().parent().next().next().html(modalPutProjectName);
        $("input[type='checkbox']:checked").parent().parent().next().next().next().html(modalPutProjectStyle);
        $("input[type='checkbox']:checked").parent().parent().next().next().next().next().next().next().html(modalPutProjectStatus);
        $("input[type='checkbox']:checked").parent().parent().next().next().next().next().next().next().next().html(modalPutProjectLeader);
      }
    },
    error: function (data) {
      $('#response_update_info').html(data)
    }
  })
}

// 删除项目
function deleteCheckProject() {
  const detele_checked_count = $("input[type='checkbox']:checked").length;
  if (detele_checked_count == 0) {
    alert('请至少选中一个， 当前选中：' + detele_checked_count + '个')
  } else {
    const project_ids = new Array();
    $('input[type="checkbox"]:checked').each(function () {
      project_ids.push($(this).val());
    });
    $.ajax({
      url: "/ProjectInfo/",
      data: {
        "project_ids": project_ids
      },
      type: 'delete',
      dataType: "json",
      success: function (data) {
        if (data.code == 100) {
          //  删除列表tr
          $("input[type='checkbox']:checked").parent().parent().parent().remove()
        } else {
          alert(data.msg)
        }
      },
      error: function (data) {
        alert(data.msg)
      }
    });
  }
}

//  input搜索框
function BtnSearchProjectInfo() {
  $.ajax({
    url: '/ProjectInfo/',
    dataType: 'json',
    type: 'get',
    data: {
      "name": $('#searchProjectName').val(),
      "leader": $('#searchProjectLeader').val(),
      "status": $('#searchProjectStatus').val(),
      "style": $('#searchProjectStyle').val(),
      "create_time": $('#searchProjectCreateTime').val(),
      "update_time": $('#searchProjectUpdateTime').val()
    },
    success: function (data) {
      if (data.code != 100) {
        $('#modalErrorMsg').html(data.msg)
      } else {
        let token = localStorage.getItem('token');
        let createProjectContent = "";
        $.each(data.data, function (k, v) {
          let pk = v["pk"];
          createProjectContent += "<tr><td><input type='checkbox' value=" + pk + "></td><td>";
          createProjectContent += v['pk'] + "</td><td>" + "<a href='/ProjectDetail/?token=" + token + "&id=" + pk + "'>";
          createProjectContent += v['fields']['name'] + "</a></td><td>";
          createProjectContent += v['fields']['style'] + "</td><td>";
          createProjectContent += v['fields']['create_time'] + "</td><td>";
          createProjectContent += v['fields']['update_time'] + "</td><td>";
          createProjectContent += v['fields']['status'] + "</td><td>";
          createProjectContent += v['fields']['leader'] + "</td></tr>";
        });
        $('#createProjectContent').html(createProjectContent);
        $('#modalCreate').modal('hide')
      }
    },
    error: function (data) {
      $('#response_info').html(data.msg)
    }
  })
}

// 上传文档组件
$(function () {
  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true,  /* 1. SEND THE FILES ONE BY ONE 这个属性指示该组件一次发送一个文件*/

    start: function (e) {   /* 2. WHEN THE UPLOADING PROCESS STARTS, SHOW THE MODAL */
      $("#modal-progress").modal("show");
    },

    stop: function (e) {  /* 3. WHEN THE UPLOADING PROCESS FINALIZE, HIDE THE MODAL */
      $("#modal-progress").modal("hide");
    },

    progressall: function (e, data) {  /* 4. UPDATE THE PROGRESS BAR */
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      $(".progress-bar").text(strProgress);
    },

    done: function (e, data) {

      $('#modalFileCreate').modal("hide");

      $("#fileUploadTo").prepend(
        "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
      )
    }
  });
});

// 文件显示
$(function () {
  /* 1. OPEN THE FILE EXPLORER WINDOW */
  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
  $("#fileupload").fileupload({  //fileupload
    dataType: 'json',
    done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER  这里的data来自于JsonResponse传来的data*/
      if (data.result.is_valid) {
        $("#gallery tbody").prepend(
          "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
        )
      }
    }
  });
});


//  编辑文档

function alertFileModalPut() {
  let checked_count = $("input[type='checkbox']:checked").length;
  if (checked_count != 1) {
    alert("当前选中" + checked_count + "个，只能选中一个")
  } else {
    // 手动显示模态框
    $('#modalPutFileId').html($("input[type='checkbox']:checked").val());
    $('#modalFilePut').modal('toggle');
  }
}

// 修改文档信息
function BtnModalPutFile() {
  $.ajax({
    url: '/ProjectDetail/',
    type: 'put',
    dataType: 'json',
    data: {
      'file_id': $('#modalPutFileId').html(),
      'fileLeader': $('#modalPutFileLeader').val(),
      "project_status": $('#modalPutFileProjectStatus').val(),
    },
    success: function (data) {
      if (data.code == 100) {
        $('#modalFilePut').modal("hide");
      } else {
        $('#response_File_update_info').html(data.msg)
      }
    }
  })

}

// 删除文档
function deleteFileCheckProject() {
  const detele_checked_count = $("input[type='checkbox']:checked").length;
  if (detele_checked_count == 0) {
    alert('请至少选中一个， 当前选中：' + detele_checked_count + '个')
  } else {
    const project_ids = new Array();
    $('input[type="checkbox"]:checked').each(function () {
      project_ids.push($(this).val());
    });
    $.ajax({
      url: "/ProjectDetail/",
      data: {
        "project_ids": project_ids
      },
      type: 'delete',
      dataType: "json",
      success: function (data) {
        if (data.code == 100) {
          //  删除列表tr
          $("input[type='checkbox']:checked").parent().parent().parent().remove()
        } else {
          alert(data.msg)
        }
      },
      error: function (data) {
        alert(data.msg)
      }
    });
  }
}

// 审批
function alertapprovalModal() {
  let checked_count = $("input[type='checkbox']:checked").length;
  if (checked_count == 0) {
    alert("当前选中" + checked_count + "个，至少选择一个")
  } else {
    $.ajax({
      url: "/Approval/File/",
      dataType: "json",
      type: 'get',
      success: function (data) {
        if (data.code == 100) {
          var selectStr = '<select class="form-control" id="modalApprovalFile">';
          $.each(data.data, function (index, item) {
            $.each(item, function (k, v) {
              selectStr += "<option value=" + k + ">" + v + "</option>"
            })
          });
          selectStr += "</select>";
          $('#modalSelectMange').html(selectStr);
          // 手动显示模态框
          $('#modalFileapprovalPut').modal('toggle');
        } else {
          $('#modalSelectMange').html(data.msg);
        }
      },
      error: function (data) {
        $('#modalSelectMange').html(data);
      }
    });

  }
}

function BtnModalApprovalFile() {
  const detele_checked_count = $("input[type='checkbox']:checked").length;
  if (detele_checked_count == 0) {
    alert('请至少选中一个， 当前选中：' + detele_checked_count + '个')
  } else {
    const file_ids = new Array();
    $('input[type="checkbox"]:checked').each(function () {
      file_ids.push($(this).val());
    });
    user_id = $('#modalApprovalFile').val();
    $.ajax({
      url: "/Approval/File/",
      data: {
        "file_ids": file_ids,
        "user_id":user_id
      },
      type: 'post',
      dataType: "json",
      success: function (data) {
        if (data.code == 100) {
          //  删除列表tr
          $("input[type='checkbox']:checked").parent().parent().parent().remove()
        } else {
          alert(data.msg)
        }
      },
      error: function (data) {
        alert(data.msg)
      }
    });
  }
}