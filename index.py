# -*- coding: utf-8 -*-
from multiprocessing import Process

from 后端.后端执行与回调部.执行部门.运维相关.路径控制 import 路径控制
from 后端.后端执行与回调部.执行部门.运维相关.调试模式.调试模式 import 调试模式_GUI启动
from 后端.后端启动器.后端启动器 import 后端启动器

if __name__ == '__main__':

    import toga
    from toga.style.pack import COLUMN, Pack


    class Graze(toga.App):
        def startup(self):
            self.main_window = toga.MainWindow(title='')
            self.webview = toga.WebView(
                on_webview_load=self.on_webview_loaded, style=Pack(flex=1)
            )
            self.url_input = toga.TextInput(
                value=f'https://{路径控制.启动位置.启动位置()}', style=Pack(flex=1)
            )
            box = toga.Box(
                children=[
                    self.webview,
                ],
                style=Pack(direction=COLUMN),
            )
            self.main_window.content = box
            self.webview.url = self.url_input.value
            # Show the main window
            self.main_window.show()

        def load_page(self, widget):
            self.webview.url = self.url_input.value

        def on_webview_loaded(self, widget):
            self.url_input.value = self.webview.url


    def main():
        return Graze("RandomPhoto", "org.beeware.graze")


    后端 = Process(target=后端启动器)
    后端.start()
    if 调试模式_GUI启动():
        main().main_loop()
