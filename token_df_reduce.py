import sys


def reduce():    
    pids = []
    pre_k = None
    for line in sys.stdin:
        splits = line.decode('utf-8').strip().split('\t')
        k = splits[0]
        pid = splits[1]
        if k != pre_k:
            if pids:
                output(pre_k, pids)
                pids = []       
            pre_k = k
        pids.append(pid)
    if pids:
        output(pre_k, pids)


def output(k, pids):
    for pid in pids:
        out_s = "%s\t%s:%d" % (pid, k, len(pids))
        print out_s.encode('utf-8')

        
if __name__=="__main__":
    reduce()                
        