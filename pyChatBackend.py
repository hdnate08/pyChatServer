"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

import config  # Defaults module
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChatGUI import Ui_MainWindow
from pyChatServer import PyChatServer  # server module


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

        # Server instance
        self.server = None

    def establish_server(self):
        self.append_to_Log("Server starting...")
        if self.server is None:
            host = self.ui.serverIP_lineEdit.text()
            port = int(self.ui.port_lineEdit.text())
            self.server = PyChatServer(host, port, self.append_to_Log)
            self.server.start()

    def shutdown_server(self):
        self.append_to_Log("Server stopping...")
        if self.server is not None:
            self.server.stop()
            self.server = None

    def clear_log(self):
        self.ui.serverActivityLog_textEdit.clear()

    def append_to_Log(self, message):
        self.ui.serverActivityLog_textEdit.append(message)

    def run(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    backend = pyChatBackend()
    backend.run()
