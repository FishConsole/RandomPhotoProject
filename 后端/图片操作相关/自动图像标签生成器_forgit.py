import gc  # 内存管理函数
import hashlib
import http.client
import json
import os
import random
import urllib
from typing import Any, Union, Dict


def 百度翻译(文本):
    appid = ''  # 填写你的appid
    secretKey = ''  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'en'  # 原文语种
    toLang = 'zh'  # 译文语种
    salt = random.randint(32768, 65536)
    q = 文本[0:100]
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        return result['trans_result'][0]['dst']

    except Exception as e:
        return e
    finally:
        if httpClient:
            httpClient.close()


def 二次元图片标签自动生成(图片路径: list = None) -> Union[Dict[str, Union[bool, None, str, Dict[Any, Any]]], str]:
    """
    - 二次元图片标签自动生成: 使用deepdanbooru人工智能模型自动为二次元图片生成标签
    - 目标模型和配套资源在RandomPhoto根目录下的DeepDanbooru文件夹中
    - 相对路径示例：'../img/主站压缩图片/123123123_1.png'
    :param 图片路径: 给出一个有效的图片路径，可以是绝对路径或相对路径
    :return: 指定图片的标签数组
    """
    from 后端.后端执行与回调部.执行部门.运维相关 import 自动标签生成器开关

    if 自动标签生成器开关:
        from deepdanbooru import commands

        if 图片路径 is None:
            raise ValueError('给出一个有效的图片路径')
        else:
            输出的内容 = {'error': False, 'message': None, 'result': {}}
            for i in 图片路径:
                # 提取文件的前缀，他会在目标文件夹生成一个同名的txt文件，我们需要获取这数据，获取完后还要删掉
                图片前缀 = i[:-4]
                # 提取图片名称
                图片名称 = i.split('\\')[-1]
                try:
                    # 生成图片标签
                    commands.evaluate(
                        target_paths=[i],
                        project_path='DeepDanbooru',
                        model_path='DeepDanbooru/model.h5',
                        tags_path='DeepDanbooru/tags.txt',
                        threshold=0.4,
                        allow_gpu=True,
                        compile_model=True,
                        allow_folder=False,
                        save_txt=True,  # 保存为txt文件
                        folder_filters=None,
                        verbose=True
                    )

                    print(图片前缀)

                    # 读取txt文件
                    with open(os.path.join(f'{图片前缀}txt'), 'r', encoding='utf-8') as f:
                        # 读取第一行数据
                        标签 = f.readline()
                        f.close()

                    # 删掉txt文件
                    os.remove(os.path.join(f'{图片前缀}txt'))

                    # 对获取的内容进行处理，按空格分割
                    标签 = 标签.split(' ')
                    # 删除逗号
                    标签 = [i.replace(',', '') for i in 标签]
                    标签 = [i.replace('_', ' ') for i in 标签]
                    翻译标签 = []
                    # 使用百度翻译对每一个元素进行翻译，如果翻译的值和输入的值一样就删除这个元素,否则就替换
                    for j in 标签:

                        翻译结果 = 百度翻译(j)
                        if 翻译结果 == j:
                            print(f'自动图像标签生成器 - 翻译前：{j}，翻译后：{翻译结果}，相同，删除')
                        else:
                            print(f'自动图像标签生成器 - 翻译前：{j}，翻译后：{翻译结果}，不同，保留')
                            # 对不应该出现的文字进行替换
                            不应该出现的文字_表 = {
                                '查看器': '屏幕',
                                '独奏': '单独',
                                '褶皱': '褶边',
                                '蛆': '橘',
                                'hakama': '袴',
                                'youtuber': '虚拟主播',
                                'gawr-gura': '古拉',
                                '1': '一',
                                '2': '两',
                                '3': '三',
                                '4': '四',
                                '5': '五',
                                '6': '六',
                                '7': '七',
                                '8': '八',
                                '9': '九',
                                '0': '零',
                            }
                            for 不应该出现的文字 in 不应该出现的文字_表.keys():
                                翻译结果 = 翻译结果.replace(不应该出现的文字, 不应该出现的文字_表[不应该出现的文字])
                            翻译标签.append(翻译结果)

                    # 将这个数据添加到"输出的内容“中
                    print(图片名称)
                    输出的内容['result'][图片名称] = 翻译标签[:-1]

                except UnicodeDecodeError:
                    输出的内容['error'] = True
                    输出的内容['message'] = f'图片 【{i}】 格式错误'
                    return 输出的内容
                except MemoryError:
                    输出的内容['error'] = True
                    输出的内容['message'] = f'服务器内存不足，正在释放服务端内存，请稍后重试'
                    # 释放内存
                    gc.collect()
                    return 输出的内容
                except AttributeError:
                    输出的内容['error'] = True
                    输出的内容['message'] = f'网络异常，翻译接口连接失败'
                    # 释放内存
                    gc.collect()
                    return 输出的内容

            # 释放内存
            gc.collect()
            return json.dumps(输出的内容, ensure_ascii=False)
    else:
        return json.dumps({'error': True, 'message': '自动标签生成器开关未开启'}, ensure_ascii=False)
