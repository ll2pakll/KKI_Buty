import Global.first_start
import subprocess
import os

path_first_start_chek = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'Global', 'first_start.py'))
path_first_start_menu = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'menus', 'first_start.py'))
path_tutorial_1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'menus', 'tutorial', 'tutorial_1.py'))
print(path_tutorial_1)
path_global_menu = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'menus', 'global_menu.py'))

with open(path_first_start_chek, 'r') as file:
    first_start = file.read()

if first_start == 'None':
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'Global', 'first_start.py')), 'w') as file:
        file.write('None')
    subprocess.call(('python', path_first_start_menu))
    subprocess.call(('python', path_tutorial_1))

subprocess.call(('python', path_global_menu))