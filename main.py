from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("pyChat.ui", self)
        self.show()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
