import subprocess
import os
import pickle
from Global.variables import *



with open(path_first_start_chek, 'r') as file:
    first_start = file.read()

if first_start == 'None':
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'Global', 'first_start.py')), 'w') as file:
        file.write('None')
    subprocess.call(('python', path_first_start_menu))
    subprocess.call(('python', path_tutorial_1))
    if not os.path.isfile(path_collection):
        collection = dict()
        with open(path_collection, 'wb') as f:
            pickle.dump(collection, f)
    subprocess.call(('python', path_box))

subprocess.call(('python', path_global_menu))