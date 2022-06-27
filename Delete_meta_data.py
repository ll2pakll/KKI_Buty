from Help_Fn.functions import *
from Global.variables import *

files = Files()
metadata = Meta_data()

path_tree = files.get_tree(path_global_collection)

for path in path_tree:
    metadata.delete(path)

print('done')