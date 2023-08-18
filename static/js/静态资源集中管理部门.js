function 静态资源集中管理部门(文件名, main状态 = false) {

    function ajax_helper_main(方法, 地址, 表单数据, 负载, 成功函数 = function () {
    }, 错误函数 = function () {
    }) {
        const xhr = new XMLHttpRequest();
        xhr.open(方法, 地址 + '?' + new URLSearchParams(负载).toString(), true);
        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                成功函数(xhr.responseText);
            }
        };
        xhr.onerror = function () {
            错误函数(xhr.statusText);
        };
        xhr.send(表单数据);
    }


    // 迭代每一个数据
    for (i = 0; i < 文件名.length; i++) {
        // 文件名这个变量在后面是会被处理的，为了避免这个情况先提取

        失败重试次数 = 0

        function 启动(文件名, 文件后缀) {
            const formData = new FormData();
            当前时间 = String(new Date().toLocaleDateString())
            文件配置信息 = JSON.parse(localStorage.getItem(文件名))
            if (文件配置信息 === null) {
                文件载入日期 = ''
            } else {
                文件载入日期 = 文件配置信息['当前时间']
            }
            if (当前时间 != 文件载入日期) {


                ajax_helper_main('get', `/${文件名}`, formData, () => {
                    失败重试次数 += 1
                    if (失败重试次数 > 3) {
                        console.log(`文件{文件名}获取失败：已经尝试重新获取文件3次，但是依然失败`)
                        // 清除失败重试次数，这样可以在下一个文件载入时使用
                        失败重试次数 = 0
                        return 0
                    } else {
                        console.log(`文件{文件名}获取失败：正在试图重新获取文件【第${失败重试次数}次】`)
                        启动(文件名, 文件后缀)
                    }
                }, (data) => {
                    // 清除失败重试次数
                    失败重试次数 = 0
                    // 获取文件，刷新或创建
                    localStorage.setItem(文件名, JSON.stringify({
                        当前时间: 当前时间,
                        代码内容: data,
                        文件后缀: 文件后缀
                    }));
                    // 递归调用，实现立刻使用文件
                    console.log({当前时间: 当前时间, 代码内容: data, 文件后缀: 文件后缀})
                    启动(文件名, 文件后缀)
                })
            } else {
                // 使用文件
                // 获得指定文件配置信息
                const 文件配置信息 = JSON.parse(localStorage.getItem(文件名))
                const 文件后缀 = 文件配置信息['文件后缀']
                const 代码内容 = 文件配置信息['代码内容']
                if (!main状态) {
                    if (文件后缀 === 'js') {
                        // js文件
                        var script = document.createElement('script');
                        script.type = 'text/javascript';
                        script.innerHTML = 代码内容;
                        document.head.appendChild(script);
                    }
                    if (文件后缀 === 'css') {
                        // css文件
                        var style = document.createElement('style');
                        style.type = 'text/css';
                        style.innerHTML = 代码内容;
                        document.head.appendChild(style);
                    }
                }else{
                    加载内容 = document.getElementById('加载内容')
                    加载内容.innerHTML = 加载内容.innerHTML + `<p>${文件名}</p>` + '<br>'
                }

            }
        }

        文件后缀 = 文件名[i].split('.')
        文件后缀 = 文件后缀[文件后缀.length - 1]
        启动(文件名[i], 文件后缀)
    }
    if (main状态){
        加载内容 = document.getElementById('加载内容')
        加载内容.innerHTML = 加载内容.innerHTML + `<p> * 静态资源加载完成</p>` + '<br>'
    }
}
