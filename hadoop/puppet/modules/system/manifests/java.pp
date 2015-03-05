class system::java {
  require apt-update
  
  package { 'oracle-java8-installer':
    ensure => 'latest'
  }
}                                             