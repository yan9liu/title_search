# coding:utf-8

import codecs
from itertools import combinations
import pickle
import sys

 
def df(title_clean_file, token_num=1):
    reader = codecs.open(title_clean_file, 'r', 'utf-8')
    out_file = "%s.df%d.dump" % (title_clean_file, token_num)
    writer = open(out_file, 'wb')
    cnt = 0
    df_dict = {}
    for line in reader:
        cnt += 1
        if cnt % 100000 == 0:
            print cnt
            
        try:
            tokens = line.strip().split('\t')[1:] 
        except Exception as e:
            print line
            print e
            continue
            
        if token_num == 1:
            for token in tokens:
                df_dict[token] = df_dict.get(token, 0) + 1
        elif token_num > 1:            
            tokens.sort()
            for comb in combinations(tokens, token_num):
                df_dict[comb] = df_dict.get(comb, 0) + 1

                
    pickle.dump((cnt, df_dict), writer)
    reader.close()
    writer.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: python title_df.py token_num title_clean_file"
        sys.exit(1)
    df(sys.argv[2], int(sys.argv[1]))
