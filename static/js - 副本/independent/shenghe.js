function 文本拷贝(text) {
    const input = document.createElement('textarea');
    input.value = text;
    // 不要让input.value转义
    input.setAttribute('readonly', '');
    document.body.appendChild(input);
    input.select();
    document.execCommand('copy');
    document.body.removeChild(input);
    console.log(text)
    snackbar(`文件名:${text}复制成功`)
}

function 通过审核图片(文件名) {
    进度条 = document.getElementById("进度条")
    文本对话框("一句话描述这个图片", async function (value) {
        // 如果value这个字符串中没有任何内容，则后面的函数不进行
        进度条.style.cssText = 'width: 10%;';
        if (value === "") {
            snackbar('至少要说一句话')
            进度条.style.cssText = 'width: 0%;opacity: 0';
            return 0
        }
        // 如果value的字数小于2个字，则后面的函数不进行
        if (value.length < 2) {
            snackbar('字数不够')
            文本拷贝(value)
            进度条.style.cssText = 'width: 0%;opacity: 0';
            return 0
        }
        进度条.style.cssText = 'width: 40%;';

        await ajax_helper_main('get', `../../admin_thing~/shenhe/Accept/${value}/${文件名}`, new FormData(), {}, function (responseText) {
            进度条.style.cssText = 'width: 80%;';

            data = ajax_helper_返回值解码(responseText)
            snackbar(`${data['内容']}`)
            目标标签 = document.getElementById(`Photo_${文件名}`)
            console.log(目标标签)
            目标标签.style.cssText = 'height:0px;opacity:0;width:100%!important;scale: 1.2;'
            setTimeout(function () {
                目标标签.parentNode.parentNode.style.cssText = 'width:0px;opacity:0;'
                进度条.style.cssText = 'width: 100%;';

                setTimeout(function () {
                    目标标签.parentNode.parentNode.style.cssText = 'display:none'
                    进度条.style.cssText = 'width: 0;opacity: 0';
                }, 500)
            }, 700)
        }, function (responseText) {
        })
    })
}

async function 删除审核图片(文件名) {
    await ajax_helper_main('get', `../../admin_thing~/shenhe/Delete/${文件名}`, new FormData(), {}, function (responseText) {
        data = ajax_helper_返回值解码(responseText)
        snackbar(`${data['内容']}`)
        目标标签 = document.getElementById(`Photo_${文件名}`)
        目标标签.style.cssText = 'height:0px;opacity:0;width:100%!important;scale: 1.2;'
        setTimeout(function () {
            目标标签.parentNode.parentNode.style.cssText = 'width:0px;opacity:0;'
            setTimeout(function () {
                目标标签.parentNode.parentNode.style.cssText = 'display:none'
            }, 500)
        }, 700)
        console.log(目标标签)

    }, function (responseText) {
        data = ajax_helper_返回值解码(responseText)
        alert(`${data['内容']}`)
    })
}


function 查看大图(文件名) {
    // 创建一个模态框
    var 标签 = document.createElement('div');
    标签.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        backdrop-filter: blur(10px);
        `

    // 创建一个图片元素
    var 图片元素 = document.createElement('img');
    图片元素.src = `/img/temp_files/${文件名}`;
    图片元素.style.cssText = 'width: 90vw!important; height: auto;margin-top: -130px;';

    // 将图片元素添加到模态框中
    标签.appendChild(图片元素);

    // 将模态框添加到页面中
    document.body.appendChild(标签);

    // 点击模态框关闭
    标签.addEventListener('click', function () {
        标签.parentNode.removeChild(标签);
    });

    文本拷贝(文件名)
}