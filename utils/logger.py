import logging
import sys


class Level:
    DEBUG = 'debug'
    INFO = 'info'
    ERROR = 'error'


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format='\n%(asctime)s - %(levelname)s - %(message)s',
                            stream=sys.stdout)

    @staticmethod
    def write(level, *args):
        try:
            getattr(logging, level)(' '.join(map(str, args)))
        except AttributeError as e:
            logging.error(f'AttributeError: No such logging level as "{level}": {e}')


log = Logger()
