from PySide2.QtWidgets import QApplication, QMessageBox, QTreeWidget, QTreeWidgetItem, QFileDialog
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
# todo 编译的时候记得把那个按键改成循环的形式
# 下面是一些静态方法，以后可以独立用一个文件，更加整洁一点
def isVar(str):
    # todo 用于判定，当前的字符串,是否符合变量命名规范
    if "-" in str:
        return False
    if str[0].isdigit():
        return False
    if str:
        return True
    else:
        return False

def bs_Magic(str):
    # todo 还没做
    # str = str.
    assert str.strip().startswith("bs$")


class out_put:
    def __init__(self):
        self.ui = QUiLoader().load('ahk_main.ui')
        # self.ui.insert_btn.clicked.connect(self.insert)
        # self.ui.Form.funs.hot_key.hot_key_ok.connect(self.hot_key_pressed())
        print(self.ui.whatsThis())
        self.ui.hotkey_ok.clicked.connect(self.hot_key_pressed)
        self.ui.Msg_ok.clicked.connect(self.Msg_ok_pressed)
        self.ui.open_btn.clicked.connect(self.open_btn_clicked)
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
        self.ui.save_btn.clicked.connect(self.save_btn_clicked)
        # 以下是鼠标键盘系列
        self.ui.a_ok.clicked.connect(self.a_ok_clicked)
        self.ui.b_ok.clicked.connect(self.b_ok_clicked)
        self.ui.c_ok.clicked.connect(self.c_ok_clicked)
        self.ui.c_com.currentIndexChanged.connect(self.c_com_changed)
        self.ui.d_ok.clicked.connect(self.d_ok_clicked)
        self.ui.e_ok.clicked.connect(self.e_ok_clicked)
        # 延时
        self.ui.g_ok.clicked.connect(self.g_ok_clicked)

    def many_inits(self):
        self.ui.key_mode.addItems(['完整按键', '按下', '抬起'])  # 注意，有一次引用，修改需一起
        self.ui.time_show.setSuffix("次")
        self.ui.time_show.setValue(1)
        self.ui.keymap.addItems(["热键们", "Ctrl", "Alt", "q", "w", "e"])  # todo a lot of key to add
        # 上一句热键们有一处引用
        # self.ui.c_com.addItems(["选择方式"]) # 一次引用
        self.ui.c_com.addItems(['完整按键', '按下', '抬起'])  # 一次引用
        self.ui.c_key.addItems(["左键", "右键", "滚轮/中键"])
        self.ui.d_mode.addItems(["向上", "向下"])
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

    def open_btn_clicked(self):
        openfile_name = QFileDialog.getOpenFileName(self.ui, '选择一个文件啵', '/', 'bs files(*.bs , *.txt)')
        f = open(openfile_name[0], mode="r", encoding="utf8")
        lines = f.readlines()
        for a_line in lines:
            self.ui.code_text.insertPlainText(a_line)
        f.close()
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
        if self.ui.key_mode.currentText() == "按下" or self.ui.key_mode.currentText() == "抬起":
            self.ui.time_show.value = 1
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
        openfile_name = QFileDialog.getOpenFileName(self.ui, '选择文件', '/', 'bs files(*.xlsx , *.xls)')
        # bs files(*.xlsx , *.xls)' 多个文件格式就这么整
        # self.ui.code_text.append("<font color=\"#FF0000\">红色字体\n</font> ")
        print(openfile_name)
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
            self.ui.c_t.value = 1
            self.ui.c_t.setEnabled(False)
        else:
            self.ui.c_t.setEnabled(True)

    def c_ok_clicked(self):
        mode = self.ui.c_com.currentText()
        key = self.ui.c_key.currentText()
        try:
            time = self.ui.c_t.value()
        except:
            time = 1
        if mode == "完整按键":
            if key == "左键":
                code = f"Click, left, {time}  ;左键点击{time}次\n"
            elif key == "右键":
                code = f"Click, right, {time}  ;右键单击{time}次\n"
            elif key == "滚轮/中键":
                code = f"Click, middle, {time}  ;右键单击{time}次\n"
        elif mode == "按下":
            if key == "左键":
                code = f"Click, left, down  ;按下左键\n"
            elif key == "右键":
                code = f"Click, right, down  ;按下右键n"
            elif key == "滚轮/中键":
                code = f"Click, middle, down  ;按下中间（就是滚轮键）\n"
        elif mode == "抬起":
            if key == "左键":
                code = f"Click, left, up  ;抬起左键\n"
            elif key == "右键":
                code = f"Click, right, up  ;抬起右键\n"
            elif key == "滚轮/中键":
                code = f"Click, middle, up  ;抬起中键\n"
        self.ui.code_text.insertPlainText(code)
        pass

    def f_ok_clicked(self):
        if isVar(self.ui.f_var.text()) and self.ui.f_thing.text():
            send_code = "{} := {}\n".format(self.ui.f_var.text(), self.ui.f_thing.text())
            self.ui.code_text.insertPlainText(send_code)
        pass

    def d_ok_clicked(self):
        time = self.ui.d_time.value()
        mode = self.ui.d_mode.currentText()
        if mode == "向上":
            code = f"bs$ Click, WheelUp,{time}  \n;滚轮向上滚动{time}次"
        else:
            code = f"bs$ Click, WheelDown,{time}  \n;滚轮向下滚动{time}次"
        self.ui.code_text.insertPlainText(code)
        pass

    def e_ok_clicked(self):
        x = self.ui.e_x.text()
        y = self.ui.e_y.text()
        print(x)
        print(y)
        if isVar(x) and isVar(y):
            code = f"MouseGetPos {x}, {y}  ;当前鼠标的位置坐标将会被保存到{x}和{y}中\n"
        else:
            msgBox = QMessageBox()
            msgBox.setText("x和y填的应该是要保存到的变量名\n检查一下？")
            msgBox.exec()
            return
        self.ui.code_text.insertPlainText(code)

    def g_ok_clicked(self):
        code = f"Sleep,{self.ui.g_time.value()}\n"
        self.ui.code_text.insertPlainText(code)

    def save_btn_clicked(self):
        code = self.ui.code_text.toPlainText
        with open("D:/a/app.txt",mode="w",encoding="utf8") as fp:
            fp.write()

app = QApplication([])
op = out_put()
op.ui.show()
app.exec_()
