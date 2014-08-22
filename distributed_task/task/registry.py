from __future__ import unicode_literals

from inspect import getmembers, isfunction
from django.utils.module_loading import module_has_submodule
from importlib import import_module
from django.apps import apps
from distributed_task.exceptions import TaskNotRegisteredError
import logging
logger = logging.getLogger(__name__)


TASKS_MODULE_NAME = 'tasks'


class TaskRegistry(object):

    _registry = {}

    def discover(self):
        for app_config in apps.get_app_configs():
            if module_has_submodule(app_config.module, TASKS_MODULE_NAME):
                tasks_module_name = '%s.%s' % (app_config.name, TASKS_MODULE_NAME)
                self._load_tasks_of_module(tasks_module_name)

    def _load_tasks_of_module(self, tasks_module_name):
        module = import_module(tasks_module_name)

        for name, fnc in getmembers(module):
            if isfunction(fnc) and getattr(fnc, '_is_registered_task', False):
                path = "%s.%s" % (tasks_module_name, name)

                self.register(path, fnc)

    def register(self, path, fnc):
        if path in self._registry.keys():
            return

        logger.info("Register task: '%s'", path)
        self._registry[path] = fnc

    def get_task_path(self, task_fnc):
        for path, task in self._registry.iteritems():
            if task == task_fnc:
                return path

        raise TaskNotRegisteredError()