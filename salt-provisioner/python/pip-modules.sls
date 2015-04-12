{% set pip2_modules = [
  'csvkit',
  'mrjob',
  'nose',
  'pygithub',
  'pymongo',
  'pyyaml',
  'rednose',
  'requests',
  'requests_oauthlib',
  'seaborn',
  'termcolor',
  'python-linkedin',
] %}

{% for module in pip2_modules %}
pip-{{ module }}:
  pip.installed:
    - name: {{ module }}
    - require:
      - pkg: python-pip
      - pkg: python-dev
{% endfor %}