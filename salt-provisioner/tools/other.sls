{% set pkgs = [
  'python-lxml',
  'zlib1g-dev',
  'unzip',
] %}

{% for pkg in pkgs %}
{{ pkg }}:
  pkg.installed:
    - refresh: False
{% endfor %}