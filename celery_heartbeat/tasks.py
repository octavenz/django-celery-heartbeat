from celery import shared_task

from celery_heartbeat.heartbeat import HeartbeatRequest


@shared_task
def send_heartbeat():
    HeartbeatRequest()()
