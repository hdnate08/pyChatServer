"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChat import Ui_MainWindow
import config  # Defaults module


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
        self.ui.serverActivityLog_textEdit.insertPlainText('Establishing server...\n')

    def shutdown_server(self):
        self.ui.serverActivityLog_textEdit.insertPlainText('Shutting down server...\n')

    def clear_log(self):
        self.ui.serverActivityLog_textEdit.clear()

    def run(self):
        self.window.show()  # Show the window
        self.app.exec_()  # Start the application event loop


if __name__ == '__main__':
    backend = pyChatBackend()
    backend.run()
