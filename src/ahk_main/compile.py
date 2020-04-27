from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *


class compile:
    def __init__(self, a):
        self.ui = QUiLoader().load("compile.ui")
        self.ui.a_choose.clicked.connect(self.a_choose_clicked)
        self.ui.b_choose.clicked.connect(self.b_choose_clicked)
        self.ui.c_choose.setEnabled(False)
        self.ui.c_line.setEnabled(False)
        self.ui.listView.setEnabled(False)
        self.ui.label_5.setEnabled(False)
        if a == "default":
            self.ui.a_line.setText("")
        else:
            self.ui.a_line.setText(a)
        pass

    def a_choose_clicked(self):
        openfile_name = QFileDialog.getOpenFileName(self.ui, '选择一个文件啵', '/', 'bs files(*.bs , *.txt)')[0]
        self.ui.a_line.setText(openfile_name)
        if openfile_name.endswith(".bs") or openfile_name.endswith(".ahk"):
            pass
        else:
            msgBox = QMessageBox()
            # todo 报错应该更详细一点，，，
            msgBox.setText("不支持该文件类型，请三思")
            msgBox.exec()
        pass

    def b_choose_clicked(self):
        openfile_name = QFileDialog.getSaveFileName(self.ui, '选择一个文件啵', '/', '可执行文件(*.exe)')[0]
        self.ui.b_line.setText(openfile_name)
        pass

    def c_choose_clicked(self):
        pass

    def start_clicked(self):
        # f = self.ui.a_line.text()
        # t = self.ui.b_line.text()
        # if f:
        #     if f.endswith(".ahk"):
        #         pass
        #     else:
        #
        pass

app = QApplication([])
op = compile("default")
op.ui.show()
app.exec_()
