/development:
  file.directory:
    - user: vagrant
    - group: vagrant
    - mode: 755
    - makedirs: True

/development/data:
  file.directory:
    - user: vagrant
    - group: vagrant
    - mode: 755
    - makedirs: True

/development/scripts:
  file.symlink:
    - target: /vagrant/scripts