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

function 通过审核图片(文件名,ID) {
    console.log(文件名)
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

        fetch(`../../admin_thing~/shenhe/Accept/${value}/${文件名}`)
            .then(response => response.json())
            .then(data => {
                进度条.style.cssText = 'width: 80%;';
                snackbar(`${data['内容']}`)
                目标标签 = document.getElementById(ID)
                console.log(目标标签)
                目标标签.style.cssText = 'display:none'
            })
    })

}

function 删除审核图片(文件名,ID) {
    fetch(`../../admin_thing~/shenhe/Delete/${文件名}`)
        .then(response => response.json())
        .then(data => {
            snackbar(`${data['内容']}`)
            目标标签 = document.getElementById(ID)
            目标标签.style.cssText = 'display:none'
        })
}

function 查看大图(文件名) {
    // 创建一个模态框
    var 标签 = document.createElement('div');
    标签.setAttribute('class', '查看大图')
    标签.style.cssText = `
    position: fixed;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    background-color: rgb(0 0 0 / 64%);
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
        `

    // 创建一个图片元素
    var 图片元素 = document.createElement('img');
    图片元素.src = `/img/Temp_File_Start/${文件名}`;
    图片元素.style.cssText = 'margin-top: -50px;border-radius: 20px;';

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