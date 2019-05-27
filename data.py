import datetime


def get_dates():
    if datetime.date.today().weekday() == 4:
        end_date = datetime.date.today()
    else:
        end_date = datetime.date.today() - datetime.timedelta(weeks=1)
        while end_date.weekday() != 4:
            end_date += datetime.timedelta(days=1)

    date_delta = datetime.timedelta(days=5)
    start_date = end_date - date_delta
    return start_date, end_date


if __name__ == "__main__":
    get_dates()
