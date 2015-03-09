hadoop-download:
  cmd.run:
    - name: "curl -O http://ftp.cixug.es/apache/hadoop/common/stable/hadoop-2.6.0.tar.gz"
    - creates: '/usr/local/hadoop'
    - require_in:
      - pkg: hadoop-unpack-and-move

hadoop-unpack-and-move:
  cmd.run:
    - name: 'gunzip hadoop-2.6.0.tar.gz; tar -xvf hadoop-2.6.0.tar; rm hadoop-2.6.0.tar; mv hadoop-2.6.0 /usr/local/hadoop'
    - creates: '/usr/local/hadoop'
