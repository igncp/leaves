/data:
  file.directory:
    - user: vagrant
    - group: vagrant
    - mode: 755
    - makedirs: True

{% set data_dirs = [
  'texts',
  'CSVs',
  'jsons',
] %}

{% for dir in data_dirs %}
/data/{{dir}}:
  file.directory:
    - user: vagrant
    - group: vagrant
    - mode: 755
    - makedirs: True
{% endfor %}