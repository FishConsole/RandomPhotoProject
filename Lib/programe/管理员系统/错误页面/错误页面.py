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
                window.location.href = "../"+用户输入+"/main";
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
