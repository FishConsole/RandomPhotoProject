import os.path
import socket

import requests

from 后端.后端执行与回调部.执行部门.运维相关.缓存相关.配置文件管理器 import 配置文件管理器
from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制


def IPv6获取工具():
    try:
        result = requests.get("https://api6.ipify.org/", timeout=1).text
        return result
    except Exception as e:
        print(f"IPv6获取工具报错：{e}")
        return "::1"


def IPv4获取工具():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        print(f"IPv6获取工具报错：{e}")
        return "::1"

