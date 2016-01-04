# coding:utf-8

import codecs
from collections import OrderedDict
import re
import sys

from title_lib import Cutter, normalize


Cutter.init()


def main(title_file):
    reader = codecs.open(title_file, 'r', 'utf-8')
    writer = codecs.open(title_file + ".clean", 'w', 'utf-8')
    cnt = 0
    for line in reader:
        cnt += 1
        if cnt % 100000 == 0:
            print cnt
        try:
            splits = line.strip().split('\t')
            pid = splits[0]
            title = splits[1]
            title_repl = re.subn(u'[\<\(（【\[].*?[\]】）\)\>]', " ", title)[0]
            # use OrderedDict to keep token order
            tokens = OrderedDict.fromkeys(Cutter.cut(normalize(title_repl))).keys()
        except Exception as e:
            print line
            print e
            continue
            
        writer.write(pid)
        for token in tokens:
            writer.write("\t" + token)
        writer.write("\n")
    reader.close()
    writer.close()
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: python clean_title.py title_file"
        sys.exit(1)
    main(sys.argv[1])

