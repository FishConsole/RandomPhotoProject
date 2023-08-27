function 程序名() {
    return 'Photos'
}

function 对话框(内容) {
    mdui.alert(内容, '<div><img src="../../static/assats/randomphoto.svg"></div>' + 程序名());
}


function 文本对话框(内容, 执行函数) {

    mdui.prompt(内容, '<div><i class="mdui-icon material-icons 对话框图标">all_out</i></div>', function (value) {
        执行函数(value)
    });
}

function snackbar(内容) {
    mdui.snackbar({ message: 内容, position: 'top' })
}

function 运行条的提示() {
    运行条.style.cssText = 'display:block';
    setTimeout(function () {
        运行条.style.cssText = 'display:none';
    }, 2000)
}

function runningBar的提示() {
    runningBar.style.cssText = 'display:block';
    setTimeout(function () {
        runningBar.style.cssText = 'display:none';
    }, 2000)
}

