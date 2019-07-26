import os
import glob
import datetime
from . import configuration


# Check whether app should reference dev or prod server/db
def dev_check():
    raw_filename = os.path.basename(configuration.config.main_file_path)
    removed_extension = raw_filename.split('.')[0]
    last_word = removed_extension.split('_')[-1]
    if last_word == 'dev':
        return True
    else:
        return False


# Return containing folder path
def get_parent():
    script_path = os.path.realpath(configuration.config.main_file_path)
    parent_path = os.path.abspath(os.path.join(script_path, os.pardir))
    return parent_path


# Check for and add SQL files for main file
def add_sql_files():
    parent_path = get_parent()
    sql_folder = parent_path + '\\files\\sql'
    type_folder = sql_folder + '\\dev' if dev_check() else sql_folder + '\\prod'
    sigm_folder = type_folder + '\\sigm'
    log_folder = type_folder + '\\log'
    sql_folders = [sigm_folder, log_folder]
    for folder in sql_folders:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                if file.endswith(".sql"):
                    file_path = folder + f'\\{file}'
                    with open(file_path, 'r') as sql_file:
                        if folder == sigm_folder:
                            configuration.config.sigm_db_cursor.execute(sql_file.read())
                        elif folder == log_folder:
                            configuration.config.log_db_cursor.execute(sql_file.read())
                        log(f'{file} added.')


def init_app_log_dir():
    parent_path = get_parent()
    if dev_check():
        log_folder = parent_path + '\\files\\log\\dev'
    else:
        log_folder = parent_path + '\\files\\log\\prod'
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)


def get_newest_log(log_folder):
    log_files = glob.glob(log_folder + '\\*')
    if log_files:
        newest_log = max(log_files, key=os.path.getctime)
        return newest_log


def create_app_log_file(log_folder):
    log_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.log'
    open(log_folder + '\\' + log_name, 'x')


def init_app_log_file(message, log_folder):
    if get_newest_log(log_folder):
        newest_log = get_newest_log(log_folder)
        message_size = len(message.encode('utf-8'))
        max_size = 1000000
        file = os.stat(newest_log)
        if file.st_size + message_size > max_size:
            create_app_log_file(log_folder)
    else:
        create_app_log_file(log_folder)


def write_app_log(message, log_folder):
    newest_log = get_newest_log(log_folder)
    with open(newest_log, 'a', encoding='utf-8') as log_file:
        log_file.write('[' + str(datetime.datetime.now()) + '] : ' + message + '\n')


def log(message):
    parent_path = get_parent()
    if dev_check():
        log_folder = parent_path + '\\files\\log\\dev'
    else:
        log_folder = parent_path + '\\files\\log\\prod'
    init_app_log_file(message, log_folder)
    write_app_log(message, log_folder)


if __name__ == "__main__":
    dev_check()
    get_parent()
    init_app_log_dir()
