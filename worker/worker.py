import redis
import os
import time


class Worker:
    def __init__(self):
        # Line broken to stay under 79 characters
        self.r = redis.Redis(
            host=os.getenv("REDIS_HOST", "redis"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            decode_responses=True
        )

    def process_jobs(self):
        print("Worker started, waiting for jobs...")
        while True:
            job = self.r.blpop("job", timeout=5)
            if job:
                job_id = job[1]
                print(f"Processing job: {job_id}")
                time.sleep(2)
                self.r.hset(f"job:{job_id}", "status", "completed")
                print(f"Finished job: {job_id}")


if __name__ == "__main__":
    worker = Worker()
    worker.process_jobs()
