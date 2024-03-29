// 动态加载iframe
加载内容 = document.getElementById('加载内容')

// 加载超时
启动图 = document.getElementById('启动图')
计时器状态 = document.getElementById('计时器')
setTimeout(function () {
    if (计时器状态.innerHTML === "true") {
        snackbar('加载失败，准备重试')
        window.location.reload()
    }
}, 20000)

// 归位，因为默认是这个颜色值
localStorage.setItem('动态颜色值', '#a9b5d8 !important')

///////////////////////////////////////////////////////////////////////////////////////////

// 背景图片控制工具
function 背景图片加载() {
    加载内容 = document.getElementById('加载内容')
    加载内容.innerHTML = 加载内容.innerHTML + '<p> > 等待背景图片</p>' + '<br>'
    fetch('/Random')
        .then(function (response) {
            if (!response.ok) {
                加载内容.innerHTML = 加载内容.innerHTML + '<p> > 图片请求异常，直接进入</p>' + '<br>'
                iframe = document.createElement('iframe')
                iframe.src = '/index'
                iframe.id = 'iframe_RandomPhoto'
                iframe.style.cssText = 'z-index:2;top:30px;opacity:0;'
                iframe.className = 'iframe_RandomPhoto'
                document.body.appendChild(iframe)
                iframe.onload = () => {
                    加载内容.innerHTML = 加载内容.innerHTML + '<p> > 加载完毕</p>' + '<br>'
                    计时器状态.innerHTML = "false"
                    RandomPhoto = document.getElementById('iframe_RandomPhoto')
                    setTimeout(() => {
                        RandomPhoto.style.cssText = 'top:0;opacity:1;'
                        启动图.style.cssText = 'display:none;'
                        加载内容.style.cssText = 'display:none;'
                        document.getElementById('index').style.cssText = 'background-color:rgb(255,255,255);'
                    }, 2000);
                }
            }
            return response.blob()
        })
        .then(function (blob) {

            // 背景图片加载
            图片URL = URL.createObjectURL(blob)
            document.getElementById('背景图片').style.cssText = 'background-image: url(' + 图片URL + ') !important;opacity:0'
            setTimeout(function () {
                document.getElementById('背景图片').style.cssText += 'opacity:1'
            }, 2500)

            // 图片背景色提取
            图片 = new Image();
            图片.src = 图片URL;

            图片.onload = function () {
                加载内容.innerHTML = 加载内容.innerHTML + '<p> > 正在准备动态取色</p>' + '<br>'
                // 获得图片数据
                画布 = document.createElement("canvas");
                画布.width = 图片.width;
                画布.height = 图片.height;

                上下文 = 画布.getContext("2d");
                上下文.drawImage(图片, 0, 0);

                图片数据 = 上下文.getImageData(0, 0, 画布.width, 画布.height).data;

                // 获得图片平均颜色
                红色总和 = 0;
                绿色总和 = 0;
                蓝色总和 = 0;
                for (i = 0; i < 图片数据.length; i += 4) {
                    红色总和 += 图片数据[i];
                    绿色总和 += 图片数据[i + 1];
                    蓝色总和 += 图片数据[i + 2];
                }
                总像素数 = 图片数据.length / 4;// 红色,绿色,蓝色,透明度
                平均颜色 = {
                    红: Math.round(红色总和 / 总像素数) + 10,
                    绿: Math.round(绿色总和 / 总像素数) + 10,
                    蓝: Math.round(蓝色总和 / 总像素数) + 10

                }
                rgb颜色值 = `rgb(${平均颜色['红']},${平均颜色['绿']},${平均颜色['蓝']})`
                加载内容.innerHTML = 加载内容.innerHTML + '<p> > 动态取色完成，正在进行微调</p>' + '<br>'

                if (平均颜色['红'] < 50 || 平均颜色['绿'] < 50 || 平均颜色['蓝'] < 50) {
                    平均颜色['红'] = 平均颜色['红'] + 150
                    平均颜色['绿'] = 平均颜色['绿'] + 150
                    平均颜色['蓝'] = 平均颜色['蓝'] + 150
                }
                if (平均颜色['红'] < 150 || 平均颜色['绿'] < 150 || 平均颜色['蓝'] < 150) {
                    // console.log('灰色背景强行调亮')
                    平均颜色['红'] = 平均颜色['红'] + 140
                    平均颜色['绿'] = 平均颜色['绿'] + 140
                    平均颜色['蓝'] = 平均颜色['蓝'] + 140
                }
                if (平均颜色['红'] < 180 || 平均颜色['绿'] < 180 || 平均颜色['蓝'] < 180) {
                    // console.log('淡灰色背景强行调亮')
                    平均颜色['红'] = 平均颜色['红'] + 40
                    平均颜色['绿'] = 平均颜色['绿'] + 40
                    平均颜色['蓝'] = 平均颜色['蓝'] + 40
                }
                if (平均颜色['红'] > 280 || 平均颜色['绿'] > 280 || 平均颜色['蓝'] > 280) {
                    // console.log('淡灰色背景强行调亮')
                    平均颜色['红'] = 平均颜色['红'] - 80
                    平均颜色['绿'] = 平均颜色['绿'] - 80
                    平均颜色['蓝'] = 平均颜色['蓝'] - 80
                }

                rgb颜色值 = `rgb(${平均颜色['红']},${平均颜色['绿']},${平均颜色['蓝']})`
                localStorage.setItem('动态颜色值', rgb颜色值 + ' !important')

                加载内容 = document.getElementById('加载内容')
                加载内容.innerHTML = 加载内容.innerHTML + '<p> * 等待加载完毕</p>' + '<br>'


                加载内容.innerHTML = 加载内容.innerHTML + '<p> > 动态取色完成</p>' + '<br>'
                // 创建并检查iframe是否加载完毕

                iframe = document.createElement('iframe')
                iframe.src = '/index'
                iframe.id = 'iframe_RandomPhoto'
                iframe.style.cssText = 'z-index:2;top:30px;opacity:0;'
                iframe.className = 'iframe_RandomPhoto'
                document.body.appendChild(iframe)
                iframe.onload = () => {
                    加载内容.innerHTML = 加载内容.innerHTML + '<p> > 加载完毕</p>' + '<br>'
                    计时器状态.innerHTML = "false"
                    RandomPhoto = document.getElementById('iframe_RandomPhoto')
                    setTimeout(() => {
                        RandomPhoto.style.cssText = 'top:0;opacity:1;'
                        启动图.style.cssText = 'display:none;'
                        加载内容.style.cssText = 'display:none;'
                        document.getElementById('index').style.cssText = 'background-color:rgb(255,255,255);'
                    }, 2000);
                }
            }
        })
}

