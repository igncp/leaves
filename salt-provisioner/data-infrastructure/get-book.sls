get-book:
  cmd.run:
    - name: 'curl -O http://www.gutenberg.org/cache/epub/2701/pg2701.txt; mv pg2701.txt /development/data/gutenberg-book.txt'
    - user: vagrant
    - creates: /development/data/gutenberg-book.txt
    - require:
      - file: /development/data
