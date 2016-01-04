from itertools import combinations
import sys


def map():
    for line in sys.stdin:
        splits = line.decode('utf-8').strip().split('\t')
        if len(splits) < 2:
            continue
        pid = splits[0]
        for token in splits[1:]:
            print (token + '\t' + pid).encode('utf-8')
        for comb in combinations(sorted(splits[1:]), 2):
            print ('|'.join(comb) + '\t' + pid).encode('utf-8')
       

if __name__=="__main__":
    map()        