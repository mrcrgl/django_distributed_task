Usage
=====

The default call scheme is:
    Task.delay -> Broker -> Worker -> Execution


Tasks
-----

distributed_task will check in every installed app (``INSTALLED_APPS``) for a ``tasks.py`` file.

Define your first task
----------------------

Create a ``tasks.py`` file in your desired app of choice::

    from distributed_task import register_task

    @register_task
    def my_heavy_task_method():
        pass


Call your task
--------------

The decorator adds a ``delay`` method to your task. You can decide in runtime if you'd like to
execute the task delayed or immediately.

Execute delayed in a worker process::

    my_heavy_task_method.delay(*args, **kwargs)


Default method execution (bypasses task distribution)::

    my_heavy_task_method(*args, **kwargs)


Arguments
---------

You can pass all args/kwargs to the ``my_heavy_task_method.delay`` method as you would call it normally.
The serializer is also able to handle Django model instances but not QuerySets.

This works fine::

    instance = User.objects.first()

    my_heavy_task_method.delay('arg 1', user=instance, some_other_arg=False, some_float=12.5212)

Response / Return values
------------------------

Method return values are not available. Maybe in a further version.

Start the worker
----------------

Finally, you need to start the worker process::
    python manage.py run_worker