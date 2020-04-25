from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *


class compile:
    def __init__(self):
        self.ui = QUiLoader().load("compile.ui")

        pass


app = QApplication([])
op = compile()
op.ui.show()
app.exec_()
