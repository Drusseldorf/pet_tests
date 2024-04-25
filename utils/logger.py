import logging


class Logger:
    def __init__(self):
        self.set_up()

    def set_up(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def write_log(self, log_type, *args):
        if log_type == 'DEBUG':
            logging.debug(' '.join(map(str, args)))
        elif log_type == 'ERROR':
            logging.error(' '.join(map(str, args)))
        elif log_type == 'INFO':
            logging.info(' '.join(map(str, args)))


logger = Logger()
