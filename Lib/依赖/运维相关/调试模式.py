# 调试模式的作用是改变程序的运行状态，比如把开启自动死亡线程，不发送邮件等
def 调试模式():
    return True


# 回环模式的作用是让程序在127.0.0.1的模式下运行，否则从路径控制中提取目标ip启动
def 调试模式_回环模式():
    return True


# 国内模式的作用是服务端如果不在国内的话，自动补全缺失库的功能将因为pypi的速度而慢很多，因此启动国内模式
# 就相当于启动pypi的清华源模式（至少目前是这样的）
def 调试模式_国内模式():
    return True


# 由于自动标签生成器这个功能需要太大的内存占用，为了避免因为服务端自身性能不足的问题而导致整个程序组无法在
# 此服务端上运行，特地设置了这个开关，未开启时将会返回错误：此功能未开启的报错
def 自动标签生成器开关():
    return False
