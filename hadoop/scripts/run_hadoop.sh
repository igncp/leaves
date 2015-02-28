rm -rf wordcount/output
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -mapper "python $PWD/scripts/mapper.py" -reducer "python $PWD/scripts/reducer.py" -input "wordcount/mobydick.txt" -output "wordcount/output"
