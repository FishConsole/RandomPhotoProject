
ChangeLog_数据源 = [
    {
      '版本号':'v20230815',
      '更新内容':[
          '质量更新：引流站搁置，但是不会放弃',
          '质量更新：引流站将mdui转换成在线载入',
          '测试：本地分支和在线分支x2',
      ]
    },
]

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

