function ajax_helper_main(方法, 地址, 表单数据, 负载, 成功函数 = function () { }, 错误函数 = function () { }) {
    const xhr = new XMLHttpRequest();
    const 路径字符串 = 地址 + '?' + new URLSearchParams(负载).toString();
    xhr.open(方法, 路径字符串);

    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 301) {
            成功函数(xhr.responseText);
        } else {
            错误函数(xhr.statusText);
        }
    };

    xhr.onerror = function () {
        错误函数(xhr.statusText);
    };

    xhr.send(表单数据);
}


function ajax_helper_返回值解码(data){
    // 返回值转码

    // 解码Unicode转义序列
    function 解码Unicode(str) {
        return decodeURIComponent(JSON.parse('"' + str + '"'));
    }

    // 解析JSON字符串
    var 解析后的数据 = JSON.parse(data);

    // 遍历对象并解码值
    for (var 键 in 解析后的数据) {
        if (解析后的数据.hasOwnProperty(键)) {
            解析后的数据[键] = 解码Unicode(解析后的数据[键]);
        }
    }

    return 解析后的数据;
}