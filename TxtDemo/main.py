# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import sys

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from TxtDemo.MainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 绑定按钮事件
        self.OpenButton.clicked.connect(self.openfile)
        self.ResetButton.clicked.connect(self.reset)

    def openfile(self):
        filename = QFileDialog.getOpenFileName(self, '选择文件', '', 'txt files(*.txt)')    # 打开文件
        fo = open(filename[0], "r", encoding="utf-8")
        self.lineEdit.setText(filename[0])
        for line in fo.readlines():
            line = line.strip()
            self.textBrowser.append(line)
        self.textBrowser.moveCursor(QTextCursor.Start)  # 光标设置到开头

    def reset(self):
        self.lineEdit.clear()
        self.textBrowser.clear()


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 适配高分辨率屏幕
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

