"""
Create by 2019/4/19 21:58
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 新建一个窗口
    w = QWidget()
    # 设置窗口的大小
    w.resize(400, 200)
    # 移动窗口的位置
    w.move(600, 300)
    # 设置窗口的标题
    w.setWindowTitle("我的PyQt")
    # 显示窗口
    w.show()
    # 维持进程
    sys.exit(app.exec_())
