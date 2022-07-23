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

        '''создаём экземлпяры служебных классов'''
        self.Files = Files()

        '''задаём отображаемый размер изображений'''
        self.img_size = 512

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

        '''список кнопок в колоде'''
        self.buttons_deck = [None] * 6

        '''список выбранных карт, сюда помещаются пути к изображениям для 
        кнопок колоды'''
        self.buttons_deck_path_list = [None]*6

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
        self.location_on_the_screen()

    '''Это функция которая позволяет позиционировать окно при запуске'''
    def location_on_the_screen(self):
        sg = QDesktopWidget().screenGeometry()
        widget = self.Collection.geometry()

        x = (sg.width() - widget.width())//2
        y = 0
        self.Collection.move(x, y)

    '''инструкция при нажатии сюда посылаем источник откуда пришёл сигнал
    и информацию сигнала'''
    def on_click(self, sours, data):
        print(self.Collection.sender().objectName())
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

        if sours == 'deck':
            self.buttons_deck[data].setIcon(QtGui.QIcon())
            self.buttons_deck_path_list[data] = None

    def pbtn_collection_creater(self):
        '''Создание кнопок с изображениями из коллекции'''
        '''создаём экземляр класса изображения'''
        self.icon = QtGui.QIcon()
        '''создаём общую политику размеров для кнопок'''
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
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

            '''создаём "замыкание" для того что бы лямбда правильно работала'''

            def on_click_lambda(x, y):
                return lambda: self.on_click(x, y)

            '''создаём привязку нажатия к функции нажатия, посылаем индекс из списка
            кнопок коллекции'''
            self.buttons_collection[i][0].clicked.connect(on_click_lambda('collection', i))

    def pbtn_deck_creater(self):
        '''создаём "замыкание" для того что бы лямбда правильно работала'''
        def on_click_lambda(x, y):
            return lambda: self.on_click(x, y)

        '''Создание иконок карт выбранных для игры'''
        for i in range(6):
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setObjectName("pushButton_deck" + str(i))
            self.pushButton.setSizePolicy(self.sizePolicy)
            self.pushButton.setMinimumSize(QtCore.QSize(self.img_size // 2, self.img_size // 2))
            self.gridLayout_4.addWidget(self.pushButton, i, 0, 1, 1)
            self.buttons_deck[i] = self.pushButton
            self.buttons_deck[i].clicked.connect(on_click_lambda('deck', i))


if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Collection_widget(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())