{% set apache_tools = [
  {
    'name_short': 'hadoop',
    'name_full': 'hadoop-2.6.0',
    'url': 'http://ftp.cixug.es/apache/hadoop/common/stable/hadoop-2.6.0.tar.gz'
  },{
    'name_short': 'pig',
    'name_full': 'pig-0.14.0',
    'url': 'http://apache.rediris.es/pig/pig-0.14.0/pig-0.14.0.tar.gz'
  },{
    'name_short': 'storm',
    'name_full': 'apache-storm-0.9.3',
    'url': 'http://apache.rediris.es/storm/apache-storm-0.9.3/apache-storm-0.9.3.tar.gz'
  }
] %}

{% for tool in apache_tools %}
{{ tool.name_short }}-download:
  cmd.run:
    - name: "curl -O {{ tool.url }}"
    - creates: "/usr/local/{{ tool.name_short }}"
    - require_in:
      - pkg: {{ tool.name_short }}-unpack-and-move

{{ tool.name_short }}-unpack-and-move:
  cmd.run:
    - name: "gunzip {{ tool.name_full }}.tar.gz; tar -xvf {{ tool.name_full }}.tar; rm {{ tool.name_full }}.tar; mv {{ tool.name_full }} /usr/local/{{ tool.name_short }}"
    - creates: "/usr/local/{{ tool.name_short }}"
{% endfor %}
