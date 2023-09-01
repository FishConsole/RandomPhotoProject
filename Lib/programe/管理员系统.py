import os

from flask import Blueprint, render_template

from Lib.programe.审核系统 import 审核, 删除审核图片, 通过审核图片
from Lib.依赖.运维相关.调试模式 import 调试模式
from Lib.依赖.图片操作相关.自动图像标签生成器 import 二次元图片标签自动生成

admin_page_bp = Blueprint('admin_page', __name__)
admin_AutoTag_page_bp = Blueprint('admin_AutoTag_page', __name__)
admin_shenhe_page_bp = Blueprint('admin_shenhe_page', __name__)

admin_DeletePhoto_bp = Blueprint('admin_DeletePhoto', __name__)
admin_PassPhoto_bp = Blueprint('admin_PassPhoto', __name__)
admin_AutoTag_bp = Blueprint('admin_AutoTag', __name__)


def 错误页面():
    return """

    <h1>访问遭到拒绝</h1>
    <p>token失效或不正确，您无法进入审核页面</p>
    <p style="color:red">如果您不知道token，您可以采取以下方法获得token</p>
    <p>1. 查看根目录下的shenhe_token文件</p>
    <p>2. 查看审核系统向项目所有的管理员发送的最新审核邮件</p>
    <label for="input">请输入新的token：</label>
    <input type="text" id="input" name="input">
    <button onclick="转到()">开始</button>
    <script>
        function 转到() {
            用户输入 = document.getElementById("input").value;

            if (用户输入 == '') return 0;
            else {
                localStorage.setItem("token", 用户输入);
                window.location.href = "../shenhe/"+用户输入;
            }
        }

        document.addEventListener("keydown", function (event) {
            if (event.key === "Enter") {
                转到();
            }
        });

        setTimeout(function () {
            // 获取用户之前输入的token
            用户输入 = localStorage.getItem("token");
            if (用户输入 == null) return 0;
            else{
                window.location.href = "../shenhe/"+用户输入;
            }
        }, 4  * 1000)
    </script>

                    """


@admin_page_bp.route('/admin~/<token>/main')
def admin(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin.html', token=token)


@admin_AutoTag_page_bp.route('/admin~/<token>/autotag')
def admin_AutoTag_page(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_autotag.html')


@admin_shenhe_page_bp.route('/admin~/<token>/shenhe')
def admin_shenhe_page(token):
    with open('shenhe_token', 'r') as f:
        文件_token = f.read().strip()
        if 文件_token != token and 调试模式() == False:
            return 错误页面()
    return render_template('admin_shenhe.html', 数据源=审核())


@admin_DeletePhoto_bp.route('/admin_thing~/shenhe/Delete/<ImgName>')
def 删除审核图片_(ImgName):
    return 删除审核图片(ImgName)


@admin_PassPhoto_bp.route('/admin_thing~/shenhe/Accept/<tag>/<ImgName>')
def 通过审核图片_(ImgName, tag):
    # 获取前端传过来的负载json
    print(tag)
    return 通过审核图片(ImgName, tag)


@admin_AutoTag_bp.route('/admin_thing~/shenhe/AutoTag/<ImgName>')
def 自动标签生成器(ImgName):
    图片名称 = os.path.join('img', '审核系统原始图片', ImgName)
    try:
        return 二次元图片标签自动生成([图片名称])
    except OSError as e:
        return {'error': True, 'message': f'指定文件不存在 - {e}', 'result': {}}
