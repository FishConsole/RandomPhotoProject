import os.path
import sqlite3

import pandas as pd

from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


class 数据库转xlsx:
    @staticmethod
    def 数据库转xlsx(数据库地址=路径控制.数据库路径().数据库地址()):
        conn = sqlite3.connect(database=数据库地址)
        cursor = conn.cursor()
        ###################################################################
        cursor.execute("select * from 压缩图片信息资源")
        data = cursor.fetchall()
        数据表工具 = pd.ExcelWriter(os.path.join(路径控制.临时资源路径().临时excel路径(), 'output.xlsx'))
        df = pd.DataFrame(data, columns=['路径', '版式', '上传时间', '标签'])
        df.to_excel(数据表工具, sheet_name="压缩图片信息资源")
        ###################################################################
        cursor.execute("select * from 审核系统图片标签重资源")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=['路径', '原始tag', '等待审核tag'])
        df.to_excel(数据表工具, sheet_name="审核系统图片标签重资源")
        ###################################################################
        数据表工具.close()
        cursor.close()
        conn.close()


print(数据库转xlsx().数据库转xlsx())
