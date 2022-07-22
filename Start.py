from PyQt5 import QtWidgets
import Global.variables as gv
from menus.start_menu import Start_menu_widget
from menus.box import Box_widget
from Help_Fn.functions import *
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
        self.add_widget(Start_menu_widget)
        self.add_widget(Box_widget)

        self.first_run()

    def add_widget(self, class_widget):
        '''функция принимает название класса виджета и добавляет окно этого виджета
        в стек вджетов, а так же добавляет ссылку на это окно виджета в словарь виджетов,
        с ключём по названию виджета'''

        # создаём окно которое будет пропущено через преобразования в виджете
        window = QtWidgets.QMainWindow()
        # создаём класс виджета и пропускаем через него окно
        widget = class_widget(window, self.stack, self.stack_dict)
        # добавляем в словарь ссылку на виджет и окно
        self.stack_dict[window.objectName()] = [widget, window]
        # добовляем окнов стек виджетов
        self.stack.addWidget(self.stack_dict[window.objectName()][1])

    def first_run(self):
        """Проверяем запускает ли пользователь игру впервые.
            Если так то он увидит первоночальные инструкции"""
        with open(gv.path_first_start_chek, 'r') as file:
            first_start = file.read()
        if first_start == 'False':
            first_start_massage = """В этой игре вы составляете свою коллекцию из фотографий случайных людей. \n
Из этой коллекции вы можете составлять игровые колоды, с которыми вы будете сражаться против других игроков. \n
Чем красивее ваши карты, тем больше у вас шансов на победу, потому что сила вашей карты будет зависеть от того, понравится ли она другим пользователям или нет. \n
Ваши карты будут развиваться и эволюционировать. \n
Так же вы можете менять непонравившиеся вам карты, а те, что нравятся наделять уникальными возможностями, делая вашу коллекцию сильнее.\n
Соберите свою уникальную коллекцию и занимайте первые места в рейтинговых соревнованиях и турнирах.
"""
            first_instruction = """Сейчас вы начнёте составлять свою коллекцию. \n
Вам будут предложены 12 пар карт, из которых вы должны выбрать те, что вам больше нравятся.\n
Чем красивее ваша коллекция, тем больше у вас шансов на победу в играх. \n
Вы всегда сможете дополнить свою коллекцию, заменить или удалить непонравившиеся карты, но ваша коллекция не может быть меньше 12-ти карт, помните это когда будете удалять или менять карты.
"""
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), './Global', 'first_Start_menu.py')),
                      'w') as file:
                file.write('False')
            QtWidgets.QMessageBox.information(self, 'Приветсвие', 'Добро пожаловать в Beauty collection!')
            QtWidgets.QMessageBox.information(self, 'Первый запуск', first_start_massage)
            QtWidgets.QMessageBox.information(self, 'Первая инструкция', first_instruction)
            self.stack_dict["Box"][0].open_boxes(2)
            self.stack.setCurrentWidget(self.stack_dict["Box"][1])




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stack_Widgets = Stack_Widgets()
    stack_Widgets.showFullScreen()
    sys.exit(app.exec_())