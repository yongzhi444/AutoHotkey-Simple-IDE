from PySide2.QtUiTools import QUiLoader


class setting_show:
    def __init__(self):
        self.ui = QUiLoader().load('setting.ui')
