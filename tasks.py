import quatro
from files import run_ninja, delete_pdfs
import data


# Checks inc tables for records added today, writes a snapshot of the record, starts timer for next snapshot
def scheduler_task(config):
    start_date, end_date = data.get_dates()
    for salesman in config.SALESMEN:
        delete_pdfs(config)
        report_pdf = run_ninja(config, start_date, end_date, salesman)
        quatro.send_email('Weekly Sales Report', [salesman['email']], ['mark.s@quatroair.com'], [report_pdf])
