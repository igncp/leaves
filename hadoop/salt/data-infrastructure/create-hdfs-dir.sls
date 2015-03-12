create-hdfs-dir:
  cmd.run:
    - name: 'hdfs dfs -mkdir /development/hdfs-dir'
    - user: 'vagrant'
    - creates: /development/hdfs-dir
    - onlyif: /usr/local/hadoop/bin/hdfs