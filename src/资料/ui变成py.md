再pyside2的uic中，会自动生成代码，然后，对代码做如下修改
就可以相当于导入ui文件的样子
1，对ui文件进行继承，并且如下方式调用父类方法
class Ui_Form(QMainWindow):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

2，向正常程序一样进行实例化
class out:
    def __init__(self):

        self.ui = Ui_Form()
        # self.ui下就会有控件的名字
        pass

app = QApplication([])
op = out()
op.ui.show()
app.exec_()

就酱


