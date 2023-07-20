"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChatServerGUI import Ui_MainWindow
from pyChatServer import PyChatServer
import config
import threading


class pyChatServerBackend:
    def __init__(self):
        # Window setup
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        # Default settings
        self.window.closeEvent = self.close_event
        self.app.setStyle(config.DEFAULT_STYLE)
        self.ui.serverIP_lineEdit.setText(config.DEFAULT_IP)
        self.ui.port_lineEdit.setText(str(config.DEFAULT_PORT))

        # Connect button signals to their respective functions
        self.ui.establishServer_pushButton.clicked.connect(self.establish_server)
        self.ui.shutdownServer_pushButton.clicked.connect(self.shutdown_server)
        self.ui.clearLog_pushButton.clicked.connect(self.clear_log)

        # Server instance
        self.server = None

    def establish_server(self):
        if self.server is None:
            host = self.ui.serverIP_lineEdit.text()
            port = int(self.ui.port_lineEdit.text())
            self.server = PyChatServer(host, port, self.append_to_Log)

            listener_thread = threading.Thread(target=self.server.start)
            listener_thread.start()

    def shutdown_server(self):
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

    def close_event(self, event):
        self.shutdown_server()
        event.accept()


if __name__ == '__main__':
    backend = pyChatServerBackend()
    backend.run()
