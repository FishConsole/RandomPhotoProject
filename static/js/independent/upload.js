document.getElementById('文件上传').addEventListener('change', function () {
    var 选择的文件 = this.files;
    var 选择的文件名 = [];
    var 选择的文件路径 = [];

    for (var i = 0; i < 选择的文件.length; i++) {
        选择的文件名.push(选择的文件[i].name);
        选择的文件路径.push(URL.createObjectURL(选择的文件[i]));
    }

    if (选择的文件.length > 1) {
        snackbar("已选择文件：" + 选择的文件名.join(", ") + "等多个文件");
    } else {
        snackbar("已选择文件：" + 选择的文件名.join(", "));
    }
    console.log(this.files);
});

document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault(); // 阻止表单默认提交行为

    var 文件上传输入框 = document.getElementById('文件上传');
    var 文件列表 = 文件上传输入框.files;

    var 进度条 = document.getElementById('progressContainer');
    var 进度容器 = document.getElementById('progressBar');

    if (文件列表.length === 0) {
        snackbar("请选择文件");
        return;
    }


    进度条.style.cssText = '';
    进度容器.style.cssText = '';

    console.log(进度容器);
    var 总文件数 = 文件列表.length;
    var 已完成文件数 = 0;

    for (var i = 0; i < 文件列表.length; i++) {
        var 当前文件 = 文件列表[i];
        var formData = new FormData();
        formData.append('file', 当前文件);

        ajax_helper_main("post", "/UploadStart", formData, "upload",
            function (data) {
                data = ajax_helper_返回值解码(data)
                console.log(data)
                if (data['状态'] === '失败') {
                    snackbar(data['内容']);
                    document.getElementById('upload_info').innerHTML += '<br>'+data['内容'];
                    setTimeout(function () {进度容器.style.cssText += 'opacity:0';}, 3000);
                }
                document.getElementById('upload_info').innerHTML = '<br>'+data['内容'] + document.getElementById('upload_info').innerHTML;
                已完成文件数++;
                var 进度 = (已完成文件数 / 总文件数) * 100;
                进度条.style.width = 进度 + "%";
                console.log(已完成文件数);
                console.log(总文件数);
                if (已完成文件数 === 总文件数) {
                    setTimeout(function () {进度容器.style.cssText += 'opacity:0';}, 3000);
                }
            },
            function (data) {
                snackbar(data);
                if (已完成文件数 === 总文件数) {
                    document.getElementById('upload_info').innerHTML += '<br>'+data['内容'];
                    setTimeout(function () {进度容器.style.cssText += 'opacity:0';}, 3000);
                }
            }
        );
    }
});