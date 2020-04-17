from PySide2.QtGui import QColor
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QListWidgetItem
import os


# import os.path
# todo 返回还没做
# todo 右键管理 新建文件夹，新建文件，双击打开和按钮打开
# todo 第一个是文件不会返回一级
def last_path(path):
    if path.endswith("/"):
        path = path[:-1]
    last_index = path.rfind("/")
    if "/" not in path:
        return -1
    return path[:last_index]


def size_format(size):
    if size < 1000:
        return '%i' % size + 'B'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size / 1000) + 'KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size / 1000000) + 'MB'
    elif 1000000000 <= size < 1000000000000:
        return '%.1f' % float(size / 1000000000) + 'GB'
    elif 1000000000000 <= size:
        return '%.1f' % float(size / 1000000000000) + 'TB'


def get_info(path):
    start0 = "<font color=\"#000000\">文件预览<br /></font >"
    temp = path[path.rfind("/") + 1:]
    file_name1 = "<b><font color=\"#000000\">文件名</font > </b>< >{}<br /></>".format(temp)
    file_size = size_format(os.path.getsize(path))
    file_size2 = "<b><font color=\"#000000\">文件大小</font > </b>< >{}<br /></>".format(file_size)
    return start0 + file_name1 + file_size2


class Fm_main:
    def __init__(self):
        self.ui = QUiLoader().load('fm_main.ui')
        self.path = "D:/a"
        self.root_path = self.path
        self.file1_path = self.path
        self.file2_path = ""
        self.file3_path = ""
        self.current_file = ""
        first_back = False
        # 初始化第一个
        str_list = os.listdir(self.path)
        self.ui.file1.addItems(str_list)
        # 初始化地址栏
        self.ui.the_path.setText(self.root_path + "/")
        self.ui.the_item.setText("路径")
        # 添加事件监听
        self.ui.file1.clicked.connect(self.file1_clicked)
        self.ui.file2.clicked.connect(self.file2_clicked)
        self.ui.file3.clicked.connect(self.file3_clicked)
        self.ui.tempt.clicked.connect(self.tempt_clicked)

    def file_inspect(self, file):
        self.ui.file_ins.setText("")
        # with open(file, "r", encoding="utf8") as fp:
        #     context = fp.readlines()
        self.ui.file_ins.setText(get_info(file))
        pass

    def file1_clicked(self):
        item = QListWidgetItem(self.ui.file1.currentItem()).text()
        if os.path.isfile(self.file1_path + "/" + item):
            self.ui.the_path.setText(self.file1_path + "/" + item)
            self.ui.the_item.setText("文件")
            self.file_inspect(self.file1_path + "/" + item)
            self.ui.file2.clear()
            self.ui.file3.clear()
            if self.file1_path != self.root_path:
                self.ui.file2.addItems(os.listdir(self.file2_path))
                self.ui.file2.setCurrentItem(self.ui.file1.currentItem())
                self.ui.file2.setCurrentRow(self.ui.file1.currentRow())
                self.ui.file1.clear()
                self.ui.file1.addItems(os.listdir(self.file1_path))
            return
        print(self.file1_path)
        print(self.root_path)
        self.ui.the_path.setText(self.file1_path + "/" + item + "/")
        self.ui.the_item.setText("路径")
        if self.file1_path == self.root_path:
            self.file2_path = self.file1_path + "/" + item
            self.ui.file2.clear()
            self.ui.file3.clear()
            self.ui.file2.addItems(os.listdir(self.file2_path))
        else:
            self.file2_path = self.file1_path
            self.file3_path = self.file1_path + "/" + item
            self.file1_path = last_path(self.file1_path)
            # file3
            self.ui.file3.clear()
            self.ui.file3.addItems(os.listdir(self.file3_path))
            self.ui.file3.setCurrentItem(self.ui.file2.currentItem())
            self.ui.file3.setCurrentRow(self.ui.file2.currentRow())
            # file2
            self.ui.file2.clear()
            self.ui.file2.addItems(os.listdir(self.file2_path))
            self.ui.file2.setCurrentItem(self.ui.file1.currentItem())
            self.ui.file2.setCurrentRow(self.ui.file1.currentRow())
            # file1
            self.ui.file1.clear()
            self.ui.file1.addItems(os.listdir(self.file1_path))
        pass

    def file2_clicked(self):
        item = QListWidgetItem(self.ui.file2.currentItem()).text()
        if os.path.isfile(self.file2_path + "/" + item):
            self.ui.the_path.setText(self.file2_path + "/" + item)
            self.ui.the_item.setText("文件")
            self.ui.file3.clear()
            self.file_inspect(self.file2_path + "/" + item)
            return
        self.ui.the_path.setText(self.file2_path + "/"+item+"/")
        self.ui.the_item.setText("路径")
        self.file3_path = self.file2_path + "/" + item
        self.ui.file3.clear()
        self.ui.file3.addItems(os.listdir(self.file3_path))
        pass

    def file3_clicked(self):
        item = QListWidgetItem(self.ui.file3.currentItem()).text()
        if os.path.isfile(self.file3_path + "/" + item):
            self.ui.the_path.setText(self.file3_path + "/" + item)
            self.ui.the_item.setText("文件")
            self.file_inspect(self.file3_path + "/" + item)
            return
        self.ui.the_path.setText(self.file3_path + "/" + item + "/")
        self.ui.the_item.setText("路径")
        self.file1_path = self.file2_path
        self.file2_path = self.file3_path
        self.file3_path = self.file3_path + "/" + item
        # 处理 file1
        self.ui.file1.clear()
        self.ui.file1.addItems(os.listdir(self.file1_path))
        self.ui.file1.setCurrentItem(self.ui.file2.currentItem())
        self.ui.file1.setCurrentRow(self.ui.file2.currentRow())
        # 处理 file2
        self.ui.file2.clear()
        self.ui.file2.addItems(os.listdir(self.file2_path))
        self.ui.file2.setCurrentItem(self.ui.file3.currentItem())
        self.ui.file2.setCurrentRow(self.ui.file3.currentRow())
        # 处理file3
        self.ui.file3.clear()
        self.ui.file3.addItems(os.listdir(self.file3_path))
        pass

    def tempt_clicked(self):
        self.ui.file_ins.setText("<B><font color=\"#000000\">红色字体\n</font > </B>")


app = QApplication(["D:/a/"])
op = Fm_main()
op.ui.show()
app.exec_()
