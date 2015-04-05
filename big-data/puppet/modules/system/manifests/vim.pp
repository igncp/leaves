class system::vim {
  require apt-update
  
  package { 'curl': ensure  => 'installed' }
  package { 'vim': ensure  => 'installed' }
  package { 'tmux': ensure  => 'installed' }

  exec { 'vim':
    command => 'curl http://j.mp/spf13-vim3 -L -o - | sh',
    cwd => '/home/vagrant',
    user => 'vagrant',
    environment => 'HOME=/home/vagrant',
    require => Package['vim'],
    creates => '/home/vagrant/.spf13-vim-3',
    logoutput => true
  }
}