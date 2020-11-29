"""
    This file is used to read configurations from a specified location (See value of 'configFilePath' below).
"""

import logging

LOG_LEVEL = 'log_level'
LOG_TO_FILE = 'log_to_file'
LOG_FILE = 'log_file'
LOG_CONF_FILE = 'log_conf_file'
APP_MODE = 'app_mode'
DEPLOY_PORT = 'deploy_port'
DEBUG_PORT = 'debug_port'
DB_HOST = 'database_host'
DB_NAME = 'database_name'
DB_USERNAME = 'database_username'
DB_PASSWORD = 'database_password'
BUCKET_NAME = 'bucket_name'
MAX_PARALLEL_PROCESS = 'max_parallel_process'
DEBUG_FILE_MODE = 'debug_file_mode'
DATA_FOLDER = 'data_folder'
SEQ2SEQ_PATH = 'seq2seq_path'
ALERT_EMAILS = 'alert_emails'
CALLBACK_URL = 'callback_url'
PRIVATE_IP = 'private_ip'
SERVER_CONFIG_FILEPATH = 'server_config_filepath'
configFilePath = '/var/mlocrappdemo/config/config.txt'
config = {}

# Read configuration file
# with open(configFilePath, 'r') as r:
#     for line in r:
#         line= line.strip('\n\r')
#         config[line[:line.find(':')]] = line[line.find(':')+1:]

def get(key):
    """
        This method is used to fetch data corresponding to a key from config file
    :param key: property whose value is to be fetched
    :return: value corresponding to 'key' property
    """
    if key == LOG_LEVEL:
        return getLogLevel()
    else:
        try:
            try:
                return int(config[key])
            except ValueError:
                return config[key]
        except KeyError:
            return 0

def getLogLevel():
    level = config.get(LOG_LEVEL)
    if level == 'DEBUG':
        return logging.DEBUG
    if level == 'INFO':
        return logging.INFO
    if level == 'WARN':
        return logging.WARN
    if level == 'ERROR':
        return logging.ERROR
    if level == 'CRITICAL':
        return logging.CRITICAL

    return logging.DEBUG #default
