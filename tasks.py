import datetime
import calendar
from threading import Timer
from config import Config
from files import run_ninja, delete_pdfs
from emails import send_email


# Start snapshot timer, optionally delay by 24 hours (for every snapshot subsequent to the first)
def start_timer():
    secs = set_timer()
    snap_timer = Timer(secs, task)
    snap_timer.start()


def schedule_handler(now):
    then = now
    for schedule in Config.TASK_SCHEDULE:
        if 'weekday' in schedule.keys():
            if now.weekday() == schedule['weekday']:
                if now.hour < schedule['hour'] or (now.hour == schedule['hour'] and now.minute < schedule['minute']):
                    minute = schedule['minute']
                    hour = schedule['hour']
                    day = then.day
                    month = then.month
                    year = then.year
                    print(f"Scheduling task for this {schedule['name']}")
                    return minute, hour, day, month, year
            elif now.weekday() < schedule['weekday']:
                while then.weekday() != schedule['weekday']:
                    then += datetime.timedelta(days=1)
                minute = schedule['minute']
                hour = schedule['hour']
                day = then.day
                month = then.month
                year = then.year
                print(f"Scheduling task for this {schedule['name']}")
                return minute, hour, day, month, year
        else:
            if now.hour < schedule['hour'] or (now.hour == schedule['hour'] and now.minute < schedule['minute']):
                minute = schedule['minute']
                hour = schedule['hour']
                day = now.day
                month = now.month
                year = now.year
                print(f"Scheduling task for this {schedule['name']}")
                return minute, hour, day, month, year

    if 'weekday' in Config.TASK_SCHEDULE[0].keys():
        while then.weekday() != Config.TASK_SCHEDULE[0]['weekday']:
            then += datetime.timedelta(days=1)
    else:
        then = now + datetime.timedelta(days=1)

    minute = Config.TASK_SCHEDULE[0]['minute']
    hour = Config.TASK_SCHEDULE[0]['hour']
    day = then.day
    month = then.month
    year = then.year
    print(f"Scheduling task for next {Config.TASK_SCHEDULE[0]['name']}")
    return minute, hour, day, month, year


# Set snapshot timer delay, optionally delay by 24 hours (for every snapshot subsequent to the first)
def set_timer():
    now = datetime.datetime.today()

    minute, hour, day, month, year = schedule_handler(now)

    then = now.replace(year=year, month=month, day=day, hour=hour, minute=minute, second=0, microsecond=0)

    delta = then - now
    secs = delta.seconds + delta.days * 86400
    hours = round((secs / 60) / 60, 2)
    print(f'Sales reports scheduled for {hours} hours from now.')
    return secs


# Checks inc tables for records added today, writes a snapshot of the record, starts timer for next snapshot
def task():
    for salesman in Config.SALESMEN:
        delete_pdfs()
        report_pdf = run_ninja(salesman)
        send_email('Weekly Sales Report', salesman, [report_pdf])
    start_timer()


if __name__ == "__main__":
    start_timer()
    set_timer()
    task()
