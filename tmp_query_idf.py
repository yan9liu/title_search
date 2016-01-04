# coding:utf-8


import codecs
import math
import pickle


print 'loading df1...'
N, df1_dict = pickle.load(open('product_name_20150401.clean.df1.dump', 'rb'))
print 'loading index...'
Q, _ = pickle.load(open('query_20150702_all.freq10.seg.idx.dump', 'rb'))

           
def idf(tokens):
    if len(tokens) < 1:
        for token in tokens:
            print token.encode('utf-8'),
        print
        return 0.0
    else:
        ret = 0.0
        for token in tokens:
            ret += math.log(float(N) / df1_dict.get(token, 1) + 1, 2)
        return ret / len(tokens)


print 'idfing ...'
Q_idf = [(i, idf(d['tokens'])) for i, d in enumerate(Q)]
print 'sorting ...'
Q_idf.sort(key=lambda p:p[1])


print 'writing ...'
writer = codecs.open("query_20150702_all.freq10.query.idf", 'w', 'utf-8')
for i, idf_val in Q_idf:
    writer.write("%g\t%s\n" % (idf_val, Q[i]['query']))
writer.close()
