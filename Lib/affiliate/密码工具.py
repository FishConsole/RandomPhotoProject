import time

    


def 交换(列表, i, j):
    列表[i], 列表[j] = 列表[j], 列表[i]

def 密钥调度算法(密钥):
    密钥长度 = len(密钥)
    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(密钥[i % 密钥长度])) % 256
        交换(S, i, j)
    
    return S

def 伪随机生成算法(S, 文本):
    i, j, K = 0, 0, []
    for l in range(len(文本)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        交换(S, i, j)
        K.append(chr(ord(文本[l]) ^ S[(S[i] + S[j]) % 256]))
    return ''.join(K)

def RC4(密钥, 文本):
    S = 密钥调度算法(密钥)
    return 伪随机生成算法(S, 文本)

def 转换为十六进制(字符串):
    return ''.join([format(ord(c), '02X') for c in 字符串])

def 从十六进制转换(hex_str):
    return ''.join([chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)])

def 加密(密钥, 文本):
    加密文本 = RC4(密钥, 文本)
    return 转换为十六进制(加密文本).upper()

def 解密(密钥, 加密文本):
    文本 = 从十六进制转换(加密文本)
    解密 = None
    try:
        解密 = int(RC4(密钥, 文本))
    except ValueError:
        解密 = '解密失败'
    return 解密



class 密码工具:
    def __init__(self):
        self.编码方式 = "UTF-8"

        # 密钥 = "AB60F256567AFCBA0310"# 一个无法解密的代码，使用的“你是傻逼吧+时间戳做出来的”
        # 时间大概是 2023年6月19日 17:00:00
        self.密钥 = "AB60F256567AFCBA0310"
        

    def 加密(self,明文):
        return 加密(self.密钥,str(int(time.time())))
        

    def 解密(self,密文):
        return 解密(self.密钥,密文)
        


