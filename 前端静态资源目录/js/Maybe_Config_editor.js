var Config_Editor = {
        创建: {
            创建: function () {
                数据源 = {}
                数据源 = JSON.stringify(数据源)
                localStorage.setItem('Maybe_Config', 数据源)
            }
        },
        读取: {
            读取数据源: function (键) {
                数据源 = localStorage.getItem('Maybe_Config');
                数据源 = JSON.parse(数据源);
                if (数据源 === null) {
                    Config_Editor.创建.创建()
                    return null
                } else {
                    数据源 = 数据源[键]
                    if(数据源 === undefined){return null}
                    return 数据源
                }
            }
        },
        写入: {
            写入数据源: function (键, 值) {
                数据源 = localStorage.getItem('Maybe_Config');
                if (数据源 === null) {
                    Config_Editor.创建.创建()
                    Config_Editor.写入.写入数据源(键, 值)
                }
                数据源 = JSON.parse(数据源);
                数据源[键] = 值
                数据源 = JSON.stringify(数据源)
                localStorage.setItem('Maybe_Config', 数据源)
            }
        },
    }

function 定位(){
    
}