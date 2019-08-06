from quatro import send_email, configuration as c
from files import run_ninja, delete_pdfs
import data


# Checks inc tables for records added today, writes a snapshot of the record, starts timer for next snapshot
def scheduler_task():
    start_date, end_date = data.get_dates()
    for salesman in c.config.SALESMEN:
        delete_pdfs()
        report_pdf = run_ninja(start_date, end_date, salesman)
        send_email('Weekly Sales Report', [salesman['email']], ['mark.s@quatroair.com'], [report_pdf])
