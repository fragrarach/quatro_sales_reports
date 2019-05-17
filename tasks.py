import quatro
from files import run_ninja, delete_pdfs


# Checks inc tables for records added today, writes a snapshot of the record, starts timer for next snapshot
def scheduler_task(config):
    for salesman in config.SALESMEN:
        delete_pdfs()
        report_pdf = run_ninja(salesman)
        quatro.send_email('Weekly Sales Report', [salesman['email']], ['mark.s@quatroair.com'], [report_pdf])
