import subprocess


def start_program(cmd):
    subprocess.call(cmd)


# Spotify is on PATH
def open_spotify():
    start_program("spotify")



