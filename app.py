from litestar import Litestar, get
from litestar.di import Provide
from temporalio.client import Client

from workflows import GreetingWorkflow


async def temporal_client() -> Client:
    """Create a Temporal client."""
    client = await Client.connect("localhost:7233")
    return client


@get("/")
async def hello_world(client: Client) -> str:
    """Run the Temporal workflow and return the result."""
    result = await client.execute_workflow(
        GreetingWorkflow.run,
        "World",
        id="hello-activity-workflow-id",
        task_queue="hello-activity-task-queue",
    )
    return f"Result from Temporal: {result}"


"""
The dependencies dictionary at the Litestar app level associates the name "client" with the provider function temporal_client.
In the route handler hello_world, you can then simply type-hint with Client, and the dependency injection system should automatically provide the Temporal client when hello_world is invoked.
"""
app = Litestar(
    route_handlers=[hello_world], dependencies={"client": Provide(temporal_client)}
)
