import logging

import coloredlogs

from images_optimization.config import root_path

logger = logging.getLogger('images_optimization')
formatter = '%(asctime)s - %(levelname)s - %(message)s';

fh = logging.FileHandler('%s/%s' % (root_path, 'output.log'))
fh.setFormatter(logging.Formatter(formatter))
logger.addHandler(fh)

coloredlogs.install(fmt=formatter)
