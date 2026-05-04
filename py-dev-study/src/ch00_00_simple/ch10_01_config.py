# 单例模式
class Config:
    def __init__(self):
        self.debug = True
        ｓelf.db_host = "localhost"
        self.db_port = 3306


config = Config()
