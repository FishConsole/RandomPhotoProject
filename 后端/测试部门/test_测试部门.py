import unittest

from 前端.接口部门.图片返回相关.图片搜索接口.图片搜索接口 import test_Search
from 前端.接口部门.图片返回相关.图片返回器 import test图片返回器
from 前端.接口部门.存活报告.存活报告 import test_Survive
from 前端.接口部门.文件上传相关.文件上传器 import test路径控制_文件上传器分部
from 前端.接口部门.管理员系统相关.Tag生成器 import test路径控制_自动标签生成器分部
from 前端.模板部门.ChangeLog页面.ChangeLog页面 import test_ChangeLog
from 前端.模板部门.index页面.index页面 import test_index页面
from 前端.模板部门.photoinfo页面.photoinfo页面 import test_PhotoInfo
from 前端.模板部门.根页面.根页面 import test_index
from 后端.后端执行与回调部.执行部门.数据库操作相关.图片信息资源管理器 import test图片信息资源管理器
from 后端.后端执行与回调部.执行部门.数据库操作相关.审核系统图片标签重构编辑器 import test路径控制_审核系统图片标签重构编辑器分部
from 后端.后端执行与回调部.执行部门.运维相关.版本号提取 import test版本号提取
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import test路径控制
from 后端.图片操作相关.审核系统 import test路径控制_管理员系统分部
from 后端.图片操作相关.随机图片发生器 import test随机图片发生器
from 并发控制部.图片一致性维护.图片一致性维护_业务环境 import test图片一致性维护
from 并发控制部.图片一致性维护.图片一致性维护_审核系统 import test图片一致性维护_审核队列
from 并发控制部.审核系统缩略图生成器.审核系统缩略图生成器 import test审核系统缩略图生成器


class test测试部门总部(unittest.TestCase):
    """
    测试部门负责收集每一个子部门的测试部门并集中运行
    :return:
    """

    def test_路径控制s(self):
        test路径控制()

    def test图片一致性维护_审核队列s(self):
        test图片一致性维护_审核队列()

    def test图片一致性维护s(self):
        test图片一致性维护()

    def test审核系统缩略图生成器s(self):
        test审核系统缩略图生成器()

    def test图片信息资源管理器s(self):
        test图片信息资源管理器()

    def test_index页面s(self):
        test_index页面()

    def test图片返回器s(self):
        test图片返回器()

    def test随机图片发生器s(self):
        test随机图片发生器()

    def test_Photo信息s(self):
        test_PhotoInfo()

    def test_Search_s(self):
        test_Search()

    def test_index_s(self):
        test_index()

    def test_ChangeLog_s(self):
        test_ChangeLog()

    def test_Survive_s(self):
        test_Survive()

    def test路径控制_文件上传器分部s(self):
        test路径控制_文件上传器分部()

    def test路径控制_自动标签生成器分部s(self):
        test路径控制_自动标签生成器分部()

    def test路径控制_管理员系统分部s(self):
        test路径控制_管理员系统分部()

    def test路径控制_审核系统图片标签重构编辑器分部s(self):
        test路径控制_审核系统图片标签重构编辑器分部()

    def test版本号提取s(self):
        test版本号提取()
