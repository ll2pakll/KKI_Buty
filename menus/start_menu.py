from menus.pyqt_files.start_menu.DS_start_menu import *
from menus.box import *

class Start_menu_widget(Ui_Start_menu):
    def __init__(self, MainWindow, stacked_widget_general=None, stack_dict_general=None):
        super(Start_menu_widget, self).__init__()
        self.setupUi(MainWindow)

        self.Start_menu = MainWindow
        self.stacked_widget_general = stacked_widget_general
        self.stack_dict_general = stack_dict_general
        self.centralwidget.setLayout(self.horizontalLayout)

        self.add_connects()

    def add_connects(self):
        '''связь сигналов'''
        self.Play.clicked.connect(self.playground_btn_clicked)
        self.Collection.clicked.connect(self.collection_btn_clicked)

    # инструкции при нажатии
    def collection_btn_clicked(self):
        self.stacked_widget_general.setCurrentWidget(self.stack_dict_general["Collection"][1])

    def playground_btn_clicked(self):
        self.stacked_widget_general.setCurrentWidget(self.stack_dict_general["game_start_menu"][1])

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