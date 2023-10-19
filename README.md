## README

### Temporal-Litestar Integration

This project demonstrates an integration between the Temporal Workflow Engine and the [Litestar web framework](https://litestar.dev).
With the help of dependency injection, a Temporal client is provided to the Litestar application to allow executing workflows directly from the web endpoint.

### Files in this project:

1. **`workflows.py`**:

   Defines the Temporal workflow that gets executed. It relies on activities defined in `activities.py` and makes use of the `compose_greeting` activity.

2. **`run_worker.py`**:

   Initiates a Temporal worker that listens to the task queue and executes the corresponding workflow and activity tasks as they are scheduled. This script needs to be running for workflows to be processed.

3. **`activities.py`**:

   Contains the definitions of activities that can be executed as part of a workflow. In this case, there's a single activity `compose_greeting` that generates a greeting message.

4. **`app.py`** (from your original code):

   Defines the Litestar web application and integrates with the Temporal client. The endpoint at "/" triggers the Temporal workflow with the argument "World".

### How to run:

1. Start the Temporal service (assuming you have it set up locally or have access to a Temporal server).

2. Execute the Temporal worker by running:

   ```bash
   python run_worker.py
   ```

   Ensure the worker is running and listening for tasks.

3. Start the Litestar web application:

   ```bash
   litestar run
   ```

4. Navigate to the root endpoint (e.g., `http://localhost:8080/`). This should trigger the Temporal workflow and display the greeting result.

### Requirements:

- Python 3.7+
- Temporal Server (local setup or cloud access)
- Dependencies:
  - `temporalio`
  - `litestar`

### Installation:

To install the required packages, use the following:

```bash
pip install temporalio litestar
```

Ensure that the Temporal server is accessible on `localhost:7233` or adjust the connection parameters as necessary in the code.
