# 导入所需的库和类
# 操作文件和目录的模块
import os
# 处理时间的模块
import time
# 发送HTTP请求的库
import requests
# Selenium库中的浏览器驱动模块，用于模拟浏览器操作
from selenium import webdriver
# 定位元素的方式，用于定位网页元素
from selenium.webdriver.common.by import By
# Edge浏览器特定的选项配置
from selenium.webdriver.edge.options import Options
# 用于等待特定条件的模块
from selenium.webdriver.support.ui import WebDriverWait
# 预期条件，用于等待特定的元素状态
from selenium.webdriver.support import expected_conditions as EC

def 网易云爬虫_直链提供器(驱动程序):
    驱动程序.get('https://music.163.com/playlist?id=7569174381')
    嵌套页面 = 驱动程序.find_element(By.CSS_SELECTOR, '#g_iframe')
    驱动程序.switch_to.frame(嵌套页面)

    链接组 = 驱动程序.find_elements(By.XPATH, "//body//tbody//span[@class='txt']/a")
    歌名组 = 驱动程序.find_elements(By.XPATH, "//body//tbody//span[@class='txt']/a/b")

    结果 = []
    for 链接, 歌名 in zip(链接组, 歌名组):
        直链标识 = 链接.get_attribute('href').split('=')[1]
        直链 = f'https://music.163.com/song/media/outer/url?id={直链标识}.mp3'
        结果.append([直链, 歌名.text.replace('\n', '')])

    return 结果


def 下载歌曲(直链, 歌名):
    首选项 = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
    Edge选项 = Options()
    Edge选项.add_experimental_option("prefs", 首选项)
    驱动程序 = webdriver.Edge(options=Edge选项)
    驱动程序.get(直链)

    try:
        WebDriverWait(驱动程序, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'source')))
        媒体源 = 驱动程序.find_element(By.TAG_NAME, 'source').get_attribute("src")
        响应 = requests.get(媒体源)
        with open(os.path.join(f'{歌名}.mp3'), 'wb') as 文件:
            文件.write(响应.content)
        print(f'已下载：{歌名}')
    except Exception as 错误:
        print(f'下载失败：{歌名}')
        print(错误)

    驱动程序.quit()


def 网易云爬虫_音乐下载器():
    print('等待直链池')
    Edge选项 = Options()
    Edge选项.page_load_strategy = 'eager'
    # Edge选项.add_argument('--headless')
    首选项 = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
    Edge选项.add_experimental_option("prefs", 首选项)
    驱动程序 = webdriver.Edge(options=Edge选项)

    try:
        直链池 = 网易云爬虫_直链提供器(驱动程序)
        for 直链, 歌名 in 直链池:
            print(f'下载{歌名}')
            下载歌曲(直链, 歌名)
            time.sleep(1)  # 给下载一些间隔时间，避免对服务器造成过大压力
    finally:
        驱动程序.quit()
