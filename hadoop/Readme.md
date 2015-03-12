The provisioner is currently changing from Puppet to Salt.

To try this:

``` shell
$ vagrant up
$ vagrant ssh
$ ./scripts/wordcount/wordcount.sh # in /development
$ less hdfs-dir/wordcount/output/part-00000
```
