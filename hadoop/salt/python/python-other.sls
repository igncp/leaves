{% set python2_other = [
  'ipython',
  'python-matplotlib',
  'python-mysqldb',
  'python-numpy',
  'python-pandas',
  'python-tk',
] %}

{% for module in python2_other %}
python-other-{{ module }}:
  pkg.installed:
    - name: {{ module }}
    - require:
      - pkg: python-pip
{% endfor %}