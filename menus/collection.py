from menus.pyqt_files.collection.collection import *
from Help_Fn.functions import *
import Global.variables as gv
from PyQt5.QtWidgets import QDesktopWidget
import functools


class Collection_widget(Ui_Collection):
    def __init__(self, MainWindow, stacked_widget_general=None, stack_dict_general=None):
        super(Collection_widget, self).__init__()
        self.setupUi(MainWindow)

        '''делаем основное окно общедоступным для всего класса'''
        self.Collection = MainWindow

        '''создаём экземлпяры служебных классов'''
        self.Files = Files()

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

        """если нет файла с колодами игрока, он создаётся"""
        if not os.path.isfile(gv.path_decks):
            pickle_save(dict(), gv.path_decks)

        '''список кнопок в коллеции'''
        self.buttons_collection = [None] * len(self.collection_list)

        """открываем файл с колодами"""
        with open(gv.path_decks, 'rb') as f:
            self.decks = pickle.load(f)

        """определяем размер колоды"""
        self.deck_len = 6

        '''список кнопок в колоде'''
        self.buttons_deck = [None] * self.deck_len

        '''список выбранных карт, сюда помещаются пути к изображениям для 
        кнопок колоды '''
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
        self.location_on_the_screen()


    def location_on_the_screen(self):
        '''Это функция которая позволяет позиционировать окно при запуске'''
        sg = QDesktopWidget().screenGeometry()
        widget = self.Collection.geometry()

        x = (sg.width() - widget.width())//2
        y = 0
        self.Collection.move(x, y)

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

        elif self.Collection.sender().objectName() == "clear_deck":
            self.buttons_deck_path_list = [None] * 6
            for i in self.buttons_deck:
                i.setIcon(QtGui.QIcon())

        elif self.Collection.sender().objectName() == "save_deck":
            deck_empty = self.buttons_deck_path_list == self.buttons_deck_path_list_empty
            deck_name_text_empty = self.deck_name.text() == ''
            def deck_saved():
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
                deck_saved()
            elif not deck_empty and not deck_name_text_empty and self.deck_name.text() in self.decks.keys():
                if QtWidgets.QMessageBox.question(self.Collection, 'Такая колода уже есть',
                                                  f'Колода с именем "{self.deck_name.text()}" уже существует, '
                                                  f'вы хотите перезаписать её?') == 16384:
                    pickle_save(self.decks, gv.path_decks)
                    deck_saved()

    def pbtn_collection_creater(self):
        '''Создание кнопок с изображениями из коллекции'''
        '''создаём экземляр класса изображения'''
        self.icon = QtGui.QIcon()
        '''создаём общую политику размеров для кнопок'''
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        for i in range(len(self.collection_list)):
            self.pushButton = QtWidgets.QPushButton(self.gridWidget)
            self.pushButton.setObjectName("pushButton" + str(i))
            self.pushButton.setSizePolicy(self.sizePolicy)
            self.pushButton.setMinimumSize(QtCore.QSize(self.img_size, self.img_size))
            if __name__ == "__main__":
                path = "../../Global_collection/DataFaces/" + self.collection_list[i]
            else:
                path = "../Global_collection/DataFaces/" + self.collection_list[i]
            self.icon.addPixmap(QtGui.QPixmap(path).scaled(self.img_size, self.img_size),
                                QtGui.QIcon.Normal,
                                QtGui.QIcon.On)
            self.pushButton.setIcon(self.icon)
            self.pushButton.setIconSize(QtCore.QSize(self.img_size, self.img_size))
            self.gridLayout_3.addWidget(self.pushButton, i // 4, i % 4, 1, 1)
            self.buttons_collection[i] = (self.pushButton, path)

            '''создаём привязку нажатия к функции нажатия, посылаем индекс из списка
            кнопок коллекции'''
            self.buttons_collection[i][0].clicked.connect(self.on_click_lambda('collection', i))

    def pbtn_deck_creater(self):
        '''Создание иконок карт выбранных для игры'''
        for i in range(self.deck_len):
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setObjectName("pushButton_deck" + str(i))
            self.pushButton.setSizePolicy(self.sizePolicy)
            self.pushButton.setMinimumSize(QtCore.QSize(self.img_size // 2, self.img_size // 2))
            self.QVB_deck_layout.addWidget(self.pushButton)
            self.buttons_deck[i] = self.pushButton
            self.buttons_deck[i].clicked.connect(self.on_click_lambda('deck', i))

        """создаём в этом же лейауте кнопку для сохранения"""
        self.save_deck = QtWidgets.QPushButton()
        self.save_deck.setObjectName("save_deck")
        self.save_deck.setText('Save')
        self.QVB_deck_layout.addWidget(self.save_deck)

        """добавляем в коно ввода имени колоды подсказку для пользователя"""
        self.deck_name.setPlaceholderText('Введи имя колоды')

    def on_click_lambda(self, x, y):
        '''создаём "замыкание" для того что бы лямбда правильно работала'''
        return lambda: self.on_click(x, y)

if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Collection_widget(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())