import os
import logging


from pyworker.worker import Worker

from jobs import SimpleJob, LongRunningJob


def start_pyworker():
    # Configuring DB connection
    PG_USER = os.environ.get("PG_USER", "postgres")
    PG_PASSWORD = os.environ.get("PG_PASSWORD", "postgres")
    PG_HOST = os.environ.get("PG_HOST", "localhost")
    PG_PORT = os.environ.get("PG_PORT", 5432)
    PG_DB_NAME = os.environ.get("PG_DB_NAME", "scientific-jobs-db")
    dbstring = f"postgres://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB_NAME}"

    # Configuring Logger
    logging.basicConfig()
    logger = logging.getLogger('pyworker')
    logger.setLevel(logging.INFO)

    # Initializing the worker and running it
    w = Worker(dbstring, logger)
    w.queue_names = 'simple_jobs,long_running_jobs'
    w.sleep_delay = 0.5

    w.run()


if __name__ == "__main__":
    start_pyworker()
