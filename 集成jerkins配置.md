# Pytest+Allure+Jenkins配置
* 项目配置
    * 系统管理-管理插件 安装插件：Allure Jenkins Plugin
    * 系统管理-Global Tool Configuration 配置：Allure Commandline
        * 参考官方地址：https://docs.qameta.io/allure/latest/#_jenkins
    * Jenkins-新建项目：自由风格
    * 项目名称+描述
    * 配置GitHub project代码地址(测试／开发代码地址(例：https://github.com/linlin547/pytest_allure_test.git/))
    * 源码管理：Git
        * 代码仓库地址Repository URL：git地址
        * 代码仓库地址用户密码Credentials-add-Jenkins：只配置Usernma和Password即可
    * 构建Exceute shell-Command：
        * export PATH=$PATH:/usr/local/bin —pytest的系统运行目录
        * pytest -s -q —rerun 1 —alluredir report
    * 构建后操作
        * 增加构建后操作步骤 - Allure Report
        * path：report(因为测试项目生成报告为当前目录)
* 邮件配置
    * 配置(发送附件)邮件：
        * 系统管理-系统设置-Extended E-mail Notification
            * SMTP server：例 smtp.163.com
            * Default user E-mail suffix：例如 @163.com
            * 高级-Use SMTP Authentication - 输入发送邮件的邮箱和密码
            * Default Content Type: HTML(text/html)
            * Default Content(报告模版,使用以下html代码即可):
            <pre>
                 添加(邮件模版.txt)中的内容即可。
                 https://github.com/linlin547/pytest_allure_test/blob/master/邮件模版.txt
            </pre>
    * 配置系统邮件：
        * 系统管理-系统设置-邮件通知
            * SMTP服务器：例 smtp.163.com
            * 用户默认邮件后缀：例如 @163.com
            * 高级-使用SMTP认证
            * 输入发送邮箱和密码 -可以使用测试邮件验证
    * 配置系统用户：
        * 系统管理-系统设置-Jenkins Location
        * 系统管理员邮件地址：xx@163.com(发送邮件用户)
    * 项目中邮件配置：
        * 构建后操作-Editable Email Notification-Advanced Setting…
            * 只更改Triggers-高级-Recipient list:输入接收邮件列表；其他默认不变更