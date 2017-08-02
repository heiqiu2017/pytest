#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
class Test_Sample:
    def test_login(self):
        allure.attach('描述', '这是一个注册登录的case')
        self.register()
        result = self.login('mio4kon')
        assert result
    @allure.step(title="登录账号:{1}")
    def login(self, account):
        return True
    @allure.step(title="注册")
    def register(self):
        pass
    def test_foo(self):
        f = open('./Image/1498470308.png', 'rb').read()
        # allure.attach('my attach', 'Hello, World')
        # 失败截图展示在报告中-思路
        assert 0,allure.attach('this is a img', f, allure.attach_type.PNG)
