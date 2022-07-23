from menus.pyqt_files.box.box import *
from Help_Fn.functions import *
import Global.variables as gv



class Box_widget(QtWidgets.QMainWindow, Ui_Box):
    def __init__(self, MainWindow, stacked_widget_general=None, stack_dict_general=None):
        super(Box_widget, self).__init__()
        self.setupUi(MainWindow)

        self.Box = MainWindow

        self.centralwidget.setLayout(self.Main_laiout)

        self.stacked_widget_general = stacked_widget_general
        self.stack_dict_general = stack_dict_general

        # Classes
        self.files = Files()  # класс для работы с файлами
        self.meta_data = Meta_data()

        # получаем разрешение экрана и создаём виджет для определения
        # максимального размера изображения в кнопке
        self.resolution = QtWidgets.QDesktopWidget().availableGeometry()
        self.image_size = int((self.resolution.width()//2)*0.95)
        self.image_size_qt = QtCore.QSize(self.image_size, self.image_size)

        #paths:
        """создаём список файлов в глобальной коллеции"""
        self.paths_list = self.files.get_tree(gv.path_global_collection)

        """если нет файла с коллекцией игрока, он создаётся"""
        if not os.path.isfile(gv.path_collection):
            pickle_save(dict(), gv.path_collection)

        """открываем файл с коллекцией игрока"""
        with open(gv.path_collection, 'rb') as f:
            self.collection = pickle.load(f)
        self.len_paths_list = len(self.paths_list)

        """инициализируем экземпляр класса генерирующего пути
        для сравниваемых фотографий"""
        self.path_generator = Path_generator(self.paths_list)

        #----------------------------------------------------------------------------
        self.add_connects()

    def actions(self):
        """обновляет окно и данные"""
        if __name__ != "__main__":
            """если кличество боксов у пользователя равно нулю
            то возможность выбора прекращается, работает только, если программа
            запускалась из другой программы"""
            if not gv.box_quantity:
                self.img_1.setDisabled(True)
                self.img_2.setDisabled(True)
            else:
                self.img_1.setEnabled(True)
                self.img_2.setEnabled(True)

        self.get_paths_and_metas()
        self.Ui_chenges()
        self.retranslateUi_1(self.Box)

    def add_connects(self):
        '''связь сигналов'''
        self.img_1.clicked.connect(self.on_click)
        self.img_2.clicked.connect(self.on_click)

    # инструкции при нажатии
    def on_click(self):
        """В коллекцию файлы добавляются только когда бокс запускается из других виджетов
        это сделано для того что бы можно было тестировать бокс запуская его напрямую, и не
        менять состояние коллецкии"""
        sender = self.sender().objectName()

        if sender == "img_1":
            self.meta_1['scores'] += 1
            self.meta_2['scores'] -= 1
            self.meta_1['history_comparison'].add(self.files.get_deep_file(self.path_file_2, -2))
            self.meta_2['history_comparison'].add(self.files.get_deep_file(self.path_file_1, -2))
            if __name__ != "__main__":
                self.collection_add(self.path_file_1)

        elif sender == "img_2":
            self.meta_2['scores'] += 1
            self.meta_1['scores'] -= 1
            self.meta_1['history_comparison'].add(self.files.get_deep_file(self.path_file_2, -2))
            self.meta_2['history_comparison'].add(self.files.get_deep_file(self.path_file_1, -2))
            if __name__ != "__main__":
                self.collection_add(self.path_file_2)

        self.both_metadata_save()
        if __name__ != "__main__":
            pickle_save(self.collection, gv.path_collection)
            self.chenge_box_quantity(-1)
        else:
            self.actions()

    def get_paths_and_metas(self):
        self.path_file_1, \
        self.path_file_2, \
        self.meta_1, \
        self.meta_2 \
            = self.path_generator.get_paths()
        self.file_name_1 = self.files.get_deep_file(self.path_file_1, -1)
        self.file_name_2 = self.files.get_deep_file(self.path_file_2, -1)

    def both_metadata_save(self):
        self.meta_data.save(self.path_file_1, self.meta_1)
        self.meta_data.save(self.path_file_2, self.meta_2)

    def collection_add(self, path_file):
        if self.files.get_deep_file(path_file, -2, -1) == 'DataFaces':
            self.collection[self.files.get_deep_file(path_file, -1)] = dict()
        else:
            self.collection[self.files.get_deep_file(path_file, -2)] = dict()

    def add_boxes(self, boxes_number=0):
        """функция добавления боксов. В качестве аргумента указывается целое число,
        которое определяет сколько боксов будет добавлено."""
        self.chenge_box_quantity(boxes_number)

    def chenge_box_quantity(self, chenger=0):
        """меняет количество боксов на чилсо кототорое переданов качестве аргумента.
        *число может быть отрицательным"""
        if chenger:
            with open(gv.path_global_variables, 'r', encoding='utf-8') as file:
                variables = file.read().replace(f'box_quantity = {gv.box_quantity}',
                                                f'box_quantity = {gv.box_quantity + chenger}')
                gv.box_quantity += chenger

            with open(gv.path_global_variables, 'w', encoding='utf-8') as file:
                file.write(variables)

        self.actions()



    def Ui_chenges(self):
        # переопределённые данные которые необходимо обновлять во время работы программы
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.path_file_1)).scaled(self.image_size_qt), QtGui.QIcon.Normal,
                       QtGui.QIcon.On)
        self.img_1.setIcon(icon)
        self.img_1.setIconSize(QtCore.QSize(self.image_size_qt))

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(self.path_file_2)).scaled(self.image_size_qt), QtGui.QIcon.Normal,
                        QtGui.QIcon.On)
        self.img_2.setIcon(icon1)
        self.img_2.setIconSize(QtCore.QSize(self.image_size_qt))

    def retranslateUi_1(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_name_1.setText(_translate("MainWindow", self.file_name_1))
        self.lb_name_2.setText(_translate("MainWindow", self.file_name_2))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Box_widget(MainWindow)
    ui.chenge_box_quantity()
    MainWindow.showFullScreen()
    sys.exit(app.exec_())