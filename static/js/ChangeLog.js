//////////////////////////////////////////////////////
// 通用函数责任区域


ChangeLog_数据源 = [
    {
      '版本号':'v20230815',
      '更新内容':[
          '质量更新：引流站搁置，但是不会放弃',
          '质量更新：引流站将mdui转换成在线载入',
          '测试：本地分支和在线分支x2',
      ]
    },
    {
      '版本号':'v20230814',
      '更新内容':[
          '质量更新：服务器加入webhook，这样做能让代码的更新变的更加的轻松',
          '架构调整：服务器RandomPhoto_webhook测试',
      ]
    },
    {
        '版本号':'v20230813',
        '更新内容':[
            '质量更新：加入自动图像标签生成器的启动器，通过这种方法可以自由启动自动图像生成器的启动和停止',
            '质量更新：main界面重写',
            '质量更新：去掉了一个没有用的请求',
            '质量更新：修复了一些命名的问题',
            '质量更新：Random功能增加：增加了选定随机范围的能力',
            'bug修复：修复了搜索系统的字符错误',
            'bug修复：修复了从内置帮助文档中打开时不从新标签页中打开的问题',
        ]
    },
    {
        '版本号':'v20230812',
        '更新内容':[
            '质量更新：加入自动图像标签生成器的启动器，通过这种方法可以自由启动自动图像生成器的启动和停止',
            '质量更新：main界面重写',
            '质量更新：去掉了一个没有用的请求',
            '质量更新：修复了一些命名的问题',
            '质量更新：Random功能增加：增加了选定随机范围的能力',
            'bug修复：修复了搜索系统的字符错误',
            'bug修复：修复了从内置帮助文档中打开时不从新标签页中打开的问题',
        ]
    },
    {
        '版本号':'v20230806',
        '更新内容':[
            '质量更新：优化海纳接口',
            '质量更新：重写admin',
            '质量更新：加入自动tag生成器【AI】',
            'bug修复：解决了Photoinfo页面在PC端的显示问题',
            '质量更新：info页面布局优化',
            '质量更新：main页面布局优化',
            'bug修复：现在背景图片在多个页面中只会显示同一张',
            'bug修复：解决了Photoinfo页面在PC端的显示问题',
            'bug修复：搜索系统修复'
        ]
    },
    {
        '版本号':'v20230720',
        '更新内容':[
            '质量更新：审核系统现在会对不满足要求的图片实行自动抛弃的策略',
            '质量更新：审核系统的猫猫图片换成了克拉拉的gif动图',
            '质量更新：图片标签现在会在主页以工具提示的方式显示',
            '质量更新：图片标签现在加入详情页面',
            '架构更新：数据库升级，对全站收录的所有图片加入标签用以搜索',
            '架构更新：针对搜索系统对所有代码进行调整',
            '质量更新：加入搜索系统',
        ]
    },
    {
        '版本号':'v20230711',
        '更新内容':[
            '阶段更新：对已有代码进行稳定性加强和评估无法修复的BUG所带来的潜在危险，本次为大版本更新。后续进入维护状态',
        ]
    },
    {
        '版本号':'v20230710',
        '更新内容':[
            '质量更新：海纳接口调整',
            '质量更新：主页最多只加载180张图片'
        ]
    },
    {
        '版本号':'v20230709',
        '更新内容':[
            '人员组织结构变化：现在RandomPhoto可以加盟了，目前有两个群聊，一个是OCSS，一个是主群，还有一个频道，欢迎加入',
            '质量更新：数据库的返回变的更加高效，理论上会大幅提升加载的速度',
            '质量更新：群聊加入链接变成直接进入主群',
            '质量更新：审核系统改为Admin系统，加入了更多的功能模板',
            '质量更新：现在主页的图片变成了当天上传的所有图片，如果当天没有上传图片，那么就会显示第一页的内容',
            '质量更新：现在不会启动重复的线程了',
            '质量更新：优化代码，挖掘出大量的BUG',
            '质量更新：将加群链接从直接跳转QQ群变成了QQ群+QQ频道',
            '质量更新：文件上传器最大限制由60>200',
            '质量更新：超鏈接文字顔色修改為MDUI樣式的文字',
            '质量更新：新增RandomPhoto引流站（IPv4地址），他和主站不在同一个服务器，但是为了防止代码不好调试和引流服务器突然暴毙现在把他和主站放在一起需要时分开上传',
            '盟友适配：针对海纳定制了专属的接口',
        ]
    },
    {
        '版本号':'v20230706',
        '更新内容':[
            '质量更新：新上传的图片在当天首页优先显示，不限张数',
            '质量更新：修复不排前面的问题',
            '质量更新：修复数据库路径和代码路径冲突的恶性BUG',
            '质量关系：升级了上传页面，它动画更加丰富了',
            '质量关系：加入百度统计',
        ]
    },
    {
        '版本号':'v20230705',
        '更新内容':[
            '质量更新：新上传的图片现在可以排在最前，最多20张',
        ]
    },
    {
        '版本号':'v20230704',
        '更新内容':[
            '质量更新：所有线程数据存储方式转为sqlite存储',
            '质量更新：Random接口支持返回横屏或竖屏的图片。默认自适应，可手动指定',
            '质量更新：帮助文档优化'
        ]
    },
    {
        '版本号':'v20230620',
        '更新内容':[
            '质量更新：自动死亡线程升级，启动时执行检测',
            '质量更新：缩率图清晰度再次上调'
        ]
    },
    {
        '版本号':'v20230619',
        '更新内容':[
            '质量更新：反盗链升级，加入token，这样可以让apk端也可以通过反盗链系统',
            '质量更新：审核系统升级，没有任务时显示猫猫图片',
            '质量更新：管理系统升级，分离出主程序，加入控制邮件发送系统的功能'
        ]
    },
    {
        '版本号':'v20230616',
        '更新内容':[
            '架构调整：将图片目录移出static得到更高的安全性',
            '架构调整：统一路径资源',
            '质量更新：规范控制台输出',
            '质量更新：完善防盗链系统',
            '质量更新：青蛙被加入管理队列',
            '质量更新：审核系统压缩图片失败将会删除对应的图片',
            '质量更新：审核系统压缩图片的分辨率提高，用较大的流量换取更低的流量消耗(减少看大图时消耗的完整流量)',
            'Bug修复：修复审核图片生成器的疏忽的问题',
        ]
    },
    {
        '版本号':'v20230614',
        '更新内容':[
            '质量更新：新增Select接口',
            '质量更新：新增防盗链系统Beta',
            '质量更新：审核系统压缩图片失败自动删除图片',
            '质量更新：大图界面点击图片可以自动复制文件名',
            '架构调整：所有的跟图片返回操作相关的代码全部移动在一起进行统一管理',
            'bug修复：现在服务端的自杀系统只会在死之前发邮件，不会像原来一样在启动的时候就发邮件了'
        ]
    },
    {
        '版本号':'v20230611',
        '更新内容':[
            '质量更新：实验性服务端自杀线程',
            '修复bug：审核队列邮件轰炸的问题',
            '修复bug：邮件系统用户缺失的问题',
            '修复bug：重载器数据载入时卡死的问题',
            '修复bug：图片元素据不存在导致的报错的问题',
            '修复bug：审核队列压缩图片时失败后依然保留图片的问题'
        ]
    },
    {
        '版本号':'v20230606',
        '更新内容':[         
            '质量更新：审核队列功能完善，实装测试',
        ]
    },
    {
        '版本号':'v20230530',
        '更新内容':[         
            '阶段更新：对各个组件进行很大的调整',
            '阶段更新：加入回调器API，所有的参数将通过json进行回调',
            '阶段更新：将主程序的代码进行了重构，使得代码更加的清晰',
            '阶段更新：将主程序所有的代码移动到了不同的文件以适应更大的代码量',
            '阶段更新：后端输出内容修改',
        ]
    },
    {
        '版本号':'v20230528',
        '更新内容':[
            '质量更新：升级图片上传系统，这使得该系统拥有了上传多文件的能力',
            '质量更新：升级图片上传系统，让他拥有了完整的进度条',
            '质量更新：升级图片上传系统，让他拥有了在邮件服务器因为批量上传导致被封IP的状态下依然可以上传的能力',
            '质量更新：升级图片上传系统，限制审核队列用来防止被炸硬盘。',
            '质量更新：升级图片上传系统，图片的上传Log不会再以Snackbare的形式显示而是显示在仿Photoshop的日志控制台上',
            '质量更新：将图片上传系统的各个代码放在了各自该在的位置上',
            '质量更新：缩略图生成器设置同步',            
            '阶段更新：阶段更新启动',
            'BUG修复：修复了点击文件时显示两次文件已选中的bug',
        ]
    },
    {
        '版本号':'v20230527',
        '更新内容':[
            '质量更新：根据小鲸鱼的想法修改了背景透明度和每一个项目的背景色',
            '质量更新：加入图片上传系统',
            '质量更新：加入低级的人工审核手段'
        ]
    },
    {
        '版本号':'v20230526',
        '更新内容':[
            '质量更新：适配Photo_info适配PC端',
            '质量更新：加入加入群组的功能',

        ]
    },
    {
        '版本号':'v20230504',
        '更新内容':[
            '架构更新：开启抽屉栏',
            'bug修复：彻底解决PC端的显示问题',
            'bug修复：修复图片计数器在第二页不显示的问题',
            'bug修复：彻底解决PC端的显示问题',
            'bug修复：Samsung Galaxy S8+屏幕布局问题修复'
        ]
    },
]


//////////////////////////////////////////////////////
// 循序执行责任区域

// 这段代码的用处就是生成页面显示的内容，这个内容要成
// if(Config_Editor.读取.读取数据源('完整的ChangeLog开关')!=true){ChangeLog_数据源 = ChangeLog_数据源.splice(0,10);}


项目范围 = document.getElementById('项目范围')

板块b='                </div>\n' +
    '            </div>\n' +
    '        </div>'
for(j=0;j<ChangeLog_数据源.length;j++){
    li_temp=''
    板块a='        <div class="板块">\n' +
        '            <div class="标题">\n' +
        '                <div class="版本号">版本号</div>\n' +
        '                <div class="版本号值">'+ChangeLog_数据源[j]['版本号']+'</div>\n' +
        '            </div>\n' +
        '            <div class="内容">\n' +
        '                <div class="文字">'

    for(i=0;i<ChangeLog_数据源[j]['更新内容'].length;i++){
        li_temp += '<li>'+ChangeLog_数据源[j]['更新内容'][i]+'</li>'
    }

    li_temp = '<ol>'+li_temp+'</ol>'
    输出 = 板块a+li_temp+板块b
    li_temp = null
    项目范围.innerHTML += 输出
}

