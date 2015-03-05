stage { 'first': before => Stage["main"] }
class { 'apt-update': stage => 'first' }

class system {
  include apt-update

  include java
  include vim
}
