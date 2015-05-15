__author__ = 'arthur'

import sys
import os


# checks if the host system is Windows
def is_windows():
    return 'win' in sys.platform or 'nt' in os.name


# checks if the host system is Mac
def is_mac():
    return 'darwin' in sys.platform


# checks if the host system is Linux
def is_unix():
    return 'linux' in sys.platform


# checks if the host system is Solaris
def is_solaris():
    return 'sun' in sys.platform