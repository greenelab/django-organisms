=========
Organisms
=========

Organisms is a simple Django app to represent organisms.


Download and Install
---------------------
This package is registered as "django-organisms" in PyPI and is pip
installable:

.. code-block:: shell

	pip install django-organisms


Quick Start
-----------

1. Add "organisms" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'organisms',
    )

2. Run `python manage.py migrate` to create the organisms models.

3. This app includes a management command in `organisms/management/commands/organisms_create_or_update.py`,
   which can be used to populate the organisms table in the database. It takes three arguments:

      * taxonomy_id
      * scientific_name
      * common_name

   For example, to populate the Human object in the database, we would enter::

     python manage.py organisms_create_or_update --taxonomy_id=9606 --scientific_name="Homo sapiens" --common_name="Human"
