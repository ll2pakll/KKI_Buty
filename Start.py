from pyqt_files.menu_1.menu_1 import *
from Help_Fn.functions import *

class Start(Ui_Dialog):
    def __init__(self, Dialog):
        super(Start, self).__init__()
        self.setupUi(Dialog)

        self.Dialog = Dialog
        self.Dialog.resize(1200, 1000)

        self.Ui_chenges()
        # self.retranslateUi_chenges()

    def Ui_chenges(self):
        self.verticalWidget.setGeometry(QtCore.QRect(20, 30, int(self.Dialog.width()*0.95), int(self.Dialog.height()*0.95)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Start(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())