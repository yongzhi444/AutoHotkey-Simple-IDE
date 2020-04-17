from PySide2 import QtGui
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
import a_frame as aa

class out:
    def __init__(self):
        self.ui = QUiLoader().load("flattst.ui")
        # self.ui = Ui_Form()
        # self.ui下就会有控件的名字
        # self.ui.the_btn.clicked.connect(funs.sayit)
        self.ui.frame = aa.Ui_Frame()
        pass



app = QApplication([])
op = out()
op.ui.show()
app.exec_()
