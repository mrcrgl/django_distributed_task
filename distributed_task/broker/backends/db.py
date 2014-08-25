# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..interface import BrokerInterface
from distributed_task import settings
from distributed_task.core.serializer import serialize, deserialize
from distributed_task.models import Message
import time


class DatabaseMessageBroker(BrokerInterface):

    queue = 'distributed_task_queue'

    def prepare(self):
        self.load_config()

    def load_config(self):
        OPTIONS = getattr(settings, 'BROKER_OPTIONS')

        self.queue = OPTIONS.get('QUEUE', 'distributed_task_queue')

    def produce_message(self, data):
        m = Message(message=serialize(data), queue=self.queue)
        m.save()

    def consume_message(self, handler):
        while True:
            next = Message.objects.filter(queue=self.queue).order_by('created').first()
            if not next:
                return True

            body = next.message
            next.delete()
            handler(deserialize(body))

    def keep_consuming(self, handler):
        while True:
            self.consume_message(handler)
            time.sleep(10)