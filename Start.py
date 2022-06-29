import subprocess
from Global.variables import *
from Help_Fn.functions import *



with open(path_first_start_chek, 'r') as file:
    first_start = file.read()

if first_start == 'True':
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'Global', 'first_start.py')), 'w') as file:
        file.write('None')
    subprocess.call(('python', path_first_start_menu))
    subprocess.call(('python', path_tutorial_1))

subprocess.call(('python', path_box, '2'))

subprocess.call(('python', path_global_menu))