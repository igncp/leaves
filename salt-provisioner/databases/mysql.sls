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

vagrant_mysql_user:
  mysql_user.present:
    - name: vagrant
    - host: localhost
    - password: 'foo'

mysql_leaves_database:
  mysql_database.present:
    - name: leaves

vagrant_mysql_user_privileges:
  mysql_grants.present:
    - grant: all privileges
    - database: leaves.*
    - user: vagrant