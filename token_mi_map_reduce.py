import os
from subprocess import Popen


HADOOP_HOME = os.environ['HADOOP_HOME']
hadoop_jar_file = (
    HADOOP_HOME + 
    "/share/hadoop/tools/lib/hadoop-streaming-2.3.0-cdh5.0.2.jar") # instead of "hadoop-streaming*.jar"


def map_reduce(name, map_file, reduce_file, input, output):
    cmd = "hadoop fs -rmr " + output
    print cmd
    Popen(cmd, shell = True).communicate()

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


if __name__ == "__main__":
#    map_reduce("token_df", 
#               "token_df_map.py", 
#               "token_df_reduce.py",
#               "/personal/liuyang/title_search_data/product_name_20150401.clean",
#               "/personal/liuyang/title_search_data/token_df")
    map_reduce("token_mi", 
               "token_mi_map.py", 
               "token_mi_reduce.py",
               "/personal/liuyang/title_search_data/token_df",
               "/personal/liuyang/title_search_data/token_mi")
