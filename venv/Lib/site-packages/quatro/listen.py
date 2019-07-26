from . import sql
from . import log
from . import configuration


def listen(task, else_task=None):
    log(f'Listening to channel {configuration.config.LISTEN_CHANNEL}')
    while 1:
        try:
            configuration.config.sigm_connection.poll()
        except:
            log('Database cannot be accessed, PostgreSQL service probably rebooting')
            try:
                configuration.config.sigm_connection.close()
                configuration.config.sigm_connection, configuration.config.sigm_db_cursor = \
                    sql.sigm_connect(configuration.config.LISTEN_CHANNEL)
                if configuration.config.log_connection:
                    configuration.config.log_connection.close()
                    configuration.config.log_connection, configuration.config.log_db_cursor = sql.log_connect()
            except:
                pass
            else:
                if else_task:
                    else_task()
        else:
            configuration.config.sigm_connection.commit()
            while configuration.config.sigm_connection.notifies:
                notify = configuration.config.sigm_connection.notifies.pop()
                task(configuration.config, notify)
