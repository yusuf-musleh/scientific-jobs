import time
import random


from pyworker.job import Job

RANDOMLY_FAIL_PERCENT = 0.05


class SimpleJob(Job):
    def __init__(self, *args, **kwargs):
        super(SimpleJob, self).__init__(*args, **kwargs)

    def run(self):
        self.logger.info("Running Simple Job...")

        if random.random() < RANDOMLY_FAIL_PERCENT:
            raise Exception("Simple Job failed!")


class LongRunningJob(Job):
    def __init__(self, *args, **kwargs):
        super(LongRunningJob, self).__init__(*args, **kwargs)

    def run(self):
        self.logger.info("Running Long Running Job...")
        time.sleep(3)

        if random.random() < RANDOMLY_FAIL_PERCENT:
            raise Exception("Long Running Job failed!")
