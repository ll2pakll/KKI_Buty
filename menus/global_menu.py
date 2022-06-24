import Global.variables
from pyqt_files.global_menu.global_menu import *
from Help_Fn.functions import *

class Start(Ui_Global_menu):
    def __init__(self, Global_menu):
        super(Start, self).__init__()
        self.setupUi(Global_menu)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())