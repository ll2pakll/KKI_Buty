from PyQt5 import QtWidgets
import Global.variables as gv
from menus.global_menu import Start_menu
from menus.box import Box
from PyQt5.QtWidgets import QDesktopWidget

class Stack_Widgets(QtWidgets.QMainWindow):
    def __init__(self):
        super(Stack_Widgets, self).__init__()
        self.setWindowTitle("Beauty_collection")

        # создаём и устанавливаем центральный виджет
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)

        # создаём стек виджетов
        self.stack = QtWidgets.QStackedWidget()

        # создаём главный лейаут, наполняем его
        # и помещаем на главный виджет
        self.Main_Layout = QtWidgets.QHBoxLayout()
        self.Main_Layout.addWidget(self.stack)
        self.centralwidget.setLayout(self.Main_Layout)

        # создаём словарь с добавленными виджетами (добавляется не сам
        # виджет, а окно которое он обработал
        self.stack_dict = {}

        # добовляем виджеты в стек, от порядка добавления зависит индекс
        # виджета в стеке, эти индексы привязаны к переменным в "Global.variables.py"
        self.add_widget(Start_menu)
        self.add_widget(Box)

    def add_widget(self, class_widget):
        '''функция принимает название класса виджета и добавляет окно этого виджета
        в стек вджетов, а так же добавляет ссылку на это окно виджета в словарь виджетов,
        с ключём по названию виджета'''
        window = QtWidgets.QMainWindow()
        widget = class_widget(window, self.stack)
        self.stack_dict[widget.objectName()] = window
        self.stack.addWidget(self.stack_dict[widget.objectName()])




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stack_Widgets = Stack_Widgets()
    stack_Widgets.showMaximized()
    sys.exit(app.exec_())