# coding:utf-8

import ctypes


class Cutter:

    @staticmethod
    def init():
        # import segmentor
        Cutter.seg = ctypes.CDLL("libprobseg.so")
        Cutter.seg_init = Cutter.seg.prob_init()
        Cutter.seg_degree = Cutter.seg.set_seg_granul(Cutter.seg_init, True)
    
    @staticmethod
    def cut(s):
        result = ' ' * 1000
        Cutter.seg.prob_seg(Cutter.seg_init, s.encode('gb18030'), result)
        tokens = result.decode('gb18030').strip().strip('\0').split()
        return tokens


def normalize(s):
    ret = []
    for uchar in s:
        if is_chinese(uchar) or is_number(uchar):
            ret.append(uchar)
        elif is_alphabet(uchar):
            ret.append(uchar.lower())
        elif uchar == ' ':
            if len(ret) > 0 and ret[-1] != ' ':
                ret.append(' ')
    return "".join(ret)


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
 

def is_number(uchar):
    if uchar >= u'\u0030' and uchar<=u'\u0039':
        return True
    else:
        return False
 

def is_alphabet(uchar):
    if ((uchar >= u'\u0041' and uchar<=u'\u005a') or 
        (uchar >= u'\u0061' and uchar<=u'\u007a')):
        return True
    else:
        return False
