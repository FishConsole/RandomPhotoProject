class 文件读写器:
    # 这个类的作用就是把文件读写的操作封装起来，这样可以节省很多的代码
    def __init__(self, 文件名):
        self.文件名 = 文件名

    def 读取(self, 编码='utf-8'):
        with open(self.文件名, 'r', encoding=编码) as f:
            返回值 = f.read()
            f.close()
            return 返回值
        
    def 写入(self, 内容, 编码='utf-8'):
        with open(self.文件名, 'w', encoding=编码) as f:
            f.write(内容)
            f.close()