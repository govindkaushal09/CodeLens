import ssl
import certifi
from celery import Celery
from app.core.config import settings

redis_url = settings.redis_url + "?ssl_cert_reqs=CERT_REQUIRED"

ssl_context = ssl.create_default_context(cafile=certifi.where())

celery_app = Celery(
    "codelens",
    broker=redis_url,
    backend=redis_url,
    include=["app.tasks.pr_tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_track_started=True,
    broker_connection_retry_on_startup=True,
    redis_backend_use_ssl={
        "ssl_cert_reqs": ssl.CERT_REQUIRED,
        "ssl_ca_certs": certifi.where()
    },
    broker_use_ssl={
        "ssl_cert_reqs": ssl.CERT_REQUIRED,
        "ssl_ca_certs": certifi.where()
    }
)