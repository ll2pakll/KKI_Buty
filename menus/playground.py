import Global.variables as gv
from menus.pyqt_files.playground.DS_playground import *
from Help_Fn.functions import *

class Playground_widget(Ui_playground):
    def __init__(self,  MainWindow, stacked_widget_general=None, stack_dict_general=None):
        super(Playground_widget, self).__init__()
        self.setupUi(MainWindow)

        self.Playground = MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Playground_widget(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())