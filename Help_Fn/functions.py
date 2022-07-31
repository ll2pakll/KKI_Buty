import DFLIMG
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
import Global.variables as gv

import os
import sys
import random
import pickle
import subprocess

# Считывание, запись и удаление метаданных
class Meta_data:
    def __init__(self):

        self.default_meta = {
                     'identifier': 0,
                     'name': 0,
                     'sex': "w",
                     "scores": 0,
                     "history_comparison": set()
                     }

    def read(self, path):
        self.__path(path)
        dflimg = DFLIMG.DFLJPG.load(self.path)
        try:
            meta = dflimg.get_dict()
            meta["history_comparison"]
            print(f'metadata from {self.name} read: ', meta)
            return meta
        except:
            print(f'{self.name} have no metadata')
            return self.default_meta

    def save(self, path, meta):
        self.__path(path)
        dflimg = DFLIMG.DFLJPG.load(self.path)
        dflimg.set_dict(dict_data=meta)
        dflimg.save()
        print('Meta_data save ', self.name, meta)

    def clear(self, path):
        dflimg = DFLIMG.DFLJPG.load(path)
        dflimg.set_dict(dict_data=self.default_meta)
        dflimg.save()

    def delete(self, path):
        dflimg = DFLIMG.DFLJPG.load(path)
        dflimg.set_dict(dict_data={})
        dflimg.save()

    #создание пути и имени файла
    def __path(self, path):
        self.path = path
        self.name = os.path.basename(self.path)

# Составление древа файлов
class Files:
    # path - путь к папке из которой нужно получить древо
    # extention - расширение подавать в виде списка
    def get_tree(self, path, extension=None):
        filelist = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if extension:
                    for i in extension:
                        if (file.endswith('.' + i)):
                            filelist.append(os.path.join(root, file))
                else:
                    filelist.append(os.path.join(root, file))
        return filelist

    #можно получить часть пути на любую глбину, начиная с названия файла
    def get_deep_file(self, path, deep, deep_2 = None):
        path = path.split('\\')[deep: deep_2]
        return os.path.join(*path)

    def open_player_collection(self, sort=False):
        """если нет файла с коллекцией игрока, он создаётся"""
        if not os.path.isfile(gv.path_collection):
            pickle_save(dict(), gv.path_collection)

        '''открываем коллекцию и сортируем её по имени'''
        with open(gv.path_collection, 'rb') as f:
            collection = pickle.load(f)
        if not sort:
            return collection

        collection_list = list()
        for k, i in collection.items():
            collection_list.append(k)
        return sorted(collection_list)

    def open_player_decks(self):
        """если нет файла с колодами игрока, он создаётся"""
        if not os.path.isfile(gv.path_decks):
            pickle_save(dict(), gv.path_decks)

        """открываем файл с колодами"""
        with open(gv.path_decks, 'rb') as f:
            return pickle.load(f)




class Path_generator:
    '''Генератор путей, который ищет пару для фото которые ещё не сравнивались'''
    def __init__(self, paths_list):
        self.files = Files()
        self.metadata = Meta_data()
        self.paths_list = paths_list
        self.len_paths_list = len(self.paths_list)

    def recurs_rand(self):
        path = random.choice(self.paths_list)
        meta = self.metadata.read(path)
        if len(meta["history_comparison"]) < self.len_paths_list:
            return path, meta
        else:
            self.paths_list.remove(path)
            return self.recurs_rand()

    def get_paths(self):
        path_1, meta_1 = self.recurs_rand()
        path_2, meta_2 = self.recurs_rand()
        if path_1 != path_2 \
        and self.files.get_deep_file(path_1, -2) not in meta_2['history_comparison'] \
        and self.files.get_deep_file(path_1, -2, -1) != meta_2['name']:
            return path_1, path_2, meta_1, meta_2
        else:
            return self.get_paths()


    def get_path(self, own_path, meta, path_list):
        # own_path - путь файла, которому надо подобрать пару
        # meta - метаданные этого файла
        # path_list - список файлов из которых надо подобрать пару
        for path in path_list:
            if own_path != path:
                if self.files.get_deep_file(path, -2) not in meta['history_comparison']:
                    if self.files.get_deep_file(path, -2, -1) != meta['name']:
                        return path

def pickle_save(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


class Card:
    """Класс экземпляры которого будут являться картами и будут хранится в
    качестве метаданных изображений. Тут реализованы методы которые дают возможность
    получить информацию о свойствах карты, дают возможность перемещять её на лейауты
    и так далее"""
    def __init__(self, path=None, obgect_name='Card', size=None):
        """в эту переменную передаём путь к изображению"""
        self.path = path

        '''задаём отображаемый размер изображений'''
        if size:
            self.img_size = size
        else:
            self.img_size = QDesktopWidget().width() // 10

        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName(obgect_name)
        self.pushButton.setSizePolicy(self.sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(self.img_size, self.img_size))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.path).scaled(self.img_size, self.img_size),
                            QtGui.QIcon.Normal,
                            QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(self.img_size, self.img_size))

    def set_layout(self, layout, greed=None, place=None):
        """функция помещает карту на нужный Layout. Первым аргументом передаётся
        сам Layout, вторым вторм аргументом надо передавать True если мы хотим поместить
        карту на сетку, третим место куда хотим поместить в виде картежа"""

        if greed:
            layout.addWidget(self.pushButton, *place)

        else:
            layout.addWidget(self.pushButton)

    def get_path(self):
        return self.path

    def get_pushButton(self):
        return self.pushButton

    def get_obgect_name(self):
        return self.pushButton.objectName()




