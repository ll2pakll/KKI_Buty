from pyqt_files.collection.collection import *
from Help_Fn.functions import *
from Global.variables import *


class Collection_manual(Ui_Collection):
    def __init__(self, Collection):
        super(Collection_manual, self).__init__()
        self.setupUi(Collection)

        # Classs
        self.Files = Files()
        self.Collection = Collection

        with open(path_collection, 'rb') as f:
            self.collection = pickle.load(f)
        self.collection_list = list()
        for k, i in self.collection.items():
            self.collection_list.append(k)

        self.collection_list = sorted(self.collection_list)


        self.button_list = [self.pushButton_1,
                            self.pushButton_2,
                            self.pushButton_3,
                            self.pushButton_4,
                            self.pushButton_5,
                            self.pushButton_6,
                            self.pushButton_7,
                            self.pushButton_8,
                            self.pushButton_9,
                            self.pushButton_10,
                            self.pushButton_11,
                            self.pushButton_12]
        self.Ui_chenges()

    def Ui_chenges(self):
        # переопределённые данные которые необходимо обновлять во время работы программы
        self.Collection.resize(1920, 1080)

        icon = QtGui.QIcon()
        for i in range(len(self.button_list)):
            icon.addPixmap(QtGui.QPixmap("../../Global_collection/DataFaces/"+self.collection_list[i]).scaled(512, 512), QtGui.QIcon.Normal,
                           QtGui.QIcon.On)
            _translate = QtCore.QCoreApplication.translate
            self.button_list[i].setIcon(icon)
            self.button_list[i].setIconSize(QtCore.QSize(512, 512))
            self.button_list[i].setText(_translate("Collection", ""))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Collection = QtWidgets.QMainWindow()
    ui = Collection_manual(Collection)
    Collection.show()
    sys.exit(app.exec_())