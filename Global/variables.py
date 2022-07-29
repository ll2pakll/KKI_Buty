import os
'''Размер окон'''

window_width = 1200
window_height = 1000

'''Пути'''
path_global_variables = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'variables.py'))
path_first_start_menu = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'menus', 'first_start.py'))
path_box = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'menus', 'box.py'))
path_start_menu = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'menus', 'start_menu.py'))
path_collection = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cards', 'collection.pkl'))
path_decks = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cards', 'decks.pkl'))
path_global_collection = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Global_collection'))
path_global_collection_datafaces = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'Global_collection', 'DataFaces'))

'''Чекеры'''
first_start = False

'''Ресурсы'''
box_quantity = 239
