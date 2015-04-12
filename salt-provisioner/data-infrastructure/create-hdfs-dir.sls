create-hdfs-dir:
  cmd.run:
    - name: 'hdfs dfs -mkdir /data/hdfs-dir'
    - user: 'vagrant'
    - creates: /data/hdfs-dir
    - onlyif: /usr/local/hadoop/bin/hdfs