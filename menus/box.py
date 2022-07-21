from menus.pyqt_files.box.box import *
from Help_Fn.functions import *
from Global.variables import *



class Box(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, MainWindow, stack=None):
        super(Box, self).__init__()
        self.setupUi(MainWindow)

        self.MainWindow = MainWindow

        self.setObjectName('Box')

        #Static:

        # Classes
        self.files = Files()  # класс для работы с файлами
        self.meta_data = Meta_data()

        #paths:
        self.paths_list = self.files.get_tree(path_global_collection)
        if not os.path.isfile(path_collection):
            pickle_save(dict(), path_collection)
        with open(path_collection, 'rb') as f:
            self.collection = pickle.load(f)
        self.len_paths_list = len(self.paths_list)
        self.path_generator = Path_generator(self.paths_list)

        #variables:


        #----------------------------------------------------------------------------
        self.add_function()
        self.open_boxes()
        self.actions()
    # функция которую надо запускать что бы обновить окно и данные
    def actions(self):
        if not self.boxes_number:
            sys.exit()
        self.get_paths_and_metas()
        self.Ui_chenges()
        self.retranslateUi_1(self.MainWindow)
        self.boxes_number -= 1

    # на данный момент это функция реагирования на нажатие
    def add_function(self):
        self.img_1.clicked.connect(lambda: self.on_click(self.img_1.objectName()))
        self.img_2.clicked.connect(lambda: self.on_click(self.img_2.objectName()))

    # инструкции при нажатии
    def on_click(self, btn_name):
        if btn_name == "img_1":
            self.meta_1['scores'] += 1
            self.meta_2['scores'] -= 1
            self.meta_1['history_comparison'].add(self.files.get_deep_file(self.path_file_2, -2))
            self.meta_2['history_comparison'].add(self.files.get_deep_file(self.path_file_1, -2))
            self.collection_add(self.path_file_1)

        elif btn_name == "img_2":
            self.meta_2['scores'] += 1
            self.meta_1['scores'] -= 1
            self.meta_1['history_comparison'].add(self.files.get_deep_file(self.path_file_2, -2))
            self.meta_2['history_comparison'].add(self.files.get_deep_file(self.path_file_1, -2))
            self.collection_add(self.path_file_2)

        self.both_metadata_save()
        pickle_save(self.collection, path_collection)
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

    def open_boxes(self, boxes_number=None):
        """функция запуска открывания боксов. В качестве аргумента указывается целове число, которое определяет
        количество боксов которые требуется открыть. Если аргумент не передан, боксы открываются до тех пор, пока
        пользователь не закроет окно"""
        if boxes_number:
            self.boxes_number = boxes_number
        else:
            self.boxes_number = float('inf')



    def Ui_chenges(self):
        # переопределённые данные которые необходимо обновлять во время работы программы
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(self.path_file_1)).scaled(768, 768), QtGui.QIcon.Normal,
                       QtGui.QIcon.On)
        self.img_1.setIcon(icon)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(self.path_file_2)).scaled(768, 768), QtGui.QIcon.Normal,
                        QtGui.QIcon.On)
        self.img_2.setIcon(icon1)

    def retranslateUi_1(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_name_1.setText(_translate("MainWindow", self.file_name_1))
        self.lb_name_2.setText(_translate("MainWindow", self.file_name_2))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Box(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())