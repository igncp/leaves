NAME="$1"
DATA="$2"
SRC=src/big-data/hadoop

hadoop jar "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper "python $SRC/$NAME/mapper.py" -reducer "python $SRC/$NAME/reduce.py" -input "/data/hdfs-dir/$NAME/$DATA" -output "/data/hdfs-dir/$NAME/output"