from Buty.Buty_interface import *
from Help_Fn.functions import *



class Buty(Ui_MainWindow):
    def __init__(self, MainWindow):
        super(Buty, self).__init__()
        self.setupUi(MainWindow)

        #Static:

        # Classes
        self.files = Files()  # класс для работы с файлами
        self.meta_data = Meta_data()

        #paths:
        self.paths_list = self.files.get_tree(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Buty_frames')))
        self.len_paths_list = len(self.paths_list)
        self.path_generator = Path_generator(self.paths_list)

        #создаём пути для первых фотографий
        self.get_paths_and_metas()

        #variables:

        #----------------------------------------------------------------------------

        self.actions()
        self.add_function()

    # функция которую надо запускать что бы обновить окно и данные
    def actions(self):
        self.Ui_chenges()
        self.retranslateUi_1(MainWindow)

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
            self.both_metadata_save()
            self.get_paths_and_metas()

        elif btn_name == "img_2":
            self.meta_2['scores'] += 1
            self.meta_1['scores'] -= 1
            self.meta_1['history_comparison'].add(self.files.get_deep_file(self.path_file_2, -2))
            self.meta_2['history_comparison'].add(self.files.get_deep_file(self.path_file_1, -2))
            self.both_metadata_save()
            self.get_paths_and_metas()
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
    ui = Buty(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())