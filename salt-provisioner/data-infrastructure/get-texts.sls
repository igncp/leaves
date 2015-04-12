{% set data_texts = [
  {
    'name': 'gutenberg-book',
    'url': 'http://www.gutenberg.org/cache/epub/2701/pg2701.txt',
  },{
    'name': 'metaphorpsum',
    'url': 'http://metaphorpsum.com/paragraphs/20/50',
  }
] %}

{% for text in data_texts %}
get-{{ text.name }}-text:
  cmd.run:
    - name: "curl -o {{text.name}}.txt {{text.url}}"
    - user: vagrant
    - cwd: /data/texts
    - creates: /data/texts/{{text.name}}.txt
    - require:
      - file: /data/texts
{% endfor %}