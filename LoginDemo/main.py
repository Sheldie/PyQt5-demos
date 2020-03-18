# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import sys
from LoginDemo.MainWindow import Ui_Login
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 绑定按钮事件
        self.LoginButton.clicked.connect(self.login)
        self.ResetButton.clicked.connect(self.reset)

    def login(self):
        if self.UsernameEdit.text() != 'test' and self.PasswordEdit.text() != 'test':
            self.TipLabel.setText("Incorrect username or password.")
            self.reset()
        else:
            self.TipLabel.setText("Successful login.")

    def reset(self):
        self.UsernameEdit.clear()
        self.PasswordEdit.clear()


if __name__ == '__main__':  # 测试账号密码: test / test
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 适配高分辨率屏幕
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
