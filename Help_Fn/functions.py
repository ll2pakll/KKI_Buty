import DFLIMG
import cv2

import os
import sys
import random
import pickle

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
            print(1)
            return path_1, path_2, meta_1, meta_2
        else:
            print(2)
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

