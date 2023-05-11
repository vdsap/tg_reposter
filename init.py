from configparser import ConfigParser
from loguru import logger
import sys


def main_config():
    configparser = ConfigParser()
    conf = configparser.read('main-conf.ini')
    if not conf:
        logger.debug('Config file not found, creating one')
        configparser['MAIN'] = {'log_level': 'INFO'}
        configparser['TG_BOT'] = {'token': input('Enter Telegram bot token: ')}
        with open('main-conf.ini', 'w') as configfile:
            configparser.write(configfile)
            configfile.close()
    logger.debug('Config file loaded')
    return configparser


def log():
    logger.remove()
    logger.add(sys.stdout, level=main_config()['MAIN']['log_level'])
    logger.debug('Logger initialized')
    return logger
