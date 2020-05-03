from PySide2.QtWidgets import QApplication
from MainWindowLogic import MainWindow

app = QApplication([])
op = MainWindow()
op.ui.show()
app.exec_()