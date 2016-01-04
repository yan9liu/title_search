import os
from subprocess import Popen


HADOOP_HOME = os.environ['HADOOP_HOME']
hadoop_jar_file = (
    HADOOP_HOME + 
    "/share/hadoop/tools/lib/hadoop-streaming-2.3.0-cdh5.0.2.jar") # instead of "hadoop-streaming*.jar"
                  

def map_reduce(name, map_file, reduce_file, input, output):
    cmd = (("hadoop jar %s "
            "-D mapred.job.name='%s' "
            "-file %s -mapper '%s' "
            "-file %s -reducer '%s' "
            "-input %s -output %s ") % 
           (hadoop_jar_file, 
            name,
            map_file, "python " + map_file,
            reduce_file, "python " + reduce_file,
            input, output))
    print cmd
    Popen(cmd, shell = True).communicate()


def map_without_reduce(name, map_file, input, output):
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
    #map_reduce("associate_name_with_cat", 
    #           "associate_name_with_cat_map.py",
    #           "associate_name_with_cat_reduce.py", 
    #           "/personal/liuyang/title_search_data/product_cat/2015-12-24 /personal/liuyang/title_search_data/token_mi",
    #           "/personal/liuyang/title_search_data/product_name_with_cat")
    map_without_reduce("associate_name_with_cat_sort", 
                       "associate_name_with_cat_sort_map.py",
                       "/personal/liuyang/title_search_data/product_name_with_cat",
                       "/personal/liuyang/title_search_data/product_name_with_cat_sort")