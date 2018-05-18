import logging

import coloredlogs

from images_optimization.config import root_path

logger = logging.getLogger('images_optimization')

fh = logging.FileHandler('%s/%s' % (root_path, 'output.log'))
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(fh)

coloredlogs.install()
