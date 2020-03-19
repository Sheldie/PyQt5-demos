# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox

from DialogDemo.Dialog import Ui_Dialog
from DialogDemo.MainWindow import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):  # 主窗口
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 绑定按钮事件
        self.PushButton.clicked.connect(self.changename)

    def changename(self):
        myDialog = MyDialog()
        myDialog.exec_()


# show():显示一个非模式对话框。控制权即刻返回给调用函数。弹出窗口是否为模式对话框，取决于modal属性的值。
# exec():显示一个模式对话框，并且锁住程序直到用户关闭该对话框为止。函数返回一个DialogCode结果。
# 调用show()的作用仅仅是将widget及其上的内容都显示出来，控制权即刻返回给调用函数。
# 而调用exec()后，调用线程将会被阻塞，锁住程序直到用户关闭该对话框，期间用户不可以切换同程序下的其它窗口直到Dialog关闭。

# 程序未处理完当前对话框时，将阻止和对话框的父窗口进行交互
# 在QtDesigner中勾选modal
class MyDialog(QDialog, Ui_Dialog):  # 对话框
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)
        # 绑定按钮事件
        self.OKButton.clicked.connect(self.confirmed)
        self.CancelButton.clicked.connect(self.cancel)

    def confirmed(self):
        name = self.lineEdit.text()
        name = name.lstrip().rstrip()  # 删除两端空格
        if name == "":  # 不允许为空
            QMessageBox.warning(self, "Error", "Name can not be empty")
        else:
            myWin.NameLabel.setText(name)
            self.close()

    def cancel(self):
        self.close()


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 适配高分辨率屏幕
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
