class system::nodejs {
  require apt-update
  
  package { 'nodejs':
    ensure => 'latest'
  }
}                                             