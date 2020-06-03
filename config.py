from os.path import dirname, abspath
import calendar


class Config:
    def __init__(self, main_file_path):
        self.main_file_path = main_file_path
        self.parent_dir = dirname(abspath(main_file_path))

    SALESMEN = [
        {
            'name': 'CHRISTOPHER FRASER',
            'rep_no': 11,
            'currency': 'CAD',
            'email': 'christopher.f@quatroair.com'
        },
        {
            'name': 'MARK CASTANHEIRO',
            'rep_no': 200,
            'currency': 'CAD',
            'email': 'mark.c@quatroair.com'
        },
        {
            'name': 'VINCE PARLAVECHIO',
            'rep_no': 19,
            'currency': 'USD',
            'email': 'vin.par@verizon.net'
        }
    ]

    TASK_SCHEDULE = [
        {
            'name': 'friday afternoon',
            'weekday': calendar.FRIDAY,
            'hour': 16,
            'minute': 50
        }
    ]
