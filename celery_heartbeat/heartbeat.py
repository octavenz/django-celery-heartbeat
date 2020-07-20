import json

import requests

from celery_heartbeat.utils import get_setting


class HeartbeatRequest(object):

    def __init__(self, endpoint=None):
        self.endpoint = endpoint
        if self.endpoint is None:
            self.endpoint = get_setting('CELERY_HEARTBEAT_ENDPOINT')

    def __call__(self):

        response = requests.post(
            self.endpoint,
            data=json.dumps({
                'token': get_setting('CELERY_HEARTBEAT_TOKEN')
            })
        )

        if not response.ok:
            raise ValueError('Heartbeat returned unexpected response: %s - %s' % (response.status_code, response.content))  # noqa
