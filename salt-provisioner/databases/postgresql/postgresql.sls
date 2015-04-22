{% set pkgs = [
  'postgresql',
  'postgresql-contrib',
  'phppgadmin',
] %}

{% for pkg in pkgs %}
{{ pkg }}:
  pkg.installed:
    - refresh: False
{% endfor %}

phppgadmin_permissions:
  cmd.run:
    - name: "sed -i 's/^#allow /allow /'  /etc/apache2/conf.d/phppgadmin; /etc/init.d/apache2 restart; touch /etc/apache2/conf.d/phppgadmin_mod"
    - creates: /etc/apache2/conf.d/phppgadmin_mod
    - user: root
    - require:
      - pkg: phppgadmin
