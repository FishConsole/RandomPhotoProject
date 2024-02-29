import xml.etree.ElementTree as ET

from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


def 生成站点地图(资源):
    根 = ET.Element("urlset", xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')

    # 创建Sitemap索引的注释
    注释 = ET.Comment('生成站点地图开始')
    根.append(注释)

    for 解包 in 资源:
        优先级 = 解包['优先级']
        全部图片信息 = 解包['图片信息资源']
        分类 = 解包['分类']

        if 分类 == 'info':
            for 链接 in 全部图片信息:
                url = ET.SubElement(根, "url")

                地址 = ET.SubElement(url, "loc")
                地址.text = f'https://{路径控制.启动位置.域名()}/PhotoInfo/{链接[0]}'

                # 最后修改时间 = ET.SubElement(url, "lastmod")
                # 最后修改时间.text = 链接[1]
                #
                # 更新频率 = ET.SubElement(url, "changefreq")
                # 更新频率.text = 'never'
                #
                # 优先级元素 = ET.SubElement(url, "priority")
                # 优先级元素.text = 优先级
                #
                # 描述 = ET.SubElement(url, "description")
                # 描述.text = 链接[2]

    return ET.tostring(根, encoding="utf-8").decode("utf-8")

# 生成的XML = 生成图片信息([
#     {'图片信息资源': 图片信息资源管理器.站点地图生成器_获取全部图片信息()[:5], '优先级': '0.5'},
# ])
#
# print(生成的XML)
