import os
from threading import Thread


def thread_target(self):
    my_command = "AutoHotkeyU64.exe temp.ahk"
    os.system(my_command)


# def run_btn_clicked(self):
#     with open("temp.ahk", "w", encoding="gbk") as fp:
#         context = self.ui.code_text.toPlainText()
#         fp.write(context)
#     t = Thread(target=self.run_btn_clicked, daemon=True)
#     t.start()
#     t.join()

thread_target(1)
