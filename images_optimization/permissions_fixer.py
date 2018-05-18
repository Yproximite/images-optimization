import shutil


def fix_permissions(filename):
    shutil.chown(filename, 'www-data', 'www-data')
