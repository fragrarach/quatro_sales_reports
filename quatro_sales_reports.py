import quatro
import config
from tasks import scheduler_task


def main():
    sales_report_config = config.Config()
    quatro.start_scheduler(sales_report_config, scheduler_task)


if __name__ == "__main__":
    main()
