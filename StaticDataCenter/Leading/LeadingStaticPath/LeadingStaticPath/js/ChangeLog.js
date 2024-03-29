ChangeLog_数据源 = [
    {
        '版本号': 'v20240229',
        '更新内容': [
            '质量更新：Random图片返回接口升级,将正排关键字修改为倒排关键字',
        ]
    },
    {
        '版本号': 'v20240228',
        '更新内容': [
            '质量更新：Random图片返回接口升级,并对其注册到了测试部门',
        ]
    },
    {
        '版本号': 'v20240227',
        '更新内容': [
            '质量更新：加入sqlite转excel，方便用户进行数据库升级',
            'BUG修复：手机端随机图片返回的图片不包含适用于平板的图片的问题',
        ]
    },
    {
        '版本号': 'v20240223',
        '更新内容': [
            '质量更新：手机端随机图片返回的图片将包含适用于平板的图片',
        ]
    },
    {
        '版本号': 'v20240222',
        '更新内容': [
            'BUG修复：修复了photoinfo的图片显示问题',
        ]
    },
    {
        '版本号': 'v20240221',
        '更新内容': [
            '阶段更新：Welcome to the RandomPhoto 4x',
            '阶段更新：上架奇妙应用',
            '阶段更新：适配 Android14 系统',
            '阶段更新：对路径控制部门进行重构，可读性大幅提高并优化了资源复用率',
            '阶段更新：后端架构调整，使用加入测试部门，将在启动时启动自动检测',
            '阶段更新：分词库销毁',
            '阶段更新：搜索系统由按词搜索修改为按字搜索，大幅度提高搜索精度并增加搜索范围',
            '阶段更新：数据目录彻底重构，规范了各个部门的命名',
            '阶段更新：数据目录支持自定义目录，可随时修改',
            '质量更新：加入基于IPv6的公网连接方式和基于IPv4的内网连接方式，使用二维码快速连接',
            '质量更新：给图片一句话打标签功能销毁，直接将这句话送入数据库以保证数据的准确性和尽可能的做到记录更多的信息',
        ]
    },
    {
        '版本号': 'v20230917',
        '更新内容': [
            '质量更新：后端架构调整，使用鱼骨架构规范',
            '质量更新：分词库自定义词典加入更多的选项，搜索精度提高',
            'BUG修复：main的界面显示调整为基于显示宽度设置高度',
            'BUG修复：修复一些接口问题',
            'BUG修复：修复海纳接口问题',
        ]
    },
    {
        '版本号': 'v20230914',
        '更新内容': [
            '质量更新：index页面加入自定义滚动条',
            '质量更新：完善审核系统的图片审核2.0 Beta（首次运行通过）',
            '质量更新：审核系统改名为Audit System',
            '质量更新：审核系统风车图标被修改为RandomPhoto Logo',
            '质量更新：info页面风车替换为svg图标并支持转动',
            '质量更新：upload页面风车替换为svg图标并支持转动',
            '质量更新：upload页面云上传图标改变为svg图标',
            '质量更新：photo页面文字修改为upload增加可读性',
            'BUG修复：修复邮件系统被忽略的问题',
        ]
    },
    {
        '版本号': 'v20230912',
        '更新内容': [
            '质量更新：前端调试控制系统Beta 持续完善',
            '质量更新：优化了index页面的启动逻辑',
            'BUG修复：修复了审核系统安全性验证的问题',
            'BUG修复：修复了审核系统安全性验证前端自动跳转的问题',
            'BUG修复：修复网速不好的情况下组件生成故障的问题',
        ]
    },
    {
        '版本号': 'v20230911',
        '更新内容': [
            '质量更新：加入前端调试控制系统Beta',
            '质量更新：修复风车图标来源问题，并且将他改成了svg用来节省流量',
            'BUG修复：修复了友联栏折叠时的布局问题',
            'BUG修复：修复了播放器的布局问题',
        ]
    },
    {
        '版本号': 'v20230910',
        '更新内容': [
            '质量更新：提交tag时将会显示动画',
            '质量更新：优化tag审核系统的代码，解决了需要提交两次才会生效的问题',
            '质量更新：优化tag审核系统的回调，拒绝死板的回调',
        ]
    },
    {
        '版本号': 'v20230909',
        '更新内容': [
            '质量更新：提交tag修改请求后将会发送邮件',
            '维护：重启所有功能',
        ]
    },
    {
        '版本号': 'v20230907',
        '更新内容': [
            '架构调整：针对tag审核系统做了大规模的调整',
            '界面更新：info页面图标换成了svg',
            '界面更新：对话框文字修改',
            '质量更新：加入tag审核系统',
            '质量更新：打散回调中心',
        ]
    },
    {
        '版本号': 'v20230904',
        '更新内容': [
            '维护：对所有js的代码进行了一次整理',
            '维护：对所有css的代码进行了一次整理',
            '维护：对Lib库的所有代码进行了一次整理',
            '质量更新：加入网易云爬虫用来爬取指定歌单的BGM用于播放器',
            '质量更新：加入ICP备案',
        ]
    },
    {
        '版本号': 'v20230827',
        '更新内容': [
            '质量更新：对话框对大型屏幕外观优化',
            '质量更新：ChangeLog现在只会显示前十条内容',
            '质量更新：子页面在被关闭时会被取消渲染用来腾出性能',
            '质量更新：优化index页面外观',
            '质量更新：自动死亡线程函数传参优化',
            '维护：对Lib库的所有代码进行了一次整理',
        ]
    },
    {
        '版本号': 'v20230826',
        '更新内容': [
            '质量更新：main页面逻辑优化',
            '质量更新：加载优化',
            '质量更新：index界面优化',
        ]
    },
    {
        '版本号': 'v20230825',
        '更新内容': [
            '质量更新：加入了动态取色系统',
            '质量更新：main页面的css，js，html分离',
            '质量更新：全新设计了RandomPhtot的图标，图标的名称就是Ra',
            '质量更新：重写main，优化了main的加载逻辑',
            '质量更新：将谷歌图标交给谷歌CDN处理，用来调高加载速度',
        ]
    },
    {
        '版本号': 'v20230824',
        '更新内容': [
            '质量更新：加入了调试模式启动的警告',
            '质量更新：加入了对苹果浏览器，华为浏览器的支持',
            '质量更新：流量节省程序升级，数据连接状态下不会加载背景图片',
            'BUG修复：修复了PC上缩放到达 100% 时出现的显示问题',
            'BUG修复：所需库一键部署大修',
            'BUG修复：修复版本号提取找不到版本号的问题',
            'BUG修复：修复了帮助文档链接跳转不用新标签打开的问题',
        ]
    },
    {
        '版本号': 'v20230821',
        '更新内容': [
            '质量更新：加入了【规范网址】用来满足搜索引擎的需求',
            '质量更新：加入了友联用来互相引荐',
            '质量更新：版本号提取器找不到文件就懒得管了',
            'BUG修复：修复了index子页面打开并退出后无法滑动的问题',
        ]
    },
    {
        '版本号': 'v20230820',
        '更新内容': [
            '质量更新：修复flask限制上传文件的大小为40MB',
            '质量更新：上传控件在原来的基础上加入了错误重试的能力，并且对整个前端上传系统进行错误处理',
            '质量更新：禁止让cloudflare托管代码文件',
            '质量更新：增加了搜索系统的错误回调的字符串把要说的内容说的更清楚了一些',
            'BUG修复：修复上传系统的400，524报错',
            'BUG修复：限制20MB以上的图片上传',
        ]
    },
    {
        '版本号': 'v20230819',
        '更新内容': [
            '质量更新：加入robots.txt用来支持搜索引擎的要求',
            '质量更新：全站meta标签补全',
            '质量更新：全站meta_description标签补全',
            '质量更新：全站title标签补全',
            '质量更新：CloudFlare缓存超时上调至1年',
            '质量更新：上传系统最高支持40MB图片的上传',
        ]
    },
    {
        '版本号': 'v20230818',
        '更新内容': [
            '质量更新：解决多解释器自动安装库的问题，默认使用目标解释器对应PIP进行安装',
            '质量更新：现在各种模式的启动位置将由路径控制管理',
            '质量更新：站点地图：/sitemap.xml上线',
        ]
    },
    {
        '版本号': 'v20230817',
        '更新内容': [
            '质量更新：修复无法启动的问题',
            '质量更新：放慢了main的加载速度让他能在回环网络上多显示一下动画',
            '质量更新：index根据调试模式自动选择不同的模式启动',
            '质量更新：倒排图片排序，越新的图片越排在前面',
            'BUG修复：修复了upload的问题',
        ]
    },
    {
        '版本号': 'v20230816',
        '更新内容': [
            '前端版本回退为0806：通过重组的方式修复无法启动的问题',
            '质量更新：main界面优化',
            '质量更新：后端新增自动三方库补全，启动index.py自动补全',
            '质量更新：后端启动时将会显示当前的版本号',
            'BUG修复：通过重组修复前端异常卡死的问题',
        ]
    },
    {
        '版本号': 'v20230806',
        '更新内容': [
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
        '版本号': 'v20230720',
        '更新内容': [
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
        '版本号': 'v20230711',
        '更新内容': [
            '阶段更新：对已有代码进行稳定性加强和评估无法修复的BUG所带来的潜在危险，本次为大版本更新。后续进入维护状态',
        ]
    },
    {
        '版本号': 'v20230710',
        '更新内容': [
            '质量更新：海纳接口调整',
            '质量更新：主页最多只加载180张图片'
        ]
    },
    {
        '版本号': 'v20230709',
        '更新内容': [
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
        '版本号': 'v20230706',
        '更新内容': [
            '质量更新：新上传的图片在当天首页优先显示，不限张数',
            '质量更新：修复不排前面的问题',
            '质量更新：修复数据库路径和代码路径冲突的恶性BUG',
            '质量关系：升级了上传页面，它动画更加丰富了',
            '质量关系：加入百度统计',
        ]
    },
    {
        '版本号': 'v20230705',
        '更新内容': [
            '质量更新：新上传的图片现在可以排在最前，最多20张',
        ]
    },
    {
        '版本号': 'v20230704',
        '更新内容': [
            '质量更新：所有线程数据存储方式转为sqlite存储',
            '质量更新：Random接口支持返回横屏或竖屏的图片。默认自适应，可手动指定',
            '质量更新：帮助文档优化'
        ]
    },
    {
        '版本号': 'v20230620',
        '更新内容': [
            '质量更新：自动死亡线程升级，启动时执行检测',
            '质量更新：缩率图清晰度再次上调'
        ]
    },
    {
        '版本号': 'v20230619',
        '更新内容': [
            '质量更新：反盗链升级，加入token，这样可以让apk端也可以通过反盗链系统',
            '质量更新：审核系统升级，没有任务时显示猫猫图片',
            '质量更新：管理系统升级，分离出主程序，加入控制邮件发送系统的功能'
        ]
    },
    {
        '版本号': 'v20230616',
        '更新内容': [
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
        '版本号': 'v20230614',
        '更新内容': [
            '质量更新：新增Select接口',
            '质量更新：新增防盗链系统Beta',
            '质量更新：审核系统压缩图片失败自动删除图片',
            '质量更新：大图界面点击图片可以自动复制文件名',
            '架构调整：所有的跟图片返回操作相关的代码全部移动在一起进行统一管理',
            'bug修复：现在服务端的自杀系统只会在死之前发邮件，不会像原来一样在启动的时候就发邮件了'
        ]
    },
    {
        '版本号': 'v20230611',
        '更新内容': [
            '质量更新：实验性服务端自杀线程',
            '修复bug：审核队列邮件轰炸的问题',
            '修复bug：邮件系统用户缺失的问题',
            '修复bug：重载器数据载入时卡死的问题',
            '修复bug：图片元素据不存在导致的报错的问题',
            '修复bug：审核队列压缩图片时失败后依然保留图片的问题'
        ]
    },
    {
        '版本号': 'v20230606',
        '更新内容': [
            '质量更新：审核队列功能完善，实装测试',
        ]
    },
    {
        '版本号': 'v20230530',
        '更新内容': [
            '阶段更新：对各个组件进行很大的调整',
            '阶段更新：加入回调器API，所有的参数将通过json进行回调',
            '阶段更新：将主程序的代码进行了重构，使得代码更加的清晰',
            '阶段更新：将主程序所有的代码移动到了不同的文件以适应更大的代码量',
            '阶段更新：后端输出内容修改',
        ]
    },
    {
        '版本号': 'v20230528',
        '更新内容': [
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
        '版本号': 'v20230527',
        '更新内容': [
            '质量更新：根据小鲸鱼的想法修改了背景透明度和每一个项目的背景色',
            '质量更新：加入图片上传系统',
            '质量更新：加入低级的人工审核手段'
        ]
    },
    {
        '版本号': 'v20230526',
        '更新内容': [
            '质量更新：适配Photo_info适配PC端',
            '质量更新：加入加入群组的功能',

        ]
    },
    {
        '版本号': 'v20230504',
        '更新内容': [
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

板块b = '                </div>\n' +
    '            </div>\n' +
    '        </div>'
for (j = 0; j < 10; j++) {
    li_temp = ''
    板块a = '        <div class="板块">\n' +
        '            <div class="标题">\n' +
        '                <div class="版本号">版本号</div>\n' +
        '                <div class="版本号值">' + ChangeLog_数据源[j]['版本号'] + '</div>\n' +
        '            </div>\n' +
        '            <div class="内容">\n' +
        '                <div class="文字">'

    for (i = 0; i < ChangeLog_数据源[j]['更新内容'].length; i++) {
        li_temp += '<li>' + ChangeLog_数据源[j]['更新内容'][i] + '</li>'
    }

    li_temp = '<ol>' + li_temp + '</ol>'
    输出 = 板块a + li_temp + 板块b
    li_temp = null
    项目范围.innerHTML += 输出
}