{% set pip2_modules = [
  'csvkit',
  'discogs_client',
  'lxml',
  'mrjob',
  'nose',
  'pygithub',
  'pymongo',
  'python-linkedin',
  'pyyaml',
  'rednose',
  'requests',
  'requests_oauthlib',
  'seaborn',
  'termcolor',
] %}

{% for module in pip2_modules %}
pip-{{ module }}:
  pip.installed:
    - name: {{ module }}
    - require:
      - pkg: python-pip
      - pkg: python-dev
{% endfor %}