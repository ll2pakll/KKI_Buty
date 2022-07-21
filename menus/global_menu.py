import Global.variables as gv
import menus.box
from menus.pyqt_files.global_menu.global_menu import *
from Help_Fn.functions import *
from menus.box import *

class Start_menu(QtWidgets.QMainWindow, Ui_Global_menu):
    def __init__(self, Global_menu, stack=None):
        super(Start_menu, self).__init__()
        self.setupUi(Global_menu)
        self.Global_menu = Global_menu
        # self.Global_menu.showMaximized()
        self.stack = stack
        self.setObjectName('Start_menu')

        """Проверяем запускает ли пользователь игру впервые. Если так то он увидит первоночальные инструкции"""
        self.first_run()

        self.Global_menu = Global_menu
        self.Global_menu.resize(gv.window_width, gv.window_height)

        self.add_function()

    def add_function(self):
        '''связь сигналов'''
        self.Play.clicked.connect(lambda: self.on_click(self.Play.objectName()))
        self.Collection.clicked.connect(self.collection_btn_clicked)

    # инструкции при нажатии
    def collection_btn_clicked(self):
        self.stack.setCurrentIndex(box_index)

    def on_click(self, btn_name):
        if btn_name == "Play":
            pass
        elif btn_name == "Collection":
            subprocess.call(('python', gv.path_global_collection_py))

    def first_run(self):
        with open(gv.path_first_start_chek, 'r') as file:
            first_start = file.read()
        if first_start == 'True':
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
            with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Global', 'first_Start_menu.py')),
                      'w') as file:
                file.write('False')
            QtWidgets.QMessageBox.information(self.Global_menu, 'Приветсвие', 'Добро пожаловать в Beauty collection!')

            QtWidgets.QMessageBox.information(self.Global_menu, 'Первый запуск', first_start_massage)
            QtWidgets.QMessageBox.information(self.Global_menu, 'Первая инструкция', first_instruction)

            # subprocess.call(('python', gv.path_box, '12'))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Start_menu(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())