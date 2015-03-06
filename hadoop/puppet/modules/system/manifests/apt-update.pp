class system::apt-update {
  file { "/etc/apt/sources.list.d/packages.list":
    source => "puppet:///modules/system/packages.list"
  }
  file { '/etc/apt/apt.conf.d/99auth': # Fix unauthenticated repo intalls (e.g. nodejs)
   owner     => root,
   group     => root,
   content   => "APT::Get::AllowUnauthenticated yes;",
   mode      => 644
  }
  exec {'update':
    command => "apt-get autoremove; apt-get clean; apt-get update",
    require => File['/etc/apt/sources.list.d/packages.list']
  }
}