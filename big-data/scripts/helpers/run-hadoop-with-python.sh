NAME=$1
DATA=$2

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper "python $PWD/scripts/$NAME/mapper.py" -reducer "python $PWD/scripts/$NAME/reduce.py" -input "hdfs-dir/$NAME/$DATA" -output "hdfs-dir/$NAME/output"