///////////////////////////////////////////////////////////////////////////////////////////


// 流量节省工具
if ('connection' in navigator) {
    html = document.getElementById('html')
    加载内容 = document.getElementById('加载内容')
    const connection = navigator.connection;
    // 获取当前网络连接类型
    const 网络连接类型 = connection.type;

    if (网络连接类型 === 'wifi') {
        背景图片加载()
        加载内容.innerHTML = 加载内容.innerHTML + '<p> * 当前使用 Wi-Fi 连接</p>' + '<br>'
    } else if (网络连接类型 === 'cellular') {
        加载内容.innerHTML = 加载内容.innerHTML + '<p> * 当前使用 数据 连接</p>' + '<br>'
        iframe = document.createElement('iframe')
        iframe.src = '/index'
        iframe.id = 'iframe_RandomPhoto'
        iframe.style.cssText = 'z-index:2;top:30px;opacity:0;'
        iframe.className = 'iframe_RandomPhoto'
        document.body.appendChild(iframe)
        iframe.onload = () => {
            加载内容.innerHTML = 加载内容.innerHTML + '<p> > 加载完毕</p>' + '<br>'
            计时器状态.innerHTML = "false"
            RandomPhoto = document.getElementById('iframe_RandomPhoto')
            setTimeout(() => {
                RandomPhoto.style.cssText = 'top:0;opacity:1;'
                启动图.style.cssText = 'display:none;'
                加载内容.style.cssText = 'display:none;'
                document.getElementById('index').style.cssText = 'background-color:rgb(255,255,255);'
            }, 2000);
        }
    } else {
        背景图片加载()
        加载内容.innerHTML = 加载内容.innerHTML + '<p> * 当前使用 未知 连接</p>' + '<br>'
    }
} else {
    加载内容.innerHTML = 加载内容.innerHTML + '<p> * 流量节省程序 - 背景图控制不受支持</p>' + '<br>'
    背景图片加载()
}

///////////////////////////////////////////////////////////////////////////////////////////

const 错位纠正 = () => {
    iframe_RandomPhoto = document.getElementById('iframe_RandomPhoto')
    iframe_RandomPhoto.style.height = `${window.innerHeight}px`
};

window.addEventListener('resize', 错位纠正);

