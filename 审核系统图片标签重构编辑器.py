import datetime
import os
import sqlite3
import jieba


class 审核系统图片标签重构编辑器:
    @staticmethod
    def 基本框架():
        连接器 = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        # 创建游标对象
        游标对象 = 连接器.cursor()
        # 创建表
        游标对象.execute(
            "CREATE TABLE IF NOT EXISTS 审核系统图片标签重资源 (路径, 原始tag, 等待审核tag, PRIMARY KEY (路径))")
        return 游标对象, 连接器

    @staticmethod
    def 获取原始图片标签(路径):
        连接器 = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        # 创建游标对象
        游标对象 = 连接器.cursor()
        # 获取资源
        游标对象.execute(f"select 标签 from 压缩图片信息资源 where 路径 = '{路径}'")
        回调 = 游标对象.fetchall()
        连接器.close()
        return 回调[0][0]

    @staticmethod
    def 提交请求(路径, 新tag):
        游标对象, 连接器 = 审核系统图片标签重构编辑器.基本框架()
        原始图片tag = 审核系统图片标签重构编辑器.获取原始图片标签(路径)
        游标对象.execute(f"SELECT INTO 审核系统图片标签重资源('路径','原始tag','等待审核tag') value ('{路径}','{原始图片tag}','{新tag}')")
        连接器.close()
        # return 回调中心.审核系统.

    @staticmethod
    def 取消更改():
        pass

    @staticmethod
    def 下一张图片():
        pass


print(审核系统图片标签重构编辑器.获取原始图片标签('20230715080726.jpg'))
