import psycopg2 as pc2
from config import config

try:
    connection = pc2.connect(
        user=config.database_user.get_secret_value(),
        password=config.database_password.get_secret_value(),
        host=config.database_host.get_secret_value(),
        port=config.database_port.get_secret_value()
    )
    cursor = connection.cursor()
except (Exception, pc2.Error):
    print("Error when working with postgres", pc2.Error)
