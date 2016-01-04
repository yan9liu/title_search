import sys


def map():
    for line in sys.stdin:
        print line.strip().replace(' ', '\t', 1)


if __name__=="__main__":
    map()        
