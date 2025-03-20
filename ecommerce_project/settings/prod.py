import dj_database_url

from ecommerce_project.settings.common import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}
