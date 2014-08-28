Settings
========

Message Broker
--------------

The default message broker ``distributed_task.broker.backends.dummy.DummyMessageBroker`` does not provide any
functionality.

The only message broker which is tested and available is `RabbitMQ <http://www.rabbitmq.com/>`.

Sample setup for RabbitMQ::

    DISTRIBUTED_TASK_BROKER = {
        'BROKER': 'distributed_task.broker.backends.amqp.AMQPMessageBroker',
        'OPTIONS': {
            # Your connection data for RabbitMQ
            'HOST': 'localhost',
            'USERNAME': 'guest',
            'PASSWORD': 'guest',
            'PORT': 5672,

            # Your desired queue name (need to change it for multiple installations)
            'QUEUE': 'distributed_task_queue',
        }
    }

