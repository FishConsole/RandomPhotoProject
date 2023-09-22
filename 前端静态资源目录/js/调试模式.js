function 调试模式专用函数(显示文字, 函数 = () => {
    throw new Error("本程序由前端调试模式停止")
}) {
    const 调试模式启动状态 = document.getElementById('调试模式').innerHTML
    if (调试模式启动状态 === 'true') {
        console.groupCollapsed(`前端调试模式 - ${显示文字}`);
        函数()
        console.groupEnd();
    } else {
        console.clear()
    }
}
