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

async function ajax_helper_main(方法, 地址, 表单数据, 负载, 成功函数 = function () {}, 错误函数 = function () {}) {

    阻止异步请求 = new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.timeout = 5000; // 设置超时时间为5秒
        xhr.open(方法, 地址 + '?' + new URLSearchParams(负载).toString());

        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                成功函数(xhr.responseText);
                resolve(xhr.responseText);
            } else {
                错误函数(xhr.statusText);
            }
        };

        xhr.onerror = function () {
            错误函数(xhr.statusText);
        };

        xhr.ontimeout = function (e) {
            错误函数(xhr.statusText);
        }

        xhr.send(表单数据);
    });
    return 阻止异步请求
}


document.getElementById('uploadForm').addEventListener('submit', async function (event) {
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
    上传成功统计 = 0
    上传失败统计 = 0

    async function 文件上传() {
        await ajax_helper_main("post", "/UploadStart", formData, "upload",

            function (data) {
                data = ajax_helper_返回值解码(data)
                if (data['状态'] === '失败') {
                    snackbar(data['内容']);
                    document.getElementById('upload_info').innerHTML += '<br>' + data['内容'];
                    setTimeout(function () {
                        进度容器.style.cssText += 'opacity:0';
                    }, 3000);
                }
                document.getElementById('upload_info').innerHTML = '<br>' + data['内容'] + document.getElementById('upload_info').innerHTML;
                已完成文件数++;
                var 进度 = (已完成文件数 / 总文件数) * 100
                进度条.style.width = 进度 + "%"
                console.group('文件上传进度')
                console.log(已完成文件数)
                console.log(总文件数)
                console.groupEnd()
                上传成功统计 = 上传成功统计 + 1
                if (已完成文件数 === 总文件数) {
                    setTimeout(function () {
                        进度容器.style.cssText += 'opacity:0'
                    }, 3000);
                }
            },
            async function (data) {
                文件上传_错误计数器 = 文件上传_错误计数器 + 1
                if (文件上传_错误计数器 > 30) {
                    上传失败统计 = 上传失败统计 + 1

                    snackbar(`目标文件上传失败，已经尝试重新上传: ${文件上传_错误计数器}次`);
                    document.getElementById('upload_info').innerHTML = '<br>' + `目标文件上传失败，已经尝试重新上传: ${文件上传_错误计数器}次，但是依然失败,放弃上传` + document.getElementById('upload_info').innerHTML;
                    文件上传_错误计数器 = 0

                    已完成文件数++;
                    var 进度 = (已完成文件数 / 总文件数) * 100
                    进度条.style.width = 进度 + "%"

                    if (已完成文件数 === 总文件数) {

                        const currentTime = new Date();
                        const hours = currentTime.getHours();
                        const minutes = currentTime.getMinutes();
                        const seconds = currentTime.getSeconds();
                        const time = `${hours}:${minutes}:${seconds}`;

                        document.getElementById('upload_info').innerHTML = '<br>' + `文件上传完毕，当前时间为${time}. 成功${上传成功统计} 失败${上传失败统计}` + document.getElementById('upload_info').innerHTML;

                        setTimeout(function () {
                            进度容器.style.cssText += 'opacity:0'
                        }, 3000);
                    }
                } else {
                    document.getElementById('upload_info').innerHTML = '<br>' + `目标文件上传失败，正在尝试重新上传: ${文件上传_错误计数器}` + document.getElementById('upload_info').innerHTML;
                    // 重新上传
                    await 文件上传()
                }

            }
        );
    }

    for (var i = 0; i < 文件列表.length; i++) {
        var 当前文件 = 文件列表[i];
        var formData = new FormData();
        formData.append('file', 当前文件);


        文件上传_错误计数器 = 0


        await 文件上传()
    }
});