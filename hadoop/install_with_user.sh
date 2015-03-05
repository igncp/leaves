# Run this script inside the VM with the vagrant user

# This provision file installs Hadoop, and configures a python app.
# It also install additional utilities, like vim spf13.

# Sources:
#   Hortonworks
#   http://www.glennklockwood.com
#   http://www.michael-noll.com

sudo apt-get update
sudo apt-get -y install curl build-essential python-software-properties git
sudo apt-get -y install vim tmux ipython
sudo add-apt-repository -y ppa:chris-lea/node.js
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
sudo apt-get update
sudo apt-get install -y oracle-java8-installer

cd /etc/apt/sources.list.d
sudo curl -O http://public-repo-1.hortonworks.com/ambari/ubuntu12/1.x/updates/1.7.0/ambari.list
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD
sudo apt-get update; sudo apt-get install -y ambari-server

cd /development
curl -O http://ftp.cixug.es/apache/pig/pig-0.14.0/pig-0.14.0-src.tar.gz
gunzip pig-0.14.0-src.tar.gz; tar -xvf pig-0.14.0-src.tar; rm pig-0.14.0-src.tar; sudo mv pig-0.14.0-src /usr/local/pig

cp /vagrant/.bashrc ~/
. ~/.bashrc

curl -O http://www.gutenberg.org/cache/epub/2701/pg2701.txt
mkdir /development/data
mv pg2701.txt /development/data

cd /development
hdfs dfs -mkdir wordcount
hdfs dfs -copyFromLocal data/pg2701.txt wordcount/mobydick.txt