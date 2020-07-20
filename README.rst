Celery Heartbeat
===

Django app that provides a task that can be run periodically to hit a webhook url of choice to provide basic celery health monitoring.

Configuration
---

Add `celery_heart` to your INSTALLED_APPS setting

    INSTALLED_APPS = [
        ...
        celery_heartbeat,
    ]

Celery-heartbeat comes with a request handler that posts to a configured endpoint and sends a token to authenticate with the receiving server.

    CELERY_HEARTBEAT_ENDPOINT = 'https://example.com/celery-webhook/
    CELERY_HEARTBEAT_TOKEN = '<valid token for endpoint request>'

You will also need to configure the heartbeat task to run periodically using celery-beat:

    CELERY_BEAT_SCHEDULE = {
        'celery-heartbeat': {
            'task': 'celery_heartbeat.tasks.send_heartbeat',
            'schedule': crontab(minute='*/5')
        }
    }
