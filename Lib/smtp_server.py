# -*- coding: utf-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from Lib.programe.调试模式 import 调试模式


def 发送邮件(内容):
    if 调试模式() == False:
        try:
            邮件服务器 = "smtp.qq.com"
            邮件用户 = "2645602049@qq.com"
            鉴权码 = "wodmfpzkrbuwdjhd"
            发件人昵称 = "来自RandomPhoto的消息"
            发件人邮箱 = "2645602049@qq.com"

            # 2460661806 海纳
            # 602116613 鱼几斤小号
            # 2780043482 青蛙小号
            收件人 = ["602116613@qq.com",
                   "2460661806@qq.com",
                   "2780043482@qq.com"]

            正文 = 内容

            msg = MIMEText(正文, "plain", "utf-8")
            发件人 = f'"{Header(发件人昵称, "utf-8").encode()}" <{发件人邮箱}>'
            msg['From'] = 发件人
            msg['To'] = Header("收件人", "utf-8")
            主标题 = "RandomPhoto项目_邮件发射器"
            msg['Subject'] = Header(主标题, "utf-8")

            smtp服务器 = smtplib.SMTP(邮件服务器, 587)
            smtp服务器.starttls()
            smtp服务器.login(邮件用户, 鉴权码)
            smtp服务器.sendmail(发件人邮箱, 收件人, msg.as_string())
            smtp服务器.quit()
            print("邮件发送成功")
        except Exception as e:
            print(f'邮件发送系统：邮件发送失败 - {e}')
    else:
        print('邮件发送系统：调试模式，不发送邮件')


