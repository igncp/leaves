{% set pkgs = [
  'python-lxml',
  'zlib1g-dev',
  'tmux',
  'xclip',
  'unzip',
] %}

{% for pkg in pkgs %}
{{ pkg }}:
  pkg.installed:
    - refresh: False
{% endfor %}