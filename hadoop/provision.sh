sudo apt-get update
sudo apt-get -y install curl build-essential python-software-properties git
sudo apt-get -y install vim tmux
sudo add-apt-repository -y ppa:chris-lea/node.js
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
sudo apt-get update
sudo apt-get install -y oracle-java8-installer
curl http://j.mp/spf13-vim3 -L -o - | sh

echo 'export JAVA_HOME="/usr/lib/jvm/java-8-oracle/"' > ~/.bashrc
echo 'export HADOOP_PREFIX=/usr/local/hadoop' >> ~/.bashrc
echo 'export PATH=/usr/local/hadoop/bin:$PATH' >> ~/.bashrc
echo 'cd /development' >> .bashrc

curl -O http://ftp.cixug.es/apache/hadoop/common/stable/hadoop-2.6.0.tar.gz

gunzip hadoop-2.6.0.tar.gz
tar -xvf hadoop-2.6.0.tar
rm hadoop-2.6.0.tar
sudo mv hadoop-2.6.0 /usr/local/hadoop
sudo mkdir /development
sudo chown vagrant /development/

cd /etc/apt/sources.list.d
sudo curl -O http://public-repo-1.hortonworks.com/ambari/ubuntu12/1.x/updates/1.7.0/ambari.list
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD
sudo apt-get update; sudo apt-get install -y ambari-server