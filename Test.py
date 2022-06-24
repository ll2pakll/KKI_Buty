from Help_Fn.functions import *


files = Files()

path = files.get_tree('f:\Work area\Buty NN\Buty_frames', ['jpg', 'bat'])

print(files.get_deep_file(path[0], None, 1))