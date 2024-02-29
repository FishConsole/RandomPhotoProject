import time

class 线程锁变量编辑器:
    def __init__(self,锁, 共享变量集合):
        self.共享变量集合 = 共享变量集合
        self.锁 = 锁

    def 线程锁变量获取(self,目标变量):
        计数器 = 0
        while True:
            self.锁.acquire()
            try:
                # 从键值对读取指定的值
                值 = self.共享变量集合[目标变量]
                if 值 == None:
                    return {}
                else:
                    return 值
            except Exception:
                # 读取失败，继续循环
                pass
            finally:
                # 释放锁
                try:
                    self.锁.release()
                except RuntimeError:
                    pass
                # 没有值的情况
                计数器 = 计数器 + 1
                if 计数器 > 20:
                    return {}
                time.sleep(0.001)
    
    def 线程锁变量修改(self,目标变量,值):
        计数器 = 0
        while True:
            # 获取锁：
            self.锁.acquire()
            try:
                # 开始修改
                self.共享变量集合[目标变量] = 值
                self.锁.release()
                break
            except Exception:
                pass
            finally:
                # 释放锁
                try:
                    self.锁.release()
                except RuntimeError:
                    pass
                # 防止死循环
                计数器 = 计数器+1
                if 计数器 > 20:
                    break
                time.sleep(0.001)