import Global.variables as gv
from menus.pyqt_files.general_window.DS_general_window import *
from menus.start_menu import Start_menu_widget
from menus.box import Box_widget
from menus.collection import Collection_widget
from menus.playground import Playground_widget
from Help_Fn.functions import *

class General_window_widget(Ui_general_window):
    def __init__(self,  MainWindow):
        super(General_window_widget, self).__init__()
        self.setupUi(MainWindow)

        self.General_window = MainWindow

        self.General_window.setWindowTitle("Beauty collection")

        # создаём словарь с добавленными виджетами
        self.stack_dict_general = {}

        # добовляем виджеты в стек
        self.add_widget(Start_menu_widget)
        self.add_widget(Box_widget)
        self.add_widget(Collection_widget)
        self.add_widget(Playground_widget)

        self.first_run()

        self.add_connects()

    def add_connects(self):
        '''связь сигналов'''
        self.exit_qpb.clicked.connect(self.slt_exit)
        self.start_menu_qpb.clicked.connect(self.slt_set_start_menu)

    def add_widget(self, class_widget):
        """функция принимает класс виджета добавляет окно этого виджета
        в стек вджетов, а так же добавляет ссылки на это окно виджета и экземпляр виджета
        в словарь виджетов, с ключём по названию виджета, где [0] - экземпляр виджета,
        [1] - окно виджета. Для того что бы не было ошибки надо добавить в __init__
        передаваемого виджета 2 дополнительных позиционных аргумента
        "stacked_widget_general=None, stack_dict_general=None" """

        # создаём окно которое будет пропущено через преобразования в виджете
        window = QtWidgets.QMainWindow()
        # создаём экземпляр класса виджета и пропускаем через него окно,
        # а так же посылаем в него глобальный стек окон и словарь виджетов
        widget = class_widget(window, self.stacked_widget_general, self.stack_dict_general)
        # добавляем в словарь ссылку на виджет и окно
        self.stack_dict_general[window.objectName()] = [widget, window]
        # добовляем окнов стек виджетов
        self.stacked_widget_general.addWidget(self.stack_dict_general[window.objectName()][1])

    def first_run(self):
        """Проверяем запускает ли пользователь игру впервые.
            Если так то он увидит первоночальные инструкции"""

        if not gv.first_start:
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
            with open(gv.path_global_variables, 'r', encoding='utf-8') as file:
                variables = file.read().replace('first_start = True', 'first_start = False')

            with open(gv.path_global_variables, 'w', encoding='utf-8') as file:
                file.write(variables)

            QtWidgets.QMessageBox.information(self.General_window, 'Приветсвие', 'Добро пожаловать в Beauty collection!')
            QtWidgets.QMessageBox.information(self.General_window, 'Первый запуск', first_start_massage)
            QtWidgets.QMessageBox.information(self.General_window, 'Первая инструкция', first_instruction)
            self.stack_dict_general["Box"][0].add_boxes(12)
            self.stacked_widget_general.setCurrentWidget(self.stack_dict_general["Box"][1])
        else:
            self.stacked_widget_general.setCurrentWidget(self.stack_dict_general["Start_menu"][1])

    #Слоты
    def slt_exit(self):
        sys.exit()

    def slt_set_start_menu(self):
        self.stacked_widget_general.setCurrentWidget(self.stack_dict_general["Start_menu"][1])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = General_window_widget(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())