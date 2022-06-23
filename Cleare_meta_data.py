from Help_Fn.functions import *

files = Files()
metadata = Meta_data()

path_tree = files.get_tree(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Buty_frames')))

for path in path_tree:
    metadata.clear(path)

print('done')