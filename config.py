from os.path import dirname, abspath
import calendar
from quatro import dev_check


class Config:
    PARENT_DIR = dirname(abspath(__file__))

    SALESMEN = [
        {
            'name': 'Christopher Fraser',
            'rep_no': 11,
            'currency': 'Canadian Dollar',
            'email': 'christopher.f@quatroair.com'
        },
        {
            'name': 'Mark Castanheiro',
            'rep_no': 200,
            'currency': 'Canadian Dollar',
            'email': 'mark.c@quatroair.com'
        },
        {
            'name': 'Vince Parlavechio',
            'rep_no': 19,
            'currency': 'US Dollar',
            'email': 'vin.par@verizon.net'
        }
    ]

    if not dev_check():
        TASK_SCHEDULE = [
            {
                'name': 'friday afternoon',
                'weekday': calendar.FRIDAY,
                'hour': 17,
                'minute': 0
            }
        ]
    else:
        TASK_SCHEDULE = [
            {
                'name': 'friday afternoon',
                'weekday': calendar.MONDAY,
                'hour': 10,
                'minute': 47
            }
        ]
