import os
from subprocess import Popen


HADOOP_HOME = os.environ['HADOOP_HOME']
hadoop_jar_file = (
    HADOOP_HOME + 
    "/share/hadoop/tools/lib/hadoop-streaming-2.3.0-cdh5.0.2.jar") # instead of "hadoop-streaming*.jar"
                  

def map_reduce(name, map_file, input, output):
    cmd = (("hadoop jar %s "
            "-D mapred.job.name='%s' "
            "-file %s -mapper '%s' "
            "-input %s -output %s ") % 
           (hadoop_jar_file, 
            name,
            map_file, "python " + map_file,
            input, output))
    print cmd
    Popen(cmd, shell = True).communicate()


if __name__ == "__main__":
    date_str = "2015-11-25"
    map_reduce("product_cat", 
               "product_cat_map.py", 
               "/groups/search/share/search_v3_view/" + date_str,
               "/personal/liuyang/title_search_data/product_cat/" + date_str)
