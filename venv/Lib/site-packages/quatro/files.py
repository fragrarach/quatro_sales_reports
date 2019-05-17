import os
import __main__


# Check whether app should reference dev or prod server/db
def dev_check():
    raw_filename = os.path.basename(__main__.__file__)
    removed_extension = raw_filename.split('.')[0]
    last_word = removed_extension.split('_')[-1]
    if last_word == 'dev':
        return True
    else:
        return False


# Return containing folder path
def get_parent():
    script_path = os.path.realpath(__main__.__file__)
    parent_path = os.path.abspath(os.path.join(script_path, os.pardir))
    return parent_path


# Check for and add SQL files for main file
def add_sql_files(config):
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
                            config.sigm_db_cursor.execute(sql_file.read())
                        elif folder == log_folder:
                            config.log_db_cursor.execute(sql_file.read())
                        print(f'{file} added.')


if __name__ == "__main__":
    dev_check()
    get_parent()
