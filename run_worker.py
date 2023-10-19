import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities import compose_greeting
from workflows import GreetingWorkflow


async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="hello-activity-task-queue",
        workflows=[GreetingWorkflow],
        activities=[compose_greeting],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
