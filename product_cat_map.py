import json
import sys


def map():
    for line in sys.stdin:
        try:
            obj = json.loads(line)
            cats = obj["cat_paths"].split('|')
            pid = obj["product_id"]
            for cat in cats:
                print (pid + " " + cat).encode('utf-8') # necessary
        except:
            pass

            
if __name__=="__main__":
    map()
