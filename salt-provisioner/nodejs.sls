nodejs:
  pkgrepo.managed:
    - ppa: chris-lea/node.js
    - dist: trusty
    - name: deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu trusty main 
    - file: /etc/apt/sources.list.d/nodejs.list
    - keyserver: keyserver.ubuntu.com
    - keyid: C7917B12
    - require_in:
      - pkg: nodejs
  pkg.installed:
    - refresh: True