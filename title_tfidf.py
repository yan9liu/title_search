# coding:utf-8

import codecs
import math
from itertools import combinations
import pickle
import re
import sys


print 'loading df1...'
N, df1_dict = pickle.load(open('product_name_20150401.clean.df1.dump', 'rb'))
print 'loading index...'
Q, Q_inverted = pickle.load(open('query_20150702_all.freq10.seg.idx.dump', 'rb'))
print "tfidf ..."
           

def main(title_clean_file):
    reader = codecs.open(title_clean_file, 'r', 'utf-8')
    writer = codecs.open(title_clean_file + ".tfidf", 'w', 'utf-8')

    def output(pid, alist):
        writer.write(pid)
        for k, v in sorted(alist, key=lambda kv:kv[1], reverse=True):
            writer.write(" %s:%g" % (k, v))
        writer.write('\n')
    
    n = 0
    for line in reader:
        n += 1
        if n % 1000 == 0:
            print n
        try:
            splits = line.strip().split('\t')  
            pid = splits[0]
            tokens = splits[1:]
        except Exception as e:
            print line
            print e
            continue

        # get subset query ids
        sid_set = set()
        for token in tokens:
            for sid in Q_inverted.get(token, []):
                if sid not in sid_set:
                    if set(Q[sid]['tokens']).issubset(tokens):
                        sid_set.add(sid)
        
        # accumulate big frequency for every unique token 
        token_dict = {}
        for sid in sid_set:
            for token in Q[sid]['tokens']:
                token_dict[token] = token_dict.get(token, 0) + Q[sid]['freq']
        
        #token_tf_list = []
        #token_idf_list = []
        token_tfidf_list = []
        for token in tokens:
            tf = math.log(token_dict.get(token, 0) + 2, 2)
            idf = math.log(float(N) / df1_dict.get(token, 1) + 1, 2)
            #token_tf_list.append((token, tf))
            #token_idf_list.append((token, idf))
            token_tfidf_list.append((token, tf * idf))
            
        #output(pid, token_tf_list)
        #output(pid, token_idf_list)
        output(pid, token_tfidf_list)
    reader.close()
    writer.close()
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: python tfidf_title.py title_clean_file"
        sys.exit(1)
    main(sys.argv[1])

