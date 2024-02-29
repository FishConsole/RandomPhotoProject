import datetime
import os
import sqlite3
import unittest

import jieba

from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


class 图片信息资源管理器:
    def __init__(self):
        self.conn = sqlite3.connect(路径控制.数据库路径().数据库地址())

    def 站点地图生成器_获取全部图片信息(self):
        # 创建游标对象
        cur = self.conn.cursor()
        # 创建表
        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
        # 获取数据
        cur.execute("SELECT 路径,上传时间,标签 FROM 压缩图片信息资源")
        row = cur.fetchall()
        # 关闭连接
        self.conn.close()
        return row

    def 获取指定页数的压缩图片信息资源(self, 页码):
        # 创建游标对象
        游标 = self.conn.cursor()
        # 创建表
        游标.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")

        # 获取全部图片的数量
        游标.execute("SELECT 路径 FROM 压缩图片信息资源")
        全部图片的数量 = 游标.fetchall()

        # 获取数据
        页码 = int(页码)
        每页记录数 = 10
        总记录数 = len(全部图片的数量)
        起始位置 = max(总记录数 - (页码 * 每页记录数), 0)

        游标.execute("SELECT 路径, 标签 FROM 压缩图片信息资源 LIMIT ?, ?", (起始位置, 每页记录数))
        # 倒排
        结果行 = 游标.fetchall()
        # 关闭连接
        return 结果行

    def 获得最新上传的图片(self):
        cur = self.conn.cursor()
        # 创建表
        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
        # 获取数据
        # 当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        cur.execute(f"SELECT 路径,标签 FROM 压缩图片信息资源 where 上传时间 = '{now}'")
        row = cur.fetchall()
        # 关闭连接
        self.conn.close()
        return row

    def 获取指定_压缩_图片信息资源(self, filename):
        # 创建游标对象
        cur = self.conn.cursor()
        # 创建表
        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
        cur.execute("SELECT 路径,标签 FROM 压缩图片信息资源 WHERE 路径 = ?", (filename,))
        row = cur.fetchall()
        # 关闭连接
        self.conn.close()
        return row

    def 搜索压缩图片信息资源(self, 标签名):
        # 创建游标对象
        cur = self.conn.cursor()
        # 创建表
        # 防止有人恶意上传太多的请求
        标签名 = 标签名[:100]

        # 把标签进行分割
        # 分割的方式是空格分割和逗号分割
        jieba.load_userdict(os.path.join(路径控制.前端资源目录().分词库(), "dict.txt"))
        jieba.load_userdict(os.path.join(路径控制.前端资源目录().分词库(), "output.txt"))
        标签名 = list(jieba.cut(标签名))

        # 删除长度为1的内容
        def 自定义搜索引擎(词组列表):
            # 分词，获取词组列表
            # 记录加号是否已经生效
            加号已生效 = False

            # 迭代器用于遍历词组列表
            迭代器 = iter(词组列表)

            # 结果列表，用于存储处理后的词组
            结果 = []

            try:
                for 词组 in 迭代器:
                    # 检测到非加号时，根据是否加号生效来决定是否添加到结果列表
                    if 加号已生效 and len(词组) == 1:
                        # 如果加号生效且当前词组只有一个字符，则保留当前词组
                        结果.append(词组)
                        # 保持加号只生效一次
                        加号已生效 = False
                    elif len(词组) > 1:
                        # 如果当前词组长度大于1，则保留当前词组
                        结果.append(词组)
                return 结果
            except StopIteration:
                return []

        标签名 = 自定义搜索引擎(标签名)
        标签名 = ''.join(标签名)
        标签名 = list(标签名)
        查询字符串 = ''
        for a in 标签名:
            查询字符串 = 查询字符串 + f" 标签 like '%{a}%'" + ' OR'

        # 去掉最后一个'or'
        查询字符串 = 查询字符串[:-3]
        cur.execute(f"SELECT 路径, 标签 FROM 压缩图片信息资源 WHERE {查询字符串}")

        row = cur.fetchall()
        # 关闭连接
        self.conn.close()
        return row[:30]

    @staticmethod
    def 获取指定_版式_压缩图片信息资源(板式, 范围=None):
        # 如果范围参数为空，则不添加范围条件
        板式查询字符串 = ''
        标签查询字符串 = 'AND '
        if 板式 == '竖屏':
            板式查询字符串 = f"版式 like '%竖屏%' or 版式 like '%平板%'"
        else:
            板式查询字符串 = f"版式 like '%{板式}%'"

        if 范围 is not None:
            # 如果范围参数不为空，则添加范围条件
            jieba.load_userdict(os.path.join(路径控制.前端资源目录().分词库(), "dict.txt"))
            jieba.load_userdict(os.path.join(路径控制.前端资源目录().分词库(), "output.txt"))
            标签名 = list(jieba.cut(范围))
            倒排标签名 = []
            for a in 标签名:
                倒排标签名.insert(0, a)
            for a in 倒排标签名:
                标签查询字符串 = 标签查询字符串 + f" 标签 like '%{a}%' or"
            标签查询字符串 = 标签查询字符串[:-3]
        else:
            标签查询字符串 = ''

        # 创建游标对象
        地址 = 路径控制.数据库路径().数据库地址()
        connection = sqlite3.connect(地址)
        cur = connection.cursor()

        # 创建表（仅在首次运行时创建）
        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径 text, 版式 text, 上传时间 text, 标签 text , PRIMARY KEY (路径))"
        )

        # 构建并执行查询语句
        查询字符串 = f"SELECT 路径 FROM 压缩图片信息资源 WHERE {板式查询字符串} {标签查询字符串}"
        print(f"\n{板式}: {查询字符串}")
        cur.execute(查询字符串)

        # 获取所有数据
        rows = cur.fetchall()

        # 关闭数据库连接
        connection.close()

        return rows

    def 写入压缩图片信息资源(self, 路径, 版式, 标签):
        print(f'审核系统当前运行路径：{os.getcwd()}')
        try:
            # 创建游标对象
            cur = self.conn.cursor()
            # 创建表
            cur.execute(
                "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
            # 插入数据
            cur.execute("INSERT INTO 压缩图片信息资源(路径,版式,上传时间,标签) VALUES (?, ?, ?, ?)",
                        (路径, 版式, datetime.date.today(), 标签))
            # 提交更改
            self.conn.commit()
            # 关闭连接
            cur.close()
        except sqlite3.IntegrityError as e:
            print(f'图片一致性维护-写入压缩图片信息资源: {路径} 已经存在: {e}')

    def 删除压缩图片信息资源(self, 路径):
        # 创建游标对象
        cur = self.conn.cursor()
        # 创建表
        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
        # 删除数据
        cur.execute("DELETE FROM 压缩图片信息资源 WHERE 路径 = ?", (路径,))
        # 提交更改
        self.conn.commit()
        # 关闭连接
        cur.close()


class test图片信息资源管理器(unittest.TestCase):
    def test全部图片信息(self):
        获取全部图片信息 = 图片信息资源管理器().站点地图生成器_获取全部图片信息()
        print(f"获取全部图片信息: {获取全部图片信息}")
        assert len(获取全部图片信息) > 0

    def test横屏图片信息(self):
        横屏压缩图片信息资源 = 图片信息资源管理器().获取指定_版式_压缩图片信息资源('横屏')
        横屏压缩图片信息资源_Tag = 图片信息资源管理器().获取指定_版式_压缩图片信息资源('横屏', "测试")
        print(f"获取指定_电脑版式_压缩图片信息资源: {横屏压缩图片信息资源}")
        print(f"获取指定_电脑版式_压缩图片信息资源: {横屏压缩图片信息资源_Tag}")
        assert len(横屏压缩图片信息资源) > 0
        assert len(横屏压缩图片信息资源_Tag) > 0

    def test竖屏图片信息(self):
        竖屏压缩图片信息资源 = 图片信息资源管理器().获取指定_版式_压缩图片信息资源('竖屏')
        竖屏压缩图片信息资源_Tag = 图片信息资源管理器().获取指定_版式_压缩图片信息资源('竖屏', "雪球")
        print(f"获取指定_竖屏版式_压缩图片信息资源: {竖屏压缩图片信息资源}")
        print(f"获取指定_竖屏版式_压缩图片信息资源: {竖屏压缩图片信息资源_Tag}")
        assert len(竖屏压缩图片信息资源) > 1
        assert len(竖屏压缩图片信息资源_Tag) > 0

    def test平板图片信息(self):
        平板压缩图片信息资源 = 图片信息资源管理器().获取指定_版式_压缩图片信息资源('平板')
        平板压缩图片信息资源_Tag = 图片信息资源管理器().获取指定_版式_压缩图片信息资源('平板', "测试")
        print(f"获取指定_平板版式_压缩图片信息资源: {平板压缩图片信息资源}")
        print(f"获取指定_平板版式_压缩图片信息资源: {平板压缩图片信息资源_Tag}")
        assert len(平板压缩图片信息资源) > 0
        assert len(平板压缩图片信息资源_Tag) > 0
