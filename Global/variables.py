import os
'''Размер окон'''

window_width = 1200
window_height = 1000

'''Пути'''
path_first_start_chek = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'first_start.py'))
path_first_start_menu = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'menus', 'first_start.py'))
path_tutorial_1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'menus', 'tutorial', 'tutorial_1.py'))
path_box = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'menus', 'box.py'))
path_global_menu = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'menus', 'global_menu.py'))
path_collection = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'collection', 'collection.pkl'))
path_global_collection = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Global_collection'))
path_global_collection_py = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'menus', 'collection.py'))

'''Индексы меню в стеке виджетов'''
start_menu_index = 0
box_index = 1
