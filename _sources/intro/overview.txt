Overview
========

In between of `celery <https://github.com/celery/celery>`, distributed_task is extremely lightweight.
We'd decided to keep it simple with less of flexibility but straight at the needs.
Just define for each method a `task`-method using the decorator and delay it at run time.

Use case
--------

The goal is to prevent "heavy" tasks to be executed between a web request and it's response.

Examples for those tasks are:

* Sending e-mails.
* Generation of pdf/csv/... files.
* Rendering of images, videos.