from PySide2.QtWidgets import QApplication, QMessageBox, QTreeWidget, QTreeWidgetItem
from PySide2.QtUiTools import QUiLoader
import setting_pyfile
import os


# import t_btn1
# 等号赋值我没做，因为我暂时并不打算推荐用户使用等号赋值的操作
# todo code 竖项自动移动
# todo 语法检查
# todo 自动标点成对的引号括号百分号 ctrlxd行操作
# todo 回车键直接输入啊
# todo 设置菜单
# todo run 好像得多线程
# todo 滚动条美观优化
# todo 编译
# todo 延时工具
# todo 添加每一个语句的时候自然在后面加上注释

# 下面是一些静态方法，以后可以独立用一个文件，更加整洁一点
def isVar(str):
    # todo 用于判定，当前的字符串,是否符合变量命名规范
    if str:
        return True
    else:
        return False


class out_put:
    def __init__(self):
        self.ui = QUiLoader().load('ahk_main.ui')
        # self.ui.insert_btn.clicked.connect(self.insert)
        # self.ui.Form.funs.hot_key.hot_key_ok.connect(self.hot_key_pressed())
        print(self.ui.whatsThis())
        self.ui.hotkey_ok.clicked.connect(self.hot_key_pressed)
        self.ui.Msg_ok.clicked.connect(self.Msg_ok_pressed)
        self.ui.run_prog_ok.clicked.connect(self.Run_Prog_clicked)
        self.ui.about_btn.clicked.connect(self.about_btn_clicked)
        self.ui.t_btn.clicked.connect(self.t_btn_clicked)
        self.ui.color_it.clicked.connect(self.color_it_clicked)
        # self.ui.code_text.setTabStopWidth(32)  # 4空格tab
        self.many_inits()
        self.ui.key_mode.currentIndexChanged.connect(self.key_mode_valChange)
        self.ui.keymap.currentIndexChanged.connect(self.keymap_valChange)
        self.ui.sendkeyok.clicked.connect(self.sendkeyok_clicked)
        self.ui.setting.clicked.connect(self.setting_connected)
        self.ui.run_btn.clicked.connect(self.run_btn_clicked)
        self.ui.f_ok.clicked.connect(self.f_ok_clicked)
        # 以下是鼠标键盘系列
        self.ui.a_ok.clicked.connect(self.a_ok_clicked)
        self.ui.b_ok.clicked.connect(self.b_ok_clicked)
        self.ui.c_ok.clicked.connect(self.c_ok_clicked)
        self.ui.c_com.currentIndexChanged.connect(self.c_com_changed)

        # 用于计数的变量
        self.c_is_first = 0

    def many_inits(self):
        self.ui.key_mode.addItems([ '完整按键', '按下', '抬起'])  # 注意，有一次引用，修改需一起
        self.ui.time_show.setSuffix("次")
        self.ui.time_show.setValue(1)
        self.ui.keymap.addItems(["热键们", "Ctrl", "Alt", "q", "w", "e"])  # todo a lot of key to add
        # 上一句热键们有一处引用
        # self.ui.c_com.addItems(["选择方式"]) # 一次引用
        self.ui.c_com.addItems(['完整按键', '按下', '抬起']) # 一次引用
        pass

    def cnsp_2_ensp(self, str1):
        str2 = str1.replace(" ", " ")
        return str2

    def space_2_bsp(self, str1):
        # str2 = str1.replace(" ", "&nbsp;")
        str2 = str1.replace(" ", "&nbsp;")
        return str2
        pass

    def tab_2_4space(self, str1):
        str2 = str1.replace("\t", "&nbsp;&nbsp;")
        return str2
        pass

    def pySymbol_2_htmlSymbol(self, line):
        print(line)
        line = self.cnsp_2_ensp(line)
        print(line)
        line = self.tab_2_4space(line)
        print(line)
        line = self.space_2_bsp(line)
        return line
        pass

    def insert(self):
        info1 = self.ui.lineEdit.text()
        self.ui.Form.textEdit.insertPlainText(info1)

    def hot_key_pressed(self):
        hot_key_is_str = self.ui.hot_key_is.text()
        while hot_key_is_str.endswith(" "):
            hot_key_is_str = hot_key_is_str[:-1]
        if self.ui.over_it.checkState():
            info = "bs$ ~" + self.ui.hot_key_is.text() + "::\n\t;在此填入按下热键后执行的命令\n\nReturn\n\n"
        else:
            info = "bs$ " + self.ui.hot_key_is.text() + "::\n;在此填入按下热键后执行的命令\n\nReturn\n\n"
        self.ui.code_text.insertPlainText(info)

    def Msg_ok_pressed(self):
        info = "MsgBox, " + self.ui.Msg_info.text() + "\n"
        self.ui.code_text.insertPlainText(info)

    def Run_Prog_clicked(self):
        info = "Run " + self.ui.run_prog_is.text() + "\n"
        self.ui.code_text.insertPlainText(info)

    def about_btn_clicked(self):
        msgBox = QMessageBox()
        msgBox.setText("ahk的编辑器\n作者邮箱zephms@163.com\n")
        msgBox.exec()
        pass

    def color_it_clicked(self):
        # todo 有bug不好用
        info = self.ui.code_text.toPlainText()
        codes = info.split("\n")
        print(codes)
        self.ui.code_text.setText("")
        for line in codes:
            print(line)
            line = self.pySymbol_2_htmlSymbol(line)
            # todo 注意这个append是新增一行然后写入的意思，当时可能错在这里了
            self.ui.code_text.append("<font color=\"#FF0000\">" + line + "\n</font> ")
        print("=======")
        pass

    def key_mode_valChange(self):
        # todo 反了，只有完整按键才有次数
        if self.ui.key_mode.currentText() == "按下" or self.ui.key_mode.currentText() == "抬起":
            self.ui.time_show.setEnabled(False)
        else:
            self.ui.time_show.setEnabled(True)

    def sendkeyok_clicked(self):
        # todo 还没对文本框进行处理
        keyText = (self.ui.key2send.text()).upper
        keysList = keyText.split()
        # for i in
        pass

    def keymap_valChange(self):
        this_key = self.ui.keymap.currentText()
        if this_key == "热键们":
            return
        temp = self.ui.hot_key_is.text()
        if temp == "":
            self.ui.hot_key_is.setText(this_key)
        else:
            self.ui.hot_key_is.setText(temp + " " + this_key)
        pass

    def t_btn_clicked(self):
        send_code = "MouseMove,{},{}"
        self.ui.code_text.append(send_code)
        # self.ui = QUiLoader().load('ahk_flat.ui')
        # self.ui.code_text.append("<font color=\"#FF0000\">红色字体\n</font> ")
        # self.ui.code_text.append("<font color=\"#FF0000\">&nbsp;haha\n</font> ")
        pass

    def setting_connected(self):
        setting_show1 = setting_pyfile.setting_show()
        setting_show1.ui.show()
        setting_show1.ui.exec()

    def run_btn_clicked(self):
        with open("temp.ahk", "w", encoding="gbk") as fp:
            context = self.ui.code_text.toPlainText()
            fp.write(context)
        run_file = "temp.ahk"
        my_command = "AutoHotkeyU64.exe" + " " + run_file
        os.system(my_command)

    def a_ok_clicked(self):
        getX = self.ui.a_x.text()
        getY = self.ui.a_y.text()
        if getX.isdigit() and getY.isdigit():
            # todo 这样判定，如果getx个gety是小数，就会被判为否定
            send_code = "MouseMove,{},{}\n".format(getX, getY)
        elif getX.isdigit() and isVar(getY):
            print("adfasfd")
            send_code = "MouseMove,{},%{}%\n".format(getX, getY)
        elif isVar(getX) and getY.isdigit():
            send_code = "MouseMove,%{}%,{}\n".format(getX, getY)
        elif isVar(getX) and isVar(getY):
            send_code = "MouseMove,%{}%,%{}%\n".format(getX, getY)
        else:
            msgBox = QMessageBox()
            # todo 报错应该更详细一点，，，
            msgBox.setText("里面应该放整数或者变量")
            msgBox.exec()
            return
        self.ui.code_text.insertPlainText(send_code)

    def b_ok_clicked(self):
        getX = self.ui.b_x.text()
        getY = self.ui.b_y.text()
        if getX.isdigit() and getY.isdigit():
            # todo 这样判定，如果getx个gety是小数，就会被判为否定
            send_code = "Relative,{},{}\n".format(getX, getY)
        elif getX.isdigit() and isVar(getY):
            print("adfasfd")
            send_code = "Relative,{},%{}%\n".format(getX, getY)
        elif isVar(getX) and getY.isdigit():
            send_code = "Relative,%{}%,{}\n".format(getX, getY)
        elif isVar(getX) and isVar(getY):
            send_code = "Relative,%{}%,%{}%\n".format(getX, getY)
        else:
            msgBox = QMessageBox()
            # todo 报错应该更详细一点，，，
            msgBox.setText("里面应该放整数或者变量")
            msgBox.exec()
            return
        self.ui.code_text.insertPlainText(send_code)

    def c_com_changed(self):
        if self.ui.c_com.currentText() == "按下" or self.ui.c_com.currentText() == "抬起":
            self.ui.c_t.setEnabled(False)
        else:
            self.ui.c_t.setEnabled(True)

    def c_ok_clicked(self):

        pass

    def f_ok_clicked(self):
        if isVar(self.ui.f_var.text()) and self.ui.f_thing.text():
            send_code = "{} := {}\n".format(self.ui.f_var.text(), self.ui.f_thing.text())
            self.ui.code_text.insertPlainText(send_code)
        pass


app = QApplication([])
op = out_put()
op.ui.show()
app.exec_()
