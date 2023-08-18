import datetime
import os
import sqlite3
import time

import jieba

from Lib.图片压缩库 import ResizeImage
from Lib.图片路径提取 import 图片路径提取
from Lib.路径控制 import 路径控制


# 压缩成功之后这个图片才是可以使用的
# 因此存入数据库的压缩图片的信息

class 图片信息资源管理器:

    @staticmethod
    def 站点地图生成器_获取全部图片信息():
        conn = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        # 创建游标对象
        cur = conn.cursor()
        # 创建表
        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
        # 获取数据
        cur.execute("SELECT 路径,上传时间,标签 FROM 压缩图片信息资源")
        row = cur.fetchall()
        # 关闭连接
        conn.close()
        return row

    @staticmethod
    def 获取指定页数的压缩图片信息资源(页码):
        连接 = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        # 创建游标对象
        游标 = 连接.cursor()
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
        连接.close()
        return 结果行

    @staticmethod
    def 获得最新上传的图片():
        conn = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        # 创建游标对象
        cur = conn.cursor()
        # 创建表

        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
        # 获取数据
        # 当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        cur.execute(f"SELECT 路径,标签 FROM 压缩图片信息资源 where 上传时间 = '{now}'")
        print(f"SELECT 路径,上传时间 FROM 压缩图片信息资源 where 上传时间 = '{now}'")
        row = cur.fetchall()
        # 关闭连接
        conn.close()
        return row

    @staticmethod
    def 获取指定_压缩_图片信息资源(filename):
        conn = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        # 创建游标对象
        cur = conn.cursor()
        # 创建表
        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
        cur.execute("SELECT 路径,标签 FROM 压缩图片信息资源 WHERE 路径 = ?", (filename,))
        row = cur.fetchall()
        # 关闭连接
        conn.close()
        return row

    @staticmethod
    def 搜索压缩图片信息资源(标签名):
        conn = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        # 创建游标对象
        cur = conn.cursor()
        # 创建表
        # 防止有人恶意上传太多的请求
        标签名 = 标签名[:100]

        # 把标签进行分割
        # 分割的方式是空格分割和逗号分割
        标签名 = list(jieba.cut(标签名))
        # 删除长度为1的内容

        print(标签名)

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
                    if 词组 == '+':
                        # 检测到加号时，将加号标记设为True，并添加加号到结果列表
                        加号已生效 = True
                    else:
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
        print(标签名)
        查询字符串 = ''
        for a in 标签名:
            查询字符串 = 查询字符串 + f" 标签 like '%{a}%'" + ' and'

        # 去掉最后一个'or'
        查询字符串 = 查询字符串[:-3]
        print(查询字符串)
        cur.execute(f"SELECT 路径, 标签 FROM 压缩图片信息资源 WHERE {查询字符串}")

        row = cur.fetchall()
        # 关闭连接
        conn.close()
        return row[:30]

    @staticmethod
    def 获取指定_版式_压缩图片信息资源(model, 范围=None):

        # 如果range中没有任何内容，就不生成对应的查询字符串
        if 范围 is None: 查询字符串_range = ''
        else: 查询字符串_range = f" and 标签 like '%{范围}%'"

        conn = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        # 创建游标对象
        cur = conn.cursor()
        # 创建表
        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
        # 获取数据
        # 他会接收两个版式参数，一个是横屏，一个是竖屏
        # 数据库中有两个字段，筛选然后返回即可
        cur.execute(f"SELECT 路径 FROM 压缩图片信息资源 WHERE 版式 = '{model}'{查询字符串_range}")
        row = cur.fetchall()
        # 关闭连接
        conn.close()
        return row

    @staticmethod
    def 写入压缩图片信息资源(路径, 版式, 标签):
        try:
            conn = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
            # 创建游标对象
            cur = conn.cursor()
            # 创建表
            cur.execute(
                "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
            # 插入数据
            cur.execute("INSERT INTO 压缩图片信息资源(路径,版式,上传时间,标签) VALUES (?, ?, ?, ?)",
                        (路径, 版式, datetime.date.today(), 标签))
            # 提交更改
            conn.commit()
            # 关闭连接
            cur.close()
        except sqlite3.IntegrityError as e:
            print(f'重新读取-写入压缩图片信息资源: {路径} 已经存在: {e}')

    @staticmethod
    def 删除压缩图片信息资源(路径):
        # 创建或打开sqlite数据库
        conn = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        # 创建游标对象
        cur = conn.cursor()
        # 创建表
        cur.execute(
            "CREATE TABLE IF NOT EXISTS 压缩图片信息资源 (路径, 版式, 上传时间, 标签 text , PRIMARY KEY (路径))")
        # 删除数据
        cur.execute("DELETE FROM 压缩图片信息资源 WHERE 路径 = ?", (路径,))
        # 提交更改
        conn.commit()
        # 关闭连接
        cur.close()


def 重新读取_():
    count = 0
    while True:
        count = count + 1
        if count > 999:
            count = 0
        # print('重新读取：开启重新读取')
        time.sleep(5)

        图片信息资源 = 图片路径提取(路径控制.主站原始图片_路径())
        压缩图片信息资源 = 图片路径提取(路径控制.主站压缩图片_路径())

        for 图片名字 in 图片信息资源.keys():
            if not os.path.exists(os.path.join(路径控制.主站压缩图片_路径(), 图片名字)):
                print(f"重新读取：生成主页缩略图 {图片名字}")
                文件输入 = os.path.join(路径控制.主站原始图片_路径(), 图片名字)
                文件输出 = os.path.join(路径控制.主站压缩图片_路径(), 图片名字)
                ResizeImage(文件输入, 文件输出)
                #############################################################################
                # 本来这里应该存数据库里面的，但是后来这玩意儿由于要存标签于是这个工作就由审核系统接管了
                # 图片信息资源管理器.写入压缩图片信息资源(图片名字, 图片大小检测(
                #     os.path.join(路径控制.主站压缩图片_路径(), 图片名字)))

        for 图片名字 in 压缩图片信息资源.keys():
            try:
                if not os.path.exists(os.path.join(路径控制.主站原始图片_路径(), 图片名字)):
                    os.remove(os.path.join(路径控制.主站压缩图片_路径(), 图片名字))

                    print(f"重新读取：未发现对应的主站原始图片，删除主页缩略图 {图片名字}")

                    # 删除数据库中的对应数据
                    # 如果转义了可能会导致无法删除，因此要阻止转义

                    # 如果是第一次运行，就有路径，第二次运行，从数据库中取出带有路径的，因此要阻止路径
                    图片信息资源管理器.删除压缩图片信息资源(图片名字)
            except FileNotFoundError as 错误信息:
                # 这种情况是数据库那边的问题，或者文件真的不存在
                print(f'重新读取：出现异常 - 文件不存在 {错误信息}')
                pass

        print(f'重新读取：主页缩略图与原图索引重新建立操作完成 - {count}')
