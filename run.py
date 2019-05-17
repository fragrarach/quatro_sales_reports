import os
from subprocess import call


script_path = os.path.realpath(__file__)
parent_path = os.path.abspath(os.path.join(script_path, os.pardir))
parent_name = parent_path.split("\\")[-1]
app_path = f'{parent_path}\\{parent_name}.py'

venv_path = f'{parent_path}\\venv\\Scripts\\python.exe'

command = f'"{venv_path}" "{app_path}"'

call(command)
