class system::apt-update {
  file { "/etc/apt/sources.list.d/packages.list":
    source => "puppet:///modules/system/packages.list"
  }
  exec {'update':
    command => "apt-get update",
    require => File['/etc/apt/sources.list.d/packages.list']
  }
}