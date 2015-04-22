{% set pkgs = [
  'sqlite3',
  'libsqlite3-dev',
] %}

{% for pkg in pkgs %}
{{ pkg }}:
  pkg.installed:
    - refresh: False
{% endfor %}