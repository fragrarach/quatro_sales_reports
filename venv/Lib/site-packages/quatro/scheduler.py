from threading import Timer
import datetime
import time


def start_scheduler(config, task):
    secs = set_timer(config)
    if secs > 0:
        extended_task = extend_task(config, task)
        schedule_timer = Timer(secs, extended_task)
        schedule_timer.start()


def schedule_handler(config, now):
    then = now
    for schedule in config.TASK_SCHEDULE:
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

    if 'weekday' in config.TASK_SCHEDULE[0].keys():
        if config.TASK_SCHEDULE[0]['weekday'] == now.weekday():
            then += datetime.timedelta(weeks=1)
        else:
            while then.weekday() != config.TASK_SCHEDULE[0]['weekday']:
                then += datetime.timedelta(days=1)
    else:
        then = now + datetime.timedelta(days=1)

    minute = config.TASK_SCHEDULE[0]['minute']
    hour = config.TASK_SCHEDULE[0]['hour']
    day = then.day
    month = then.month
    year = then.year
    print(f"Scheduling task for next {config.TASK_SCHEDULE[0]['name']}")
    return minute, hour, day, month, year


def set_timer(config):
    now = datetime.datetime.today()

    minute, hour, day, month, year = schedule_handler(config, now)

    then = now.replace(year=year, month=month, day=day, hour=hour, minute=minute, second=0, microsecond=0)

    delta = then - now
    secs = delta.seconds + delta.days * 86400
    hours = round((secs / 60) / 60, 2)
    print(f'Order report scheduled for {hours} hours from now.')
    return secs


def extend_task(config, task):
    def extended_task():
        task(config)
        time.sleep(60)
        start_scheduler(config, task)
    return extended_task
