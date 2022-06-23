from Help_Fn.functions import *

files = Files()
meta_data = Meta_data()

paths_list = files.get_tree(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Buty_frames')))

for path in paths_list:
    dict = files.get_deep_file(path, -2, -1)
    if dict != 'DataFaces':
        meta = meta_data.read(path)
        meta['name'] = dict
        meta_data.save(path, meta)
