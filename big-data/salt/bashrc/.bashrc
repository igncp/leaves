alias ls="ls -lah"
alias tmux="tmux -2" # for vim colors
alias rm='rm -rf'

export JAVA_HOME="/usr/lib/jvm/java-8-oracle/"
export HADOOP_HOME="/usr/local/hadoop"
export HADOOP_PREFIX=/usr/local/hadoop
export PATH=/usr/local/hadoop/bin:$PATH
export PATH=/usr/local/pig/bin:$PATH
export PATH=/usr/local/storm/bin:$PATH
export PATH=/usr/local/hive/bin:$PATH
export PIG_HOME="/usr/local/pig/"

PS1='${debian_chroot:+($debian_chroot)}\[\033[01;33m\]\n\u@\h\[\033[00m\]:\[\033[01;34m\] \W\[\033[01;36m\]$(__git_ps1) \[\033[00m\]· '

cd /development