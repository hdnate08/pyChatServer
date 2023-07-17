"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

import threading
import socket
import config  # Defaults module
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChatGUI import Ui_MainWindow
# from pyChatServer import PyChatServer  # server module


class pyChatBackend:
    def __init__(self):
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        # Default settings
        self.app.setStyle(config.DEFAULT_STYLE)
        self.ui.serverIP_lineEdit.setText(config.DEFAULT_IP)
        self.ui.port_lineEdit.setText(config.DEFAULT_PORT)

        # Connect button signals to their respective functions
        self.ui.establishServer_pushButton.clicked.connect(self.establish_server)
        self.ui.shutdownServer_pushButton.clicked.connect(self.shutdown_server)
        self.ui.clearLog_pushButton.clicked.connect(self.clear_log)

    def establish_server(self):
        self.append_to_Log("Server started")

    def shutdown_server(self):
        self.append_to_Log("Server stopped")

    def clear_log(self):
        self.ui.serverActivityLog_textEdit.clear()

    def append_to_Log(self, message):
        self.ui.serverActivityLog_textEdit.append(message)

    def run(self):
        self.window.show()  # Show the window
        self.app.exec_()  # Start the application event loop


if __name__ == '__main__':
    backend = pyChatBackend()
    backend.run()
