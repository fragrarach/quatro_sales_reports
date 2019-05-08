from os.path import dirname, abspath
import calendar

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

    TASK_SCHEDULE = [
        {
            'name': 'monday afternoon',
            'weekday': calendar.MONDAY,
            'hour': 17,
            'minute': 0
        },
        {
            'name': 'tuesday afternoon',
            'weekday': calendar.TUESDAY,
            'hour': 17,
            'minute': 0
        },
        {
            'name': 'wednesday afternoon',
            'weekday': calendar.WEDNESDAY,
            'hour': 15,
            'minute': 0
        },
        {
            'name': 'thursday afternoon',
            'weekday': calendar.THURSDAY,
            'hour': 15,
            'minute': 0
        },
        {
            'name': 'friday afternoon',
            'weekday': calendar.FRIDAY,
            'hour': 17,
            'minute': 0
        }
    ]
