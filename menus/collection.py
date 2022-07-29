from menus.pyqt_files.collection.collection import *
from Help_Fn.functions import *
import Global.variables as gv
from PyQt5.QtWidgets import QDesktopWidget


class Collection_widget(Ui_Collection):
    def __init__(self, MainWindow, stacked_widget_general=None, stack_dict_general=None):
        super(Collection_widget, self).__init__()
        self.setupUi(MainWindow)

        '''делаем основное окно общедоступным для всего класса'''
        self.Collection = MainWindow

        """меняем текущую дирректорию на корневой котолог"""
        os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

        '''создаём экземлпяры служебных классов'''
        self.Files = Files()

        """Создаём экземпляр иконки, что бы не создавать её
        каждый раз там где можно использовать этот экзмепляр"""
        self.icon = QtGui.QIcon()

        '''создаём общую политику размеров что бы использовать там
        где можно не создавать новую политику'''
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        '''задаём отображаемый размер изображений'''
        self.img_size = QDesktopWidget().width()//10

        """если нет файла с коллекцией игрока, он создаётся"""
        if not os.path.isfile(gv.path_collection):
            pickle_save(dict(), gv.path_collection)

        '''открываем коллекцию и сортируем её по имени'''
        with open(gv.path_collection, 'rb') as f:
            self.collection = pickle.load(f)
        self.collection_list = list()
        for k, i in self.collection.items():
            self.collection_list.append(k)
        self.collection_list = sorted(self.collection_list)

        '''список кнопок в коллеции'''
        self.buttons_collection = [None] * len(self.collection_list)

        """если нет файла с колодами игрока, он создаётся"""
        if not os.path.isfile(gv.path_decks):
            pickle_save(dict(), gv.path_decks)

        """открываем файл с колодами"""
        with open(gv.path_decks, 'rb') as f:
            self.decks = pickle.load(f)

        """создаём переменную с количеством сохранённых колод"""
        self.decks_len = len(self.decks)

        """определяем размер колоды"""
        self.deck_len = 6

        '''список кнопок в колоде'''
        self.buttons_deck = [None] * self.deck_len

        """список конопок сохранённых колод"""
        self.buttons_decks = {}

        '''список выбранных карт, сюда помещаются пути к изображениям для 
        кнопок колоды'''
        self.buttons_deck_path_list_empty = [None]*self.deck_len
        self.buttons_deck_path_list = self.buttons_deck_path_list_empty.copy()

        '''определяем скорость прокрутки коллекции колёсиком мышки'''
        self.scrollArea.verticalScrollBar().setSingleStep(self.img_size // 7)

        '''задаём размер окна ориентируясь на разрешение экрана'''
        self.Collection.resize(int(QDesktopWidget().screenGeometry().width() * 0.9),
                               int(QDesktopWidget().screenGeometry().height() * 0.89))

        '''задаём размер поля в котором будут отображаться карты из коллекции'''
        self.scrollAreaWidgetContents_2.setMinimumSize(
            QtCore.QSize(int(self.img_size * 4 * 1.1), (len(self.collection_list) // 4)
                         * int(self.img_size * 1.1) + self.img_size))

        '''функции'''
        self.pbtn_collection_creater()
        self.pbtn_deck_creater()
        self.add_connects()

    def add_connects(self):
        '''связь сигналов'''
        self.clear_deck.clicked.connect(self.on_click)
        self.save_deck.clicked.connect(self.on_click)

    def on_click(self, sours=None, data=None):
        '''инструкция при нажатии сюда посылаем источник откуда пришёл сигнал
            и информацию сигнала'''
        if sours == 'collection':
            path = self.buttons_collection[data][1]
            if path not in self.buttons_deck_path_list:
                try:
                    index = self.buttons_deck_path_list.index(None)
                    self.icon.addPixmap(QtGui.QPixmap(path).scaled(self.img_size // 2, self.img_size // 2),
                                        QtGui.QIcon.Normal,
                                        QtGui.QIcon.On)
                    self.buttons_deck_path_list[index] = path
                    self.buttons_deck[index].setIcon(self.icon)
                    self.buttons_deck[index].setIconSize(QtCore.QSize(self.img_size//2, self.img_size//2))
                except:
                    pass

        elif sours == 'deck':
            self.buttons_deck[data].setIcon(QtGui.QIcon())
            self.buttons_deck_path_list[data] = None

        elif sours == 'decks':
            for i in range(len(self.decks[data])):
                self.buttons_deck_path_list[i] = self.decks[data][i]
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.decks[data][i]).scaled(self.img_size // 2, self.img_size // 2),
                                    QtGui.QIcon.Normal,
                                    QtGui.QIcon.On)
                self.buttons_deck[i].setIcon(icon)
                self.buttons_deck[i].setIconSize(QtCore.QSize(self.img_size//2, self.img_size//2))

            self.deck_name.setText(data)

            self.tab_deck_Widget.setCurrentIndex(0)

        elif self.Collection.sender().objectName() == "clear_deck":

            self.buttons_deck_path_list = self.buttons_deck_path_list_empty.copy()
            for i in self.buttons_deck:
                i.setIcon(QtGui.QIcon())

        elif self.Collection.sender().objectName() == "save_deck":
            deck_empty = self.buttons_deck_path_list == self.buttons_deck_path_list_empty
            deck_name_text_empty = self.deck_name.text() == ''
            def deck_save():
                pickle_save(self.decks, gv.path_decks)
                QtWidgets.QMessageBox.information(self.Collection, 'Колода сохранена',
                                                  f'Колода сохранена под именем "{self.deck_name.text()}"')
            if deck_empty:
                QtWidgets.QMessageBox.warning(self.Collection, 'Внимание', 'Колода пуста. Наполните её прежде чем сохранять')
            elif deck_name_text_empty:
                QtWidgets.QMessageBox.critical(self.Collection, 'Внимание', 'Назовите колоду, иначе она не сохранится!')
            elif None in self.buttons_deck_path_list:
                QtWidgets.QMessageBox.warning(self.Collection, 'Внимание', 'Колода не полная. '
                                                'Пока вы её не наполните вы не сможете с ней играть')
            if not deck_empty and not deck_name_text_empty and self.deck_name.text() not in self.decks.keys():
                self.decks[self.deck_name.text()] = self.buttons_deck_path_list
                deck_save()
            elif not deck_empty and not deck_name_text_empty and self.deck_name.text() in self.decks.keys():
                if QtWidgets.QMessageBox.question(self.Collection, 'Такая колода уже есть',
                                                  f'Колода с именем "{self.deck_name.text()}" уже существует, '
                                                  f'вы хотите перезаписать её?') == 16384:
                    pickle_save(self.decks, gv.path_decks)
                    deck_save()

    def pbtn_collection_creater(self):
        '''Создание кнопок с изображениями из коллекции'''

        for i in range(len(self.collection_list)):
            path = gv.path_global_collection_datafaces + '\\' + self.collection_list[i]
            card = Card(path, self.collection_list[i], self.img_size)
            card.set_layout(self.gridLayout_3, True, (i // 4, i % 4, 1, 1))
            self.buttons_collection[i] = (card.get_pushButton(), card.get_path())
            self.buttons_collection[i][0].clicked.connect(self.on_click_lambda('collection', i))


    def pbtn_deck_creater(self):
        self.indent_between_cards = 1.1
        '''Создание области для работы с колодами'''
        self.new_deck_widget = QtWidgets.QWidget()
        self.new_deck_widget.setMinimumWidth(int(self.img_size//2*1.35))
        self.QVB_deck = QtWidgets.QVBoxLayout()
        self.new_deck_widget.setLayout(self.QVB_deck)

        """Помещаем поле для ввода названия колоды на своё место"""
        self.QVB_deck.addWidget(self.deck_name)

        """Создание области с картами"""
        self.scrollArea_deck = QtWidgets.QScrollArea()
        self.QVB_deck.addWidget(self.scrollArea_deck)

        self.scrollArea_deck_widget = QtWidgets.QWidget()
        self.scrollArea_deck_widget.setGeometry(QtCore.QRect(0, 0, int((self.img_size // 2) * self.indent_between_cards),
                                                    int((self.img_size // 2) * self.deck_len * self.indent_between_cards)))
        self.QVB_scrollArea_deck_widgetleyout = QtWidgets.QVBoxLayout()
        self.scrollArea_deck_widget.setLayout(self.QVB_scrollArea_deck_widgetleyout)
        self.scrollArea_deck.setWidget(self.scrollArea_deck_widget)

        """Цикл размещения кнопок с картами в области создания колоды"""
        for i in range(self.deck_len):
            card = Card(obgect_name='card' + str(i), size=self.img_size // 2)
            card.set_layout(self.QVB_scrollArea_deck_widgetleyout)
            self.buttons_deck[i] = card.get_pushButton()
            self.buttons_deck[i].clicked.connect(self.on_click_lambda('deck', i))

        """создаём в этом же лейауте горизонтальный лейаут и добавляем на него
        кнопки save и clear"""
        self.QHB_save_clear_btn_layout = QtWidgets.QHBoxLayout()
        self.save_deck = QtWidgets.QPushButton()
        self.save_deck.setObjectName("save_deck")
        self.save_deck.setText('Save')
        self.clear_deck = QtWidgets.QPushButton(self.centralwidget)
        self.clear_deck.setObjectName("clear_deck")
        self.clear_deck.setText("Clear")
        self.QVB_deck_layout.addWidget(self.clear_deck)
        self.QHB_save_clear_btn_layout.addWidget(self.save_deck)
        self.QHB_save_clear_btn_layout.addWidget(self.clear_deck)
        self.QVB_deck.addLayout(self.QHB_save_clear_btn_layout)

        """добавляем в коно ввода имени колоды подсказку для пользователя"""
        self.deck_name.setPlaceholderText('Введи имя колоды')

        """добавляем закладку в которую помещаем разметку для создания колоды"""
        self.tab_deck_Widget.removeTab(0)
        self.tab_deck_Widget.addTab(self.new_deck_widget, 'Создание колоды')

        self.deck_selector()

    def deck_selector(self):
        """создаём область куда будут загружаться уже созданные колоды"""

        """прокручиваемая область для того что бы можно было загружать много колод"""
        self.scrollArea_selector = QtWidgets.QScrollArea()

        """виджет который будет помещён на скролл эреа"""
        self.deck_selector_scrollArea_widget = QtWidgets.QWidget()
        self.deck_selector_scrollArea_widget.setGeometry(QtCore.QRect(0, 0, int((self.img_size // 2)*self.indent_between_cards),
                                                    int((self.img_size // 2)*self.decks_len*self.indent_between_cards)))
        self.scrollAreaWidgetContents_2.setSizePolicy(self.sizePolicy)
        self.QVB_selector_widget_scrollArea_leyout = QtWidgets.QVBoxLayout()
        self.deck_selector_scrollArea_widget.setLayout(self.QVB_selector_widget_scrollArea_leyout)
        self.scrollArea_selector.setWidget(self.deck_selector_scrollArea_widget)

        """Создаём кнопки с колодами и иконками первой карты из колоды"""
        for k, i in self.decks.items():
            for p in self.decks[k]:
                if p:
                    icon_path = p
                    break

            card = Card(icon_path, "deck" + ' - ' + str(k), self.img_size // 2)
            card.set_layout(self.QVB_selector_widget_scrollArea_leyout)
            self.buttons_decks[k] = card.pushButton
            self.buttons_decks[k].clicked.connect(self.on_click_lambda('decks', k))

        self.tab_deck_Widget.addTab(self.scrollArea_selector, 'Сохранённые колоды')

    def on_click_lambda(self, x, y):
        '''создаём "замыкание" для того что бы лямбда правильно работала'''
        return lambda: self.on_click(x, y)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Collection_widget(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())