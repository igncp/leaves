{% set python2_other = [
  'ipython',
  'python-matplotlib',
  'python-mysqldb',
  'python-numpy',
  'python-tk',
  'python-scipy',
] %}

{% for module in python2_other %}
python-other-{{ module }}:
  pkg.installed:
    - name: {{ module }}
    - require:
      - pkg: python-pip
{% endfor %}

# Get a higher version of Pandas
python-pandas:
  pkgrepo.managed:
    - name: 'deb http://ppa.launchpad.net/pythonxy/pythonxy-devel/ubuntu precise main'
    - file: /etc/apt/sources.list.d/pandas.list
    - keyserver: keyserver.ubuntu.com
    - keyid: ADC95410
  pkg.installed:
    - refresh: True