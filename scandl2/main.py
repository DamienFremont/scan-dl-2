import getopt
import glob
import json
import os
import pathlib
import re
import subprocess
import sys
from datetime import datetime, timezone
from os.path import exists
from subprocess import call


# STATIC **********************************************************************


# PUBLIC **********************************************************************

class Item:
    index = 0

# PRIVATE *********************************************************************

def process():
    print("Start")
    items = []
    print('End')

# FUNCTIONS *********************************************************************

# LOGS *********************************************************************

# UTILS *********************************************************************

# SCRIPT **********************************************************************

def main(argv):
    process()

if __name__ == "__main__":
    main(sys.argv[1:])
