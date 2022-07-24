# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Collection(object):
    def setupUi(self, Collection):
        Collection.setObjectName("Collection")
        Collection.resize(1124, 936)
        self.centralwidget = QtWidgets.QWidget(Collection)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.QVB_deck_layout = QtWidgets.QVBoxLayout()
        self.QVB_deck_layout.setObjectName("QVB_deck_layout")
        self.clear_deck = QtWidgets.QPushButton(self.centralwidget)
        self.clear_deck.setObjectName("clear_deck")
        self.QVB_deck_layout.addWidget(self.clear_deck)
        self.deck_name = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deck_name.sizePolicy().hasHeightForWidth())
        self.deck_name.setSizePolicy(sizePolicy)
        self.deck_name.setObjectName("deck_name")
        self.QVB_deck_layout.addWidget(self.deck_name)
        self.gridLayout_2.addLayout(self.QVB_deck_layout, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: rgb(90, 87, 82);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1000, 1000))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(1000, 1000))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.gridWidget.setStyleSheet("background-color: rgb(82, 106, 113);")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_1 = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QtCore.QSize(512, 512))
        self.pushButton_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Global_collection/DataFaces/00000.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setIconSize(QtCore.QSize(256, 256))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_3.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.gridWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 3, 1, 1)
        Collection.setCentralWidget(self.centralwidget)

        self.retranslateUi(Collection)
        QtCore.QMetaObject.connectSlotsByName(Collection)

    def retranslateUi(self, Collection):
        _translate = QtCore.QCoreApplication.translate
        Collection.setWindowTitle(_translate("Collection", "MainWindow"))
        self.clear_deck.setText(_translate("Collection", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Collection = QtWidgets.QMainWindow()
    ui = Ui_Collection()
    ui.setupUi(Collection)
    Collection.show()
    sys.exit(app.exec_())
