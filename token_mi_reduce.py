import math
import sys


N = 17456754


def reduce():
    df_dict = {}
    pre_pid = None
    for line in sys.stdin:
        splits = line.decode('utf-8').strip().split('\t')
        pid = splits[0]
        splits2 = splits[1].split(':')
        k = splits2[0]
        if '|' in k:
            k = tuple(k.split('|'))
        df = int(splits2[1])

        if pid != pre_pid:
            if df_dict:
                output(pre_pid, df_dict)
                df_dict = {}
            pre_pid = pid
        df_dict[k] = df
    if df_dict:
        output(pre_pid, df_dict)


def output(pid, df_dict):
    tokens, combs = divide_by_key(df_dict)
    out_s = pid
    if len(tokens) == 1:
        idf = math.log(float(N) / df_dict[tokens[0]] + 1, 2) # idf
        out_s += ' %s:%g' % (tokens[0], idf)
    else:
        comb_mis = [(comb, mutual_information(comb, df_dict)) for comb in combs]
        token_mi_list = []
        total = 0.0
        for token in tokens:
            token_mi = sum([mi for comb, mi in comb_mis if token in comb])
            token_mi /= len(tokens) - 1
            token_mi_list.append(token_mi)
            total += token_mi
        head_total = 0.0
        for token, mi in sorted(zip(tokens, token_mi_list),
                                key=lambda tm:tm[1],
                                reverse=True):
            out_s += ' %s:%g' % (token, mi)
            head_total += mi
            if head_total / total > 0.8: # set shreshold to 0.9999 to output all tokens
                break
    print out_s.encode('utf-8')


def divide_by_key(df_dict):
    combs = []
    tokens = []
    for k in df_dict:
        if type(k) is tuple:
            combs.append(k)
        else:
            tokens.append(k)
    return tokens, combs


def mutual_information(comb, df_dict):
    ret = float(N) * df_dict.get(comb, 1)
    for token in comb:
        ret /= df_dict.get(token, 1)
    return math.log(ret + 1, 2)        


if __name__=="__main__":
    reduce()                
        