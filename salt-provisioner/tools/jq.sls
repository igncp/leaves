jq:
  cmd.run:
    - name: 'curl -O http://stedolan.github.io/jq/download/linux64/jq; chmod +x jq; mv jq /usr/bin'
    - user: root
    - creates: /usr/bin/jq
    - require:
      - pkg: curl
