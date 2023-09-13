import os
broker_url = os.getenv('BROKER_URL')

task_queues = {
    'default': {
        'exchange': 'default',
        'exchange_type': 'direct',
        'binding_key': 'default'
    },
    'high_priority': {
        'exchange': 'high_priority',
        'exchange_type': 'direct',
        'binding_key': 'high_priority'
    },
}

task_routes = {
    'app1.tasks.*': {'queue': 'default'},
    'app1.tasks.high_priority_task': {'queue': 'high_priority'},
}

worker_concurrency = os.getenv('WORKER_CONCURRENCY')

