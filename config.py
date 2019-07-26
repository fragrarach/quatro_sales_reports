from os.path import dirname, abspath
import calendar


class Config:
    def __init__(self, main_file_path):
        self.main_file_path = main_file_path
        self.parent_dir = dirname(abspath(main_file_path))

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
        # {
        #     'name': 'friday afternoon',
        #     'weekday': calendar.FRIDAY,
        #     'hour': 16,
        #     'minute': 50
        # }
        {
            'name': 'friday afternoon',
            'weekday': calendar.FRIDAY,
            'hour': 10,
            'minute': 56
        }
    ]
