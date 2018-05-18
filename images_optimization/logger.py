import logging
from logging.handlers import RotatingFileHandler

import coloredlogs

from images_optimization.config import root_path

logger = logging.getLogger('images_optimization')
formatter = '%(asctime)s - %(levelname)s - %(message)s'

rh = RotatingFileHandler('%s/%s' % (root_path, 'output.log'), maxBytes=1024)
rh.setFormatter(logging.Formatter(formatter))
logger.addHandler(rh)

coloredlogs.install(fmt=formatter)
