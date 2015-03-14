This part of the project tries several technologies related with big data. To try it, you require Vagrant. It is provisioned with Salt, which should setup all the environment (with some exceptions, like Apache Ambari, which need manual setup) and then you can run the scripts located in the `scripts` directory:

``` shell
$ vagrant up
$ vagrant ssh
```

And a Hadoop script:

```
$ ./scripts/wordcount/wordcount.sh # in /development
$ less hdfs-dir/wordcount/output/part-00000
```