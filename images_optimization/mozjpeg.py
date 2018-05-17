from images_optimization.execute import execute

binary = 'cjpeg'


def check_binary():
    execute('%s -version' % binary);
