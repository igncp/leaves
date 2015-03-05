class hadoop {
  Exec {
    cwd => '/home/vagrant',
    creates => '/usr/local/hadoop'
  }
  
  exec {'download_hadoop':
    command => 'curl -O http://ftp.cixug.es/apache/hadoop/common/stable/hadoop-2.6.0.tar.gz'
  }

  exec { 'unpack_hadoop_and_move':
    command => 'gunzip hadoop-2.6.0.tar.gz; tar -xvf hadoop-2.6.0.tar; \
    rm hadoop-2.6.0.tar; mv hadoop-2.6.0 /usr/local/hadoop',
    require => Exec['download_hadoop']
  }
}