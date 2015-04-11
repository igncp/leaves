{% set pip2_modules = [
  'csvkit',
  'pymongo',
  'pyyaml',
  'requests_oauthlib',
  'sqlalchemy',
  'termcolor',
  'mrjob',
  'rednose',
  'seaborn',
] %}

{% for module in pip2_modules %}
pip-{{ module }}:
  pip.installed:
    - name: {{ module }}
    - require:
      - pkg: python-pip
      - pkg: python-dev
{% endfor %}