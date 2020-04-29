from PySide2.QtCore import (QCoreApplication, QRect, Qt, QMetaObject)
from PySide2.QtGui import QFont
from PySide2.QtWidgets import *


class MainWindowUI(object):
    def __init__(self):
        super(MainWindowUI, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1066, 619)
        self.verticalLayout_11 = QVBoxLayout(Form)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_10.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.open_btn = QPushButton(Form)
        self.open_btn.setObjectName(u"open_btn")

        self.horizontalLayout.addWidget(self.open_btn)

        self.save_btn = QPushButton(Form)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)

        self.about_btn = QPushButton(Form)
        self.about_btn.setObjectName(u"about_btn")

        self.horizontalLayout.addWidget(self.about_btn)

        self.run_btn = QPushButton(Form)
        self.run_btn.setObjectName(u"run_btn")

        self.horizontalLayout.addWidget(self.run_btn)

        self.cp_btn = QPushButton(Form)
        self.cp_btn.setObjectName(u"cp_btn")

        self.horizontalLayout.addWidget(self.cp_btn)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.tabWidget_2 = QTabWidget(Form)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setDocumentMode(True)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 20, 491, 261))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.over_it = QCheckBox(self.layoutWidget)
        self.over_it.setObjectName(u"over_it")

        self.horizontalLayout_3.addWidget(self.over_it)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_3.addWidget(self.checkBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.keymap = QComboBox(self.layoutWidget)
        self.keymap.setObjectName(u"keymap")

        self.horizontalLayout_4.addWidget(self.keymap)

        self.hot_key_is = QLineEdit(self.layoutWidget)
        self.hot_key_is.setObjectName(u"hot_key_is")
        self.hot_key_is.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.hot_key_is)

        self.hotkey_ok = QPushButton(self.layoutWidget)
        self.hotkey_ok.setObjectName(u"hotkey_ok")

        self.horizontalLayout_4.addWidget(self.hotkey_ok)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.run = QHBoxLayout()
        self.run.setObjectName(u"run")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.run.addWidget(self.label_4)

        self.run_prog_is = QLineEdit(self.layoutWidget)
        self.run_prog_is.setObjectName(u"run_prog_is")
        self.run_prog_is.setClearButtonEnabled(False)

        self.run.addWidget(self.run_prog_is)

        self.run_prog_ok = QPushButton(self.layoutWidget)
        self.run_prog_ok.setObjectName(u"run_prog_ok")

        self.run.addWidget(self.run_prog_ok)


        self.verticalLayout_2.addLayout(self.run)

        self.Msg = QHBoxLayout()
        self.Msg.setObjectName(u"Msg")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.Msg.addWidget(self.label_6)

        self.Msg_info = QLineEdit(self.layoutWidget)
        self.Msg_info.setObjectName(u"Msg_info")
        self.Msg_info.setClearButtonEnabled(False)

        self.Msg.addWidget(self.Msg_info)

        self.Msg_ok = QPushButton(self.layoutWidget)
        self.Msg_ok.setObjectName(u"Msg_ok")

        self.Msg.addWidget(self.Msg_ok)


        self.verticalLayout_2.addLayout(self.Msg)

        self.Msg_2 = QHBoxLayout()
        self.Msg_2.setObjectName(u"Msg_2")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.Msg_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.Msg_2.addWidget(self.label_9)

        self.f_var = QLineEdit(self.layoutWidget)
        self.f_var.setObjectName(u"f_var")
        self.f_var.setClearButtonEnabled(False)

        self.Msg_2.addWidget(self.f_var)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.Msg_2.addWidget(self.label_10)

        self.f_thing = QLineEdit(self.layoutWidget)
        self.f_thing.setObjectName(u"f_thing")
        self.f_thing.setClearButtonEnabled(False)

        self.Msg_2.addWidget(self.f_thing)

        self.f_ok = QPushButton(self.layoutWidget)
        self.f_ok.setObjectName(u"f_ok")

        self.Msg_2.addWidget(self.f_ok)


        self.verticalLayout_2.addLayout(self.Msg_2)

        self.tabWidget_2.addTab(self.widget, "")
        self.tabWidget_2Page1 = QWidget()
        self.tabWidget_2Page1.setObjectName(u"tabWidget_2Page1")
        self.layoutWidget1 = QWidget(self.tabWidget_2Page1)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 501, 291))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_13)

        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)


        self.horizontalLayout_10.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.a_x = QLineEdit(self.layoutWidget1)
        self.a_x.setObjectName(u"a_x")
        self.a_x.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.a_x)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_16)

        self.a_y = QLineEdit(self.layoutWidget1)
        self.a_y.setObjectName(u"a_y")
        self.a_y.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.a_y)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_17)

        self.b_x = QLineEdit(self.layoutWidget1)
        self.b_x.setObjectName(u"b_x")
        self.b_x.setClearButtonEnabled(False)

        self.horizontalLayout_6.addWidget(self.b_x)

        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_20)

        self.b_y = QLineEdit(self.layoutWidget1)
        self.b_y.setObjectName(u"b_y")
        self.b_y.setClearButtonEnabled(False)

        self.horizontalLayout_6.addWidget(self.b_y)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.c_com = QComboBox(self.layoutWidget1)
        self.c_com.setObjectName(u"c_com")
        self.c_com.setDuplicatesEnabled(False)

        self.horizontalLayout_7.addWidget(self.c_com)

        self.c_key = QComboBox(self.layoutWidget1)
        self.c_key.setObjectName(u"c_key")

        self.horizontalLayout_7.addWidget(self.c_key)

        self.c_t = QSpinBox(self.layoutWidget1)
        self.c_t.setObjectName(u"c_t")
        self.c_t.setMinimum(1)
        self.c_t.setMaximum(999)
        self.c_t.setValue(1)

        self.horizontalLayout_7.addWidget(self.c_t)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.d_mode = QComboBox(self.layoutWidget1)
        self.d_mode.setObjectName(u"d_mode")

        self.horizontalLayout_8.addWidget(self.d_mode)

        self.d_time = QSpinBox(self.layoutWidget1)
        self.d_time.setObjectName(u"d_time")
        self.d_time.setValue(1)

        self.horizontalLayout_8.addWidget(self.d_time)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_19)

        self.e_x = QLineEdit(self.layoutWidget1)
        self.e_x.setObjectName(u"e_x")
        self.e_x.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.e_x)

        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_22)

        self.e_y = QLineEdit(self.layoutWidget1)
        self.e_y.setObjectName(u"e_y")
        self.e_y.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.e_y)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.key2send = QLineEdit(self.layoutWidget1)
        self.key2send.setObjectName(u"key2send")
        self.key2send.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.key2send)

        self.key_mode = QComboBox(self.layoutWidget1)
        self.key_mode.setObjectName(u"key_mode")

        self.horizontalLayout_2.addWidget(self.key_mode)

        self.time_show = QSpinBox(self.layoutWidget1)
        self.time_show.setObjectName(u"time_show")
        self.time_show.setMinimum(1)
        self.time_show.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.time_show)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.a_ok = QPushButton(self.layoutWidget1)
        self.a_ok.setObjectName(u"a_ok")

        self.verticalLayout_3.addWidget(self.a_ok)

        self.b_ok = QPushButton(self.layoutWidget1)
        self.b_ok.setObjectName(u"b_ok")

        self.verticalLayout_3.addWidget(self.b_ok)

        self.c_ok = QPushButton(self.layoutWidget1)
        self.c_ok.setObjectName(u"c_ok")

        self.verticalLayout_3.addWidget(self.c_ok)

        self.d_ok = QPushButton(self.layoutWidget1)
        self.d_ok.setObjectName(u"d_ok")

        self.verticalLayout_3.addWidget(self.d_ok)

        self.e_ok = QPushButton(self.layoutWidget1)
        self.e_ok.setObjectName(u"e_ok")

        self.verticalLayout_3.addWidget(self.e_ok)

        self.sendkeyok = QPushButton(self.layoutWidget1)
        self.sendkeyok.setObjectName(u"sendkeyok")

        self.verticalLayout_3.addWidget(self.sendkeyok)


        self.horizontalLayout_10.addLayout(self.verticalLayout_3)

        self.tabWidget_2.addTab(self.tabWidget_2Page1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget2 = QWidget(self.tab)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 491, 111))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_14.addWidget(self.label_21)

        self.line_3 = QFrame(self.layoutWidget2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.h_t = QLineEdit(self.layoutWidget2)
        self.h_t.setObjectName(u"h_t")

        self.horizontalLayout_12.addWidget(self.h_t)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.h_ok1 = QPushButton(self.layoutWidget2)
        self.h_ok1.setObjectName(u"h_ok1")

        self.verticalLayout_6.addWidget(self.h_ok1)

        self.h_ok2 = QPushButton(self.layoutWidget2)
        self.h_ok2.setObjectName(u"h_ok2")

        self.verticalLayout_6.addWidget(self.h_ok2)


        self.horizontalLayout_12.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.h_c = QPushButton(self.layoutWidget2)
        self.h_c.setObjectName(u"h_c")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.h_c.sizePolicy().hasHeightForWidth())
        self.h_c.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.h_c)

        self.h_b = QPushButton(self.layoutWidget2)
        self.h_b.setObjectName(u"h_b")
        sizePolicy1.setHeightForWidth(self.h_b.sizePolicy().hasHeightForWidth())
        self.h_b.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.h_b)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_14.addLayout(self.verticalLayout_7)

        self.layoutWidget3 = QWidget(self.tab)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 130, 491, 30))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget3)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_18)

        self.g_time = QSpinBox(self.layoutWidget3)
        self.g_time.setObjectName(u"g_time")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.g_time.sizePolicy().hasHeightForWidth())
        self.g_time.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.g_time)

        self.g_ok = QPushButton(self.layoutWidget3)
        self.g_ok.setObjectName(u"g_ok")
        sizePolicy1.setHeightForWidth(self.g_ok.sizePolicy().hasHeightForWidth())
        self.g_ok.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.g_ok)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget4 = QWidget(self.tab_2)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(60, 80, 171, 157))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.color_it = QPushButton(self.layoutWidget4)
        self.color_it.setObjectName(u"color_it")

        self.verticalLayout_8.addWidget(self.color_it)

        self.t_btn = QPushButton(self.layoutWidget4)
        self.t_btn.setObjectName(u"t_btn")

        self.verticalLayout_8.addWidget(self.t_btn)

        self.pushButton_3 = QPushButton(self.layoutWidget4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_8.addWidget(self.pushButton_3)

        self.label_14 = QLabel(self.layoutWidget4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_14)

        self.tabWidget_2.addTab(self.tab_2, "")

        self.verticalLayout_10.addWidget(self.tabWidget_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_9.addWidget(self.label)

        self.code_text = QTextEdit(Form)
        self.code_text.setObjectName(u"code_text")
        self.code_text.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_9.addWidget(self.code_text)


        self.horizontalLayout_15.addLayout(self.verticalLayout_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line)


        self.retranslateUi(Form)

        self.tabWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AutoHotkey Simple IDE", None))
        self.open_btn.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.about_btn.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.run_btn.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c", None))
        self.cp_btn.setText(QCoreApplication.translate("Form", u"\u7f16\u8bd1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u589e\u52a0\u4e00\u7ec4\u70ed\u952e", None))
        self.over_it.setText(QCoreApplication.translate("Form", u"\u8986\u76d6\u539f\u6709\u529f\u80fd", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"$\u6a21\u5f0f(\u5b9e\u73b0\u4e2d)", None))
        self.hot_key_is.setPlaceholderText(QCoreApplication.translate("Form", u"\u70ed\u952e\u540d", None))
        self.hotkey_ok.setText(QCoreApplication.translate("Form", u"ok", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u7a0b\u5e8f    ", None))
        self.run_prog_is.setPlaceholderText(QCoreApplication.translate("Form", u"\u7a0b\u5e8f\u540d", None))
        self.run_prog_ok.setText(QCoreApplication.translate("Form", u"ok", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5f39\u51fa\u6d88\u606f\u6846", None))
        self.Msg_info.setPlaceholderText(QCoreApplication.translate("Form", u"\u5185\u5bb9", None))
        self.Msg_ok.setText(QCoreApplication.translate("Form", u"ok", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u4f20\u503c", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u5185\u5bb9  \uff1a", None))
        self.f_var.setPlaceholderText(QCoreApplication.translate("Form", u"\u88ab\u4f20\u503c\u7684\u53d8\u91cf", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<==", None))
        self.f_thing.setPlaceholderText(QCoreApplication.translate("Form", u"\u503c", None))
        self.f_ok.setText(QCoreApplication.translate("Form", u"ok", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.widget), QCoreApplication.translate("Form", u"\u7cfb\u7edf", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u79fb\u52a8\u5230", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u76f8\u5bf9\u79fb\u52a8", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u6309\u952e", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6eda\u8f6e\u4e0a\u4e0b", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5c06\u5f53\u524d\u9f20\u6807\u4f4d\u7f6e\u4fdd\u5b58\u5230\u53d8\u91cf\u4e2d", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u53d1\u9001\u6309\u952e", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Y", None))
        self.c_com.setCurrentText("")
        self.c_t.setSuffix(QCoreApplication.translate("Form", u"\u6b21", None))
        self.d_time.setSuffix(QCoreApplication.translate("Form", u"\u6b21", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Y", None))
        self.key2send.setPlaceholderText(QCoreApplication.translate("Form", u"\u8981\u53d1\u9001\u7684\u6309\u952e", None))
        self.a_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.b_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.c_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.d_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.e_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.sendkeyok.setText(QCoreApplication.translate("Form", u"ok[\u5f00\u53d1\u4e2d]", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabWidget_2Page1), QCoreApplication.translate("Form", u"\u952e\u76d8\u9f20\u6807", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u5faa\u73af", None))
        self.h_t.setInputMask("")
        self.h_t.setPlaceholderText(QCoreApplication.translate("Form", u"\u6b21\u6570(\u7a7a\u8868\u793a\u65e0\u9650)", None))
        self.h_ok1.setText(QCoreApplication.translate("Form", u"OK for \u666e\u901a\u5faa\u73af", None))
        self.h_ok2.setText(QCoreApplication.translate("Form", u"OK for \u6761\u4ef6\u5faa\u73af", None))
        self.h_c.setText(QCoreApplication.translate("Form", u"continue\u8bed\u53e5", None))
        self.h_b.setText(QCoreApplication.translate("Form", u"break\u8bed\u53e5", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u5ef6\u65f6", None))
        self.g_time.setSuffix(QCoreApplication.translate("Form", u"\u6beb\u79d2", None))
        self.g_ok.setText(QCoreApplication.translate("Form", u"OK", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("Form", u"\u7a0b\u5e8f\u6d41\u8f6c", None))
        self.color_it.setText(QCoreApplication.translate("Form", u"\u4e0a\u8272", None))
        self.t_btn.setText(QCoreApplication.translate("Form", u"t", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4ece\u5c0f\u5de5\u5177\u83b7\u5f97", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u8fd8\u6709\u4e00\u4e2a\u62d6\u653e\u6211\u6ca1\u5b9e\u73b0", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u5de5\u5730", None))
        self.label.setText(QCoreApplication.translate("Form", u"codes", None))
    # retranslateUi