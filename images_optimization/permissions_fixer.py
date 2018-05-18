import os
import shutil


def fix_permissions(filename):
    shutil.chown(filename, 'www-data', 'www-data')
    os.chmod(filename, 0o644)
