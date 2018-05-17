import subprocess


def execute(command):
    subprocess.run(command, shell=True, check=True)
