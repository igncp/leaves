stage { 'first': before => Stage["main"] }
class { 'apt-update': stage => 'first' }

class system {
  include apt-update

  include nodejs
  include java
  include vim
}
