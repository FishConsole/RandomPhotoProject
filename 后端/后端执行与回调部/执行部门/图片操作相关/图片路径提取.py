# encoding: utf-8
# 上面的代码是为了保证在默认使用ASCII的系统中也能正常运行
# 忆雨架构：在5000个函数中如何快速定位某个函数，怎么快怎么来，非必要不用循环，发挥python恐怖的优势
def 图片路径提取(路径):
    import os

    # 图片目录，程序将在此查找所有的图片
    
    # 遍历目录
    图片字典 = {}
    # 先定义一个计数器，这个计数器就用来防止ID重复的情况
    # 为什么要用这种方式来定义变量，因为这种方法可以有效避免变量名重复定义造成的可读性与非报红出错的可追溯溯doge的问题
    ID变量组 = {'计数器': 0}
    
    for 初始图片数据 in os.listdir(路径):
        # 分割文件名和路径
        被分割的数组 = 初始图片数据.split(".")
    
        # 获取文件名和路径
        文件名 = 被分割的数组[0]
        后缀 = 被分割的数组[1]
    
        # 判断是否为png，jpeg，jpg
        # 成功则启动插入模式
        # 插入模式状态下将会获取其他文件，比如"文件名_info.txt",这个文件是用来输出对应图片的详细信息的，在第二个路由
        # 默认为False，这样就不会启动
        插入模式 = 后缀 in ['png', 'jpeg', 'jpg']
        if 插入模式:
            # 这个地方不需要去close，他不会造成内存泄露，因为变量值会被覆盖
            # 注意，我们是以gbk的编码来读取文件的，因为我们的文件是gbk编码的
            try:
                详细信息 = open('info/' + 文件名 + '.txt', encoding='gbk').read()
            except FileNotFoundError:
                详细信息 = '暂无信息'
        else:
            # 如果没有启动插入模式，那就意味这这个文件不是图片，那么就跳过
            continue
        

    
        # 图片ID就是photo_1，第二张就是photo_2，值就是一个列表
        # 它里面存放的是物理路径和图片的介绍，两张图片的具体的数据类型就是{"photo_1":["路径","信息"],"photo_2":["路径","信息"]}
    
        # 每迭代一次计数器就增加一次
        ID变量组['计数器'] += 1
    

        # 如果是插入模式，那么就将图片的名字和路径存入字典
        图片字典[文件名+'.'+后缀] = [文件名+'.'+后缀,详细信息]
        
    return  图片字典
    