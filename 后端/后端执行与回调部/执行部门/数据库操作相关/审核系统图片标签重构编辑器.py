import os
import sqlite3

import jieba

from 后端.后端执行与回调部.回调相关.审核系统.tag审核 import tag审核
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制
from 后端.后端执行与回调部.执行部门.邮件相关.smtp_server import 发送邮件


def 路径控制_审核系统图片标签重构编辑器分部():
    return 路径控制.数据库路径().数据库地址()


def test路径控制_审核系统图片标签重构编辑器分部():
    assert os.path.exists(路径控制_审核系统图片标签重构编辑器分部())


class 审核系统图片标签重构编辑器:
    @staticmethod
    def 基本框架():
        连接器 = sqlite3.connect(路径控制_审核系统图片标签重构编辑器分部())
        # 创建游标对象
        游标对象 = 连接器.cursor()
        # 创建表
        游标对象.execute(
            "CREATE TABLE IF NOT EXISTS 审核系统图片标签重资源 (路径, 原始tag, 等待审核tag, PRIMARY KEY (路径))")
        return 游标对象, 连接器

    @staticmethod
    def 获取原始图片标签(路径):
        连接器 = sqlite3.connect(路径控制_审核系统图片标签重构编辑器分部())
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
            result = tag审核.tag审核_失败(f'提交请求失败：获取原始图片标签失败：{路径}')
            return result

        原始新tag = list(jieba.cut(新tag))
        新tag列表_垃圾处理 = []
        新tag列表_回调字符串 = ''
        for i in 原始新tag:
            if len(i) >= 2:
                新tag列表_垃圾处理.append(i)
        for i in 新tag列表_垃圾处理:
            新tag列表_回调字符串 = 新tag列表_回调字符串 + i
        print(f'路径 - {路径}')
        print(f'原始图片tag - {原始图片tag}')
        print(f'新tag列表_回调字符串 - {新tag列表_回调字符串}')
        回调数据 = tag审核.tag审核_成功(f"提交请求成功：{路径}")
        try:
            游标对象.execute(f"INSERT INTO 审核系统图片标签重资源(路径,原始tag,等待审核tag) VALUES (?, ?, ?)",
                             (路径, 原始图片tag, 新tag列表_回调字符串))
            连接器.commit()
            with open(路径控制.前端资源目录().shenhe_token(), 'r') as f:
                随机数发生器_生成的数字 = f.read()
                f.close()
                发送邮件(
                    f"<h2>RandomPhoto审核系统</h2>有用户提交了tag修改请求，请尽快审核<br>）<br>这里是审核的网址：https://www.root-a.top/admin~/{随机数发生器_生成的数字}/main")
        except sqlite3.IntegrityError as e:
            回调数据 = tag审核.tag审核_失败(f"提交请求失败：{e}")
        return 回调数据

    @staticmethod
    def 取消更改(名字):
        游标对象, 连接器 = 审核系统图片标签重构编辑器.基本框架()
        try:
            游标对象.execute('delete from 审核系统图片标签重资源 where 路径 = ?', (名字,))
            连接器.commit()
            游标对象.close()
            连接器.close()
            result = tag审核.tag审核_成功(f"取消更改成功：{名字}")
            return result
        except Exception as e:
            result = tag审核.tag审核_失败(e)
            return result

    @staticmethod
    def 下一张图片(重构tag, img_name, 第一次加载):
        正式环境_连接器 = sqlite3.connect(路径控制_审核系统图片标签重构编辑器分部())
        正式环境_游标对象 = 正式环境_连接器.cursor()
        重构编辑器_游标对象, 重构编辑器_连接器 = 审核系统图片标签重构编辑器.基本框架()
        result = tag审核.tag审核_成功(img_name)

        def 返回剩下的图片():
            try:
                查询结果 = 重构编辑器_游标对象.execute('SELECT * from 审核系统图片标签重资源 LIMIT 1')
                查询结果 = 查询结果.fetchall()
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
                print(f'result:{result}')
                return result
            except IndexError:
                # 这个情况是因为队列里面没有数据了
                result_e = tag审核.tag审核_失败("审核队列已空")
                return result_e

        def 删除数据():
            正式环境_游标对象.execute('UPDATE 压缩图片信息资源 SET 标签=? where 路径=?', (重构tag, img_name))
            正式环境_连接器.commit()
            重构编辑器_游标对象.execute('delete from 审核系统图片标签重资源 where 路径 = ?', (img_name,))
            重构编辑器_连接器.commit()

        def 关闭数据库():
            正式环境_游标对象.close()
            正式环境_连接器.close()
            重构编辑器_游标对象.close()
            重构编辑器_连接器.close()

        if 第一次加载 == 'true':
            result = 返回剩下的图片()
            关闭数据库()
            return result
        else:
            删除数据()
            result = 返回剩下的图片()
            关闭数据库()
            return result
