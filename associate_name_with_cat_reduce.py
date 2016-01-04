import sys


def reduce():    
    cats = []
    names = []
    pre_pid = None
    for line in sys.stdin:
        splits = line.decode('utf-8').strip().split('\t', 1)
        pid = splits[0]
        if pid != pre_pid:
            if cats and names:
                output(pre_pid, cats, names)
            cats = []       
            names = []
            pre_pid = pid
        if ':' in splits[1]:
            names.append(splits[1])
        else:
            cats.append(splits[1])
    if cats and names:
        output(pre_pid, cats, names)


def output(pid, cats, names):
    for name in names:
        for cat in cats:
            out_s = pid + "\t" + cat + "\t" + name
            print out_s.encode('utf-8')


if __name__=="__main__":
    reduce()                
        
