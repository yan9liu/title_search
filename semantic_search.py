# coding:utf-8

import codecs
from gensim import corpora, models, similarities


def doc_iterator(file_name):
    for line in codecs.open(file_name, 'r', 'utf-8'):
        splits = line.strip().split('\t')[2].split()
        yield [s.split(':')[0] for s in splits]


file_name = r'C:\Users\ocean\Desktop\gensim\product_name_20150401.clean.token_mi_ratio0.8_cat'
dictionary = corpora.Dictionary(doc_iterator(file_name))
print dictionary


def bow_iterator(file_name):
    for tokens in doc_iterator(file_name):
        yield dictionary.doc2bow(tokens)


tfidf = models.TfidfModel(bow_iterator(file_name), id2word=dictionary)
print tfidf
tfidf_iterator = tfidf[bow_iterator(file_name)]


#model = models.LdaModel(list(bow_iterator(file_name)), id2word=dictionary, num_topics=100) # lda is not iterative, why?
model = models.LsiModel(tfidf_iterator, id2word=dictionary, num_topics=500) 
print model
index = similarities.Similarity(r'C:\Users\ocean\Desktop\tmp', model[bow_iterator(file_name)], num_features=500)
print index


#test_bow = list(bow_iterator(file_name))[0]
sims = index[model[tfidf[dictionary.doc2bow([u'搜索引擎优化'])]]] # !!!!!!!!!!
sims = sorted(enumerate(sims), key=lambda item: -item[1])
docs = list(doc_iterator(file_name))
for i, sim in sims[:100]:
    for token in docs[i]:
        print token.encode('utf-8'),
    print 
    print
