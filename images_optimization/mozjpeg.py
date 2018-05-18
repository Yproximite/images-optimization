import shutil
import tempfile

from images_optimization.config import config
from images_optimization.execute import execute

binary = config.get('cjpeg_binary')


def check_binary():
    execute('%s -version' % binary)


def optimize(filename):
    tmpfile = tempfile.NamedTemporaryFile(delete=False)
    execute('%s "%s" > "%s"' % (binary, filename, tmpfile.name))

    shutil.move(tmpfile.name, filename)
