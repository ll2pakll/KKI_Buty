from menus.pyqt_files.game_start_menu.DS_game_start_menu import *
from Help_Fn.functions import *
import Global.variables as gv
from PyQt5.QtWidgets import QDesktopWidget

class Game_start_menu_widget(Ui_game_start_menu):
    def __init__(self, MainWindow, stacked_widget_general=None, stack_dict_general=None):
        super(Game_start_menu_widget, self).__init__()
        self.setupUi(MainWindow)

        '''делаем основное окно общедоступным для всего класса'''
        self.game_start_menu = MainWindow

        self.stacked_widget_general = stacked_widget_general
        self.stack_dict_general = stack_dict_general

        self.add_connects()

    def add_connects(self):
        """связь сигналов"""
        self.btn_start.clicked.connect(self.btn_start_clicked)

    def btn_start_clicked(self):
        self.stacked_widget_general.setCurrentWidget(self.stack_dict_general["playground"][1])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game_start_menu = QtWidgets.QDialog()
    Game_start_menu_widget(game_start_menu)
    game_start_menu.showMaximized()
    sys.exit(app.exec_())
