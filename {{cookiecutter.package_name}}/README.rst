{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.package_display_name %}={% endfor %}
{{ cookiecutter.package_display_name }}
{% for _ in cookiecutter.package_display_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name }}
    :alt: Python Package

.. image:: https://readthedocs.org/projects/{{ cookiecutter.package_name | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.package_name | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_user_name }}/{{ cookiecutter.package_name }}
    :target: https://github.com/{{ cookiecutter.github_user_name }}/{{ cookiecutter.github_repo_name }}/blob/master/LICENSE
    :alt: License

.. image:: https://github.com/{{ cookiecutter.github_user_name }}/{{ cookiecutter.package_name }}/workflows/CI/badge.svg
    :target: https://github.com/{{ cookiecutter.github_user_name }}/{{ cookiecutter.github_repo_name }}/actions
    :alt: Actions

.. image:: https://img.shields.io/pypi/dd/{{ cookiecutter.package_name }}
    :target: https://pepy.tech/project/{{ cookiecutter.package_name }}

.. image:: https://img.shields.io/github/languages/top/{{ cookiecutter.github_user_name }}/{{ cookiecutter.package_name }}
    :target: https://github.com/{{ cookiecutter.github_user_name }}/{{ cookiecutter.github_repo_name }}
    :alt: Top Language

{%- endif %}


{{ cookiecutter.package_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.package_name | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
