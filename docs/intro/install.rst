Installation
============

To use distributed_task, a `Django <https://www.djangoproject.com/>` installation is required.

Requirements
------------

It's well tested with following versions:

+-----------+---------------+---------------+
| Version   | Python        | Django        |
+-----------+---------------+---------------+
| 1.0       | 2.6, 3.3, 3.4 | 1.5, 1.6, 1.7 |
+-----------+---------------+---------------+

Get the code
------------

django_distributed_task package is available on ``pip``:

.. code-block:: bash

    pip install django_distributed_task


Register app in your Django settings.py
---------------------------------------

After install, register ``distributed_task`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        "distributed_task",
    )

And finally ``sync`` your database:

.. code-block:: bash

    ./manage.py syncdb distributed_task