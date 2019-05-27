import config
from tasks import scheduler_task


def main():
    sales_report_config = config.Config()
    scheduler_task(sales_report_config)


if __name__ == "__main__":
    main()
