import subprocess

import Global.variables
from pyqt_files.global_menu.global_menu import *
from Help_Fn.functions import *

class Start(Ui_Global_menu):
    def __init__(self, Global_menu):
        super(Start, self).__init__()
        self.setupUi(Global_menu)

        self.Global_menu = Global_menu
        self.Global_menu.resize(Global.variables.window_width, Global.variables.window_height)

        self.add_function()

    def add_function(self):
        self.Play.clicked.connect(lambda: self.on_click(self.Play.objectName()))
        self.Collection.clicked.connect(lambda: self.on_click(self.Collection.objectName()))

    # инструкции при нажатии
    def on_click(self, btn_name):
        if btn_name == "Play":
            pass
        elif btn_name == "Collection":
            subprocess.call(('python', Global.variables.path_global_collection_py))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())