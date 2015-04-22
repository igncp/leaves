{% set pkgs = [
  'mysql-server',
  'mysql-common',
  'mysql-client',
] %}

{% for pkg in pkgs %}
{{ pkg }}:
  pkg.installed:
    - refresh: False
{% endfor %}

vagrant:
  mysql_user.present:
    - host: localhost
    - password: 'foo'