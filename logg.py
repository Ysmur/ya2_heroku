import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='example.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s'
                    )


def log():

    logging.debug('Debug')
    logging.info('Info')
    logging.warning('Warning')
    logging.error('Error')
    logging.critical('Critical or Fatal')


if __name__ == '__main__':
    log()
