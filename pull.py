import subprocess
import time

# 设置远程仓库的名称、本地分支和远程分支名称
远程仓库名称 = 'origin'
本地分支名称 = '数据港口【出】'
远程分支名称 = 'main'

while True:
    # 执行 git push 命令，并请求输入用户名和密码
    git_push_command = ['git', '-c', 'credential.helper=', '-c', 'core.quotepath=false', '-c', 'log.showSignature=false', 'push', '--progress', '--porcelain', 远程仓库名称, f'{本地分支名称}:{远程分支名称}', '--follow-tags']
    结果 = subprocess.run(git_push_command, capture_output=True, text=True)

    # 获取命令的标准输出和标准错误输出
    标准输出 = 结果.stdout
    标准错误输出 = 结果.stderr

    # 检查提交是否成功
    if "Everything up-to-date" in 标准输出:
        print("提交成功，停止循环。")
        break
    elif "fatal: unable to access" in 标准错误输出:
        print(f"无法访问远程仓库，检查远程仓库的URL和凭据。{标准错误输出}")
    else:
        print(f"提交失败，等待一段时间后重试。{标准错误输出}")
        time.sleep(0)  # 休眠60秒后重试
