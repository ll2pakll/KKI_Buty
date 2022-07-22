import Global.variables as gv
import menus.box
from menus.pyqt_files.start_menu.start_menu import *
from Help_Fn.functions import *
from menus.box import *

class Start_menu_widget(Ui_Start_menu):
    def __init__(self, MainWindow, stack=None, stack_dict=None):
        super(Start_menu_widget, self).__init__()
        self.setupUi(MainWindow)

        self.Start_menu = MainWindow
        self.stack = stack
        self.centralwidget.setLayout(self.horizontalLayout)

        self.add_connects()

    def add_connects(self):
        '''связь сигналов'''
        self.Play.clicked.connect(lambda: self.on_click(self.Play.objectName()))
        self.Collection.clicked.connect(self.collection_btn_clicked)

    # инструкции при нажатии
    def collection_btn_clicked(self):
        self.stack.setCurrentIndex(box_index)

    def on_click(self, btn_name):
        if btn_name == "Play":
            pass
        elif btn_name == "Collection":
            subprocess.call(('python', gv.path_global_collection_py))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Start_menu_widget(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())