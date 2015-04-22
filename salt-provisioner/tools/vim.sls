curl:
  pkg:
    - installed

vim:
  pkg:
    - installed
  cmd.run:
    - name: 'curl http://j.mp/spf13-vim3 -L -o - | sh'
    - user: vagrant
    - creates: /home/vagrant/.spf13-vim-3/.vimrc
    - require:
      - pkg: vim
      - pkg: curl
    - require_in:
      - file: vim-config-replace


vim-config-replace:
  file.replace:
    - pattern: dark
    - name: "/home/vagrant/.spf13-vim-3/.vimrc"
    - repl: light