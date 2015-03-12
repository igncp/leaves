rm -rf hdfs-dir/wordcount
hdfs dfs -mkdir hdfs-dir/wordcount

hdfs dfs -copyFromLocal data/gutenberg-book.txt hdfs-dir/wordcount/gutenberg-book.txt

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper "python $PWD/scripts/wordcount/mapper.py" -reducer "python $PWD/scripts/wordcount/reducer.py" -input "hdfs-dir/wordcount/gutenberg-book.txt" -output "hdfs-dir/wordcount/output"