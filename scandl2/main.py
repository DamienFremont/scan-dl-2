import sys
from scandl2 import app

def main(argv):
    app.execute(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
