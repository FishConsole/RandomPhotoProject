import datetime
import json
import os
import sqlite3
import jieba
from Lib.依赖.回调相关.审核系统.tag审核 import tag审核


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
        return 回调

    @staticmethod
    def 提交请求(路径, 新tag):
        游标对象, 连接器 = 审核系统图片标签重构编辑器.基本框架()
        try:
            原始图片tag = 审核系统图片标签重构编辑器.获取原始图片标签(路径)[0][0]
        except IndexError:
            return {'内容': '服务端错误'}
        原始新tag = list(jieba.cut(新tag))
        新tag列表_垃圾处理 = []
        新tag列表_回调字符串 = ''
        for i in 原始新tag:
            if len(i) >= 2:
                新tag列表_垃圾处理.append(i)
        for i in 新tag列表_垃圾处理:
            新tag列表_回调字符串 = 新tag列表_回调字符串 + i

        print(路径)
        print(原始图片tag)
        print(新tag列表_回调字符串)

        游标对象.execute(f"INSERT INTO 审核系统图片标签重资源(路径,原始tag,等待审核tag) VALUES (?, ?, ?)",
                         (路径, 原始图片tag, 新tag列表_回调字符串))
        连接器.commit()
        连接器.close()

        回调数据 = tag审核.提交请求.提交请求_成功(路径)
        回调数据['原始图片tag'] = 原始图片tag
        回调数据['新tag'] = 新tag
        return 回调数据

    @staticmethod
    def 取消更改(名字):
        游标对象, 连接器 = 审核系统图片标签重构编辑器.基本框架()
        游标对象.execute('delete from 审核系统图片标签重资源 where 路径 = ?', 名字)
        连接器.commit()
        游标对象.close()
        连接器.close()
        result = tag审核.提交请求.提交请求_成功('取消更改成功')
        return result

    @staticmethod
    def 下一张图片(重构tag, img_name, 第一次加载):
        重构编辑器_游标对象, 重构编辑器_连接器 = 审核系统图片标签重构编辑器.基本框架()
        正式环境_连接器 = sqlite3.connect(os.path.join('数据库', '图片信息资源.db'))
        正式环境_游标对象 = 正式环境_连接器.cursor()
        查询结果 = 重构编辑器_游标对象.execute('SELECT * from 审核系统图片标签重资源 LIMIT 1')
        查询结果 = 查询结果.fetchall()
        result = tag审核.提交请求.提交请求_成功('')
        try:
            查询结果 = 查询结果[0]
            路径 = 查询结果[0]
            原始tag = list(jieba.cut(查询结果[1]))
            新tag = list(jieba.cut(查询结果[2]))
            原始tag_字符串 = ''
            新tag_字符串 = ''
            for i in 原始tag:
                原始tag_字符串 = 原始tag_字符串 + '|' + i
            for i in 新tag:
                新tag_字符串 = 新tag_字符串 + '|' + i
            result['数据'] = [路径, 原始tag_字符串, 新tag_字符串]
            print(img_name)
            if 第一次加载 != 'true':
                正式环境_游标对象.execute('UPDATE 压缩图片信息资源 SET 标签=? where 路径=?', (重构tag, img_name))
                正式环境_连接器.commit()
                重构编辑器_游标对象.execute('delete from 审核系统图片标签重资源 where 路径 = ?', (img_name,))
                重构编辑器_连接器.commit()
            return result
        except IndexError:
            # 这个情况是因为队列里面没有数据了
            result = tag审核.下一张图片.审核队列已空()
            return result
        finally:
            # 关闭游标和连接
            正式环境_游标对象.close()
            正式环境_连接器.close()
            重构编辑器_游标对象.close()
            重构编辑器_连接器.close()
