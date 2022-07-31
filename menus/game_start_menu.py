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

        """создаём экземлпяры служебных классов"""
        self.files = Files()

        """если нет файла с колодами игрока, он создаётся"""
        """открываем файл с колодами"""
        self.decks = self.files.open_player_decks()

        """список конопок сохранённых колод"""
        self.buttons_decks = {}

        self.decks_menu()
        self.add_connects()

    def add_connects(self):
        """связь сигналов"""
        self.btn_start.clicked.connect(self.on_click)

    def on_click(self, sours=None, data=None):
        if sours == 'decks':
            if self.choised_deck_key:
                self.coloreEffect.setEnabled(False)
            self.buttons_decks[data].setGraphicsEffect(self.coloreEffect)
            self.coloreEffect.setEnabled(True)
            self.choised_deck_key = data
            self.deck_name.setText(data)

        elif self.game_start_menu.sender().objectName() == "btn_start":
            self.stacked_widget_general.setCurrentWidget(self.stack_dict_general["playground"][1])

    def decks_menu(self):
        '''задаём отображаемый размер изображений'''
        self.img_size = QDesktopWidget().width() // 10

        self.decks_gridLayout = QtWidgets.QGridLayout()
        self.decks_scrollAreaWidgetContents.setLayout(self.decks_gridLayout)
        self.decks_scrollAreaWidgetContents.setMinimumSize(
            QtCore.QSize(int(self.img_size * 4 * 1.1), (len(self.decks) // 4)
                         * int(self.img_size * 1.1) + self.img_size))

        n = 0
        for k, i in self.decks.items():
            for p in self.decks[k]:
                if p:
                    icon_path = p
                    break

            card = Card(icon_path, "deck" + ' - ' + str(k), int(self.img_size)*1.3)
            card.set_layout(self.decks_gridLayout, True, (n // 4, n % 4, 1, 1))
            self.buttons_decks[k] = card.pushButton
            self.buttons_decks[k].clicked.connect(self.on_click_lambda('decks', k))
            n +=1

        """Создаём эффект цвета который будет использоваться для выбора активной колоды, которая
                будет открываться при нажатии на кнопку Open. А так же создаём переменную в которой будет
                хранится ключ выбранной колоды"""
        self.coloreEffect = QtWidgets.QGraphicsColorizeEffect()
        self.coloreEffect.setColor(QtGui.QColor(0, 0, 255, 255))
        self.choised_deck_key = None

    def on_click_lambda(self, x, y):
        '''создаём "замыкание" для того что бы лямбда правильно работала'''
        return lambda: self.on_click(x, y)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game_start_menu = QtWidgets.QDialog()
    Game_start_menu_widget(game_start_menu)
    game_start_menu.showMaximized()
    sys.exit(app.exec_())
