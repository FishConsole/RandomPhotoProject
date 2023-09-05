版本号 = ChangeLog_数据源[0]['版本号']

function 组件生成(数据源) {
    加载状态 = document.getElementById('加载状态')
    加载状态.style.cssText = ''
    // 提取动态颜色值
    动态颜色值 = localStorage.getItem('动态颜色值')
    数据源 = 数据源["Image_Data"]
    // 获取输出图片的位置
    限制 = document.getElementById('图片展示器')

    for (a in 数据源) {
        图片地址 = 数据源[a][0]
        图片简介 = 数据源[a][1]
        // 取图片简介的前四个字
        图片简介_剪切 = 图片简介.slice(0, 4)
        图片标签 = `
            <span class="img mdui-ripple mdui-ripple-white" onload="cssd()" style="background:${动态颜色值}"mdui-tooltip="{content: '${图片简介}'}">
                <a href="/PhotoInfo/${图片地址}">
                    <img src="../img/picture_down//${图片地址}" title=${图片简介} style="opacity: 0" target="_blank">
                </a>
                <p>${图片简介_剪切}</p>
            </span>
        `
        限制.innerHTML += 图片标签
    }

    图片加载状态 = setInterval(function () {
        所有图片标签 = document.querySelectorAll('img')
        总数 = 所有图片标签.length
        准备关闭的计数器 = 0
        for (i = 0; i < 所有图片标签.length; i++) {
            if (所有图片标签[i].complete) {
                所有图片标签[i].style.cssText = ''
                准备关闭的计数器 = 准备关闭的计数器 + 1
            }
        }
        if (准备关闭的计数器 == 总数) {
            clearInterval(图片加载状态)
        }
    }, 100)
    加载状态.style.cssText = 'display:none'

}


function 搜索发动() {
    文本对话框("请输入您想要搜索的图片名称", async function (搜索内容) {
        if (搜索内容 === "") {
            snackbar('至少要说一句话')
        } else {
            // 把文字限制在100个字符
            if (搜索内容.length > 100) {
                搜索内容 = 搜索内容.slice(0, 100)
            }
            限制 = document.querySelector('.限制')
            限制.style.cssText = 'opacity:0;'
            await ajax_helper_main('get', `/Search/${搜索内容}`, new FormData(), {}, function (responseText) {
                responseText = ajax_helper_返回值解码(responseText)
                responseText = eval(responseText)
                result = []

                for (a in responseText) {
                    // 把每一个数组中的数据按逗号分割，变成嵌套数组
                    result.unshift(responseText[a].split(','))
                }

                responseText = result
                if (responseText.length == 0) {
                    限制.style.cssText = 'opacity:1;'
                    snackbar('没有找到相关图片')
                } else {
                    限制.innerHTML = ''
                    responseText = {'Image_Data': responseText}
                    组件生成(responseText)
                    限制.style.cssText = 'opacity:1;'

                }

            }, function () {
                snackbar('关键词错误或网络错误')
            })
        }
    })
}

function 输出文档() {
    对话框(`
<div class="mdui-typo">
这里是RandomPhoto随机图片提供系统<br><br>当前版本为
     <b>${版本号}</b><br><br>
     由鱼几斤开发，您可以在此处预览和下载本站的所有图片
     <br><br>
     随机图片调用地址：
     <a href="/Random?range=月亮" target="_blank">随机图片调用地址</a>
     <br><br>
     指定图片调用地址：
     <a href="/Select/你中意的图片的文件名.png" target="_blank">指定图片调用地址</a>
     <br><br><br>
</div>
`);
}

function 开启抽屉栏() {
    var 抽屉栏_状态 = new mdui.Drawer('#drawer');
    抽屉栏_状态.open()
}

function 关闭抽屉栏() {
    if (window.screen.availWidth < 1000) {
        setTimeout(() => {
            var 抽屉栏_状态 = new mdui.Drawer('#drawer')
            抽屉栏_状态.close()
        }, 2000)
    }
}

function 进入更新记录() {
    var 子页面_ChangeLog = document.getElementById('子页面_ChangeLog');
    子页面_ChangeLog.style.display = 'block';
    关闭抽屉栏();
    setTimeout(function () {
        子页面_ChangeLog.style.left = '1vw';
    }, 50);
}

function 进入文件上传() {
    var 子页面_upload = document.getElementById('子页面_upload');
    子页面_upload.style.display = 'block';
    关闭抽屉栏();
    setTimeout(function () {
        子页面_upload.style.left = '1vw';
    }, 50);
}


parent.parent.返回 = function (data) {
    function 关闭overlay() {
        mdui.$.hideOverlay();
        mdui.$.lockScreen();


        if ((window.screen.availWidth < 1000)) {
            var 抽屉栏_状态 = new mdui.Drawer('#drawer')
            抽屉栏_状态.close()
        }

    }


    //加载来自config系统的配置
    //1 第一条配置：退出编辑器弹窗开关
    /////////////////////////////////////////
    function 取消渲染() {
        子页面_upload = document.getElementById('子页面_upload')
        子页面_ChangeLog = document.getElementById('子页面_ChangeLog')
        setTimeout(() => {
            子页面_upload.style.display = 'none';
            子页面_ChangeLog.style.display = 'none';
        }, 600)
    }

    if (data == 'upload') {
        子页面_upload = document.getElementById('子页面_upload')
        子页面_upload.style.cssText = 'left:100vw;'
        关闭overlay()
        取消渲染()
    }
    if (data == 'ChangeLog') {
        子页面_ChangeLog = document.getElementById('子页面_ChangeLog')
        子页面_ChangeLog.style.cssText = 'left:100vw;'
        关闭overlay()
        取消渲染()
    }
}

//////////////////////////////////////////////////////////////////////////////////////////////

function 加入群组() {
    对话框(`
<div class="mdui-typo">
欢迎大家来到RandomPhoto的群组，我们很高兴能和大家一起讨论问题，分享图片，一起进步！<br><br>QQ群：<a class="mdui-typo" href="http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=-oliRT0JFze5-8MVoIuLMX9a1XAaVDsV&authKey=8uo%2FKb%2FcG5uVu25N8fkyfr0AzdKwWa9wBVnDSHdT2ErtSmam8AgQJN%2FmUZ2Bee4g&noverify=0&group_code=117907928">加入QQ群</a>
    <br><br>
     QQ频道：<a class="mdui-typo" href="https://pd.qq.com/s/ewcec18hm">加入频道</a>
   </div>
`);
}

//////////////////////////////////////////////////////////////////////////////////////////////

子页面_历史更新容器 = document.getElementById('子页面_历史更新容器')
子页面_文件上传容器 = document.getElementById('子页面_文件上传容器')

setTimeout(function () {
    子页面_历史更新容器.innerHTML = '<iframe src="../ChangeLog" id="子页面_ChangeLog" style="display:none" class="child_page"></iframe>'
    子页面_文件上传容器.innerHTML = '<iframe src="../Upload" id="子页面_upload" style="display:none" class="child_page"></iframe>'

}, 2000)