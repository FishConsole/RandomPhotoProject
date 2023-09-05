import datetime
import os
import sqlite3
import jieba


class 审核系统图片标签重构编辑器:
    @staticmethod
    def 基本框架():
        连接器 = sqlite3.connect(os.path.join('数据库', '图片标签重构编辑器.db'))
        # 创建游标对象
        游标对象 = 连接器.cursor()
        # 创建表
        游标对象.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 原始tag, 等待审核tag, PRIMARY KEY (路径))")
        return 游标对象, 连接器

    @staticmethod
    def 提交请求():
        游标对象, 连接器 = 审核系统图片标签重构编辑器.基本框架()
        游标对象.execute("SELECT 路径,标签 FROM 压缩图片信息资源 WHERE 路径 = ?", (filename,))
        row = 游标对象.fetchall()
        # 关闭连接
        连接器.close()
        return row

    @staticmethod
    def 取消更改():
        pass

    @staticmethod
    def 下一张图片():
        pass


审核系统图片标签重构编辑器.提交请求()