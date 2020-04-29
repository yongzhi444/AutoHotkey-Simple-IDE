from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Compile_Window(object):
    def __init__(self):
        super(Compile_Window, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(746, 427)
        Form.setMinimumSize(QSize(746, 427))
        Form.setMaximumSize(QSize(746, 427))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 190, 72, 15))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 70, 641, 102))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.a_line = QLineEdit(self.layoutWidget)
        self.a_line.setObjectName(u"a_line")

        self.verticalLayout.addWidget(self.a_line)

        self.b_line = QLineEdit(self.layoutWidget)
        self.b_line.setObjectName(u"b_line")

        self.verticalLayout.addWidget(self.b_line)

        self.c_line = QLineEdit(self.layoutWidget)
        self.c_line.setObjectName(u"c_line")
        self.c_line.setReadOnly(False)

        self.verticalLayout.addWidget(self.c_line)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.a_choose = QPushButton(self.layoutWidget)
        self.a_choose.setObjectName(u"a_choose")

        self.verticalLayout_2.addWidget(self.a_choose)

        self.b_choose = QPushButton(self.layoutWidget)
        self.b_choose.setObjectName(u"b_choose")

        self.verticalLayout_2.addWidget(self.b_choose)

        self.c_choose = QPushButton(self.layoutWidget)
        self.c_choose.setObjectName(u"c_choose")

        self.verticalLayout_2.addWidget(self.c_choose)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 20, 641, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.start = QPushButton(self.layoutWidget1)
        self.start.setObjectName(u"start")

        self.horizontalLayout_2.addWidget(self.start)

        self.listView = QListView(Form)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(40, 220, 631, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Compile", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u56fe\u6807\u5e93", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6765\u6e90\u6587\u4ef6(.ahk/.bs)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u6587\u4ef6(.exe)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u56fe\u6807\u6587\u4ef6", None))
        self.a_line.setInputMask("")
        self.a_line.setPlaceholderText(QCoreApplication.translate("Form", u"\u7a7a\u8868\u793a\u4f7f\u7528\u7f16\u8f91\u5668\u4e2d\u7684\u4ee3\u7801", None))
        self.a_choose.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.b_choose.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.c_choose.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7f16\u8bd1\u9009\u9879", None))
        self.start.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u7f16\u8bd1", None))
    # retranslateUi