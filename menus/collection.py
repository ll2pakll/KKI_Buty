from pyqt_files.collection.collection import *
from Help_Fn.functions import *
from Global.variables import *


class Collection_manual(Ui_Collection):
    def __init__(self, Collection):
        super(Collection_manual, self).__init__()
        self.setupUi(Collection)

        self.Collection = Collection
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
        icon.addPixmap(QtGui.QPixmap("../../Global_collection/DataFaces/00000.jpg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        _translate = QtCore.QCoreApplication.translate
        for i in self.button_list:
            i.setIcon(icon)
            i.setText(_translate("Collection", ""))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Collection = QtWidgets.QMainWindow()
    ui = Collection_manual(Collection)
    Collection.show()
    sys.exit(app.exec_())