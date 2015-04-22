accept-license:
  cmd.run:
    - name: "echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections"
    - require_in:
      - pkg: "oracle-java8-installer"

oracle-java8-installer:
  pkgrepo.managed:
    - ppa: webupd8team/java
    - dist: trusty
    - name: 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main '
    - file: /etc/apt/sources.list.d/java.list
    - keyserver: keyserver.ubuntu.com
    - keyid: EEA14886
    - require_in:
      - pkg: "oracle-java8-installer"
  pkg.installed:
    - refresh: True