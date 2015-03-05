class dotfiles {
  File { owner => 'vagrant' }

  file { "/home/vagrant/.bashrc":
      source => "puppet:///modules/dotfiles/.bashrc"
  }
}