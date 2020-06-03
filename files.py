import os
from subprocess import check_output
from quatro import log, configuration as c


def run_ninja(start_date, end_date, salesman):
    ninja = c.config.parent_dir + '\\CrystalReportsNinja.exe'
    report = c.config.parent_dir + '\\files\\crystal reports\\Sales Order Summary.rpt'

    date_stamp = f'{start_date.month}-{start_date.day} to {end_date.month}-{end_date.day}'

    output_dir = c.config.parent_dir + '\\files\\pdf'
    output_name = f'\\Weekly Sales Report ({date_stamp}).pdf'
    output_path = output_dir + output_name
    rep = salesman['name']
    curr = salesman['currency']
    command = f'"{ninja}" -D QuatroAir -U SIGM -F "{report}" -O "{output_path}" ' \
              f'-a "Salesman:{rep}" ' \
              f'-a "Date Range:({start_date}, {end_date})" ' \
              f'-a "Currency:{curr}"'
    log(f'Sending following command to shell : {command} \n')
    check_output(command, shell=True).decode()
    report_pdf = {'file': output_path, 'name': output_name}

    return report_pdf


def delete_pdfs():
    pdf_dir = c.config.parent_dir + '\\files\\pdf'
    for file in os.listdir(pdf_dir):
        file_path = pdf_dir + f'\\{file}'
        os.remove(file_path)
        log(f'Deleted {file_path} \n')
