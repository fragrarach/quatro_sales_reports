import os
from subprocess import check_output


def run_ninja(config, start_date, end_date, salesman):
    ninja = config.PARENT_DIR + '\\CrystalReportsNinja.exe'
    report = config.PARENT_DIR + '\\files\\crystal reports\\Sales Order Summary.rpt'

    date_stamp = f'{start_date.month}-{start_date.day} to {end_date.month}-{end_date.day}'

    output_dir = config.PARENT_DIR + '\\files\\pdf'
    output_name = f'\\Weekly Sales Report ({date_stamp}).pdf'
    output_path = output_dir + output_name
    rep = salesman['rep_no']
    curr = salesman['currency']
    command = f'"{ninja}" -D QuatroAir -U SIGM -F "{report}" -O "{output_path}" ' \
              f'-a "Representative:{rep}" ' \
              f'-a "Date:({start_date}, {end_date})" ' \
              f'-a "Summary Currency:{curr}"'
    print(f'Sending following command to shell : {command} \n')
    check_output(command, shell=True).decode()
    report_pdf = {'file': output_path, 'name': output_name}

    return report_pdf


def delete_pdfs(config):
    pdf_dir = config.PARENT_DIR + '\\files\\pdf'
    for file in os.listdir(pdf_dir):
        file_path = pdf_dir + f'\\{file}'
        os.remove(file_path)
        print(f'Deleted {file_path} \n')
