get-comments:
  cmd.run:
    - name: 'curl http://jsonplaceholder.typicode.com/comments > comments.json'
    - user: vagrant
    - cwd: /data/jsons
    - creates: /data/jsons/comments.json
    - require:
      - file: /data/jsons