Maybe this would be a nice module:

what to do?
- find nice name (distributed_task)
- define api

Package
- diff broker
- own settings
- unified exceptions

Worker
- multi processing (threading)
- neat (colored) output


API
============

## Internal methods

``produce_message(method, **kwargs)``

``consume_messages(handler)``

## Tasks

Write decorator to change the method like:
-> funky_method.delegate(*args, **kwargs)

Worker should run in daemon and cron mode

`Just be just like a walk in the park`