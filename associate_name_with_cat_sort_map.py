import sys


def map():
    for line in sys.stdin:
        a = line.strip().split('\t', 2)
        print a[1] + '\t' + a[0] + '\t' + a[2]

if __name__=="__main__":
    map()        
