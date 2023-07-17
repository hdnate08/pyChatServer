"""
pyChat server module
Nathan Harris
July 17, 2023
"""

class PyChatServer:
    def __init__(self, host, port, to_log):
        self.host = host
        self.port = port
        self.to_Log = to_log

    def start(self):
        self.to_Log('In PyChatServer start(), host:' + self.host + ' port:' + str(self.port))

    def stop(self):
        self.to_Log('In PyChatServer stop(), host:' + self.host + ' port:' + str(self.port))
