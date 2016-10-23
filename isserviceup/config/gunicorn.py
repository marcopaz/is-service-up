# -*- coding: utf-8 -*-
from multiprocessing import cpu_count


def max_workers():
    return cpu_count()


bind = '0.0.0.0:8000'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" in %(D)sµs'

max_requests = 1000
worker_class = 'eventlet'

workers = max_workers()
