/home/vagrant/.bashrc:
  file.managed:
    - source: salt://bashrc/.bashrc
    - user: vagrant
    - group: vagrant
    - mode: 644