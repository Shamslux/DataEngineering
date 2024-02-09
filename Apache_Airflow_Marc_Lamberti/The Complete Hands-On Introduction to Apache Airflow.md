![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)

# Why use Airflow?

Using Apache Airflow can be advantageous for several reasons:

1. **Workflow Automation**: Airflow allows you to automate complex workflows, making it easier to schedule and manage tasks in a systematic manner.

2. **Flexibility**: It provides flexibility in defining workflows using Python code, allowing you to create custom logic and handle various data processing scenarios.

3. **Dependency Management**: Airflow lets you define dependencies between tasks, ensuring that tasks are executed in the correct order.

4. **Monitoring and Logging**: You can monitor and log the execution of tasks, making it easier to troubleshoot issues and track progress.

5. **Scalability**: Airflow is scalable and can handle both small and large workflows, making it suitable for a wide range of data processing needs.

6. **Extensibility**: You can extend Airflow's functionality by integrating it with external systems and tools.

# What is Airflow?

Apache Airflow is an open-source platform used for orchestrating, scheduling, and automating complex data workflows. It allows users to define, schedule, and monitor workflows as directed acyclic graphs (DAGs), making it easier to manage and automate data processing, ETL (Extract, Transform, Load) tasks, and other workflow-related activities. Airflow is highly customizable, extensible, and widely used for data pipeline automation and management.

# Airflow's Core Components

1. **Scheduler**:
   - The Scheduler is responsible for scheduling when and how often a DAG (Directed Acyclic Graph) should run. It continuously checks the status of DAGs and triggers the execution of tasks based on predefined schedules.

2. **Work Queue**:
   - Airflow uses a message queuing system (such as Celery or RabbitMQ) as a central communication hub between the Scheduler and Workers. It enqueues tasks for Workers to execute and monitors their progress.

3. **Metadata Database**:
   - Airflow uses a database (commonly PostgreSQL) to store metadata related to DAGs, tasks, schedules, and job status. This database is crucial for tracking the state and history of workflow executions.

4. **Executor**:
   - The Executor is a critical component responsible for executing tasks on worker nodes.
   - Airflow supports various Executors, including the LocalExecutor (for single-machine deployments), CeleryExecutor (for distributed execution using Celery), and more.
   - The Executor orchestrates the parallel execution of tasks across worker nodes, ensuring efficient task execution based on dependencies and scheduling.

5. **Worker**:
   - Workers are responsible for executing the tasks defined within DAGs. They pull tasks from the work queue, execute them, and report the results back to the Scheduler.

6. **DAGs (Directed Acyclic Graphs)**:
   - DAGs are at the heart of Airflow. They define the structure and dependencies of your workflow. Each DAG represents a workflow composed of tasks, with defined execution order and dependencies.

7. **Web Interface (UI)**:
   - The web-based UI provides a user-friendly way to interact with Airflow. Users can monitor the status of DAGs, view logs, trigger manual runs (Triggering), and visualize the structure of their workflows using the DAG visualization tool.

8. **CLI (Command Line Interface)**:
   - Airflow offers a command-line interface for interacting with and managing Airflow components, such as triggering DAGs, testing tasks, and performing administrative tasks.

9. **Triggering**:
   - Triggering allows users to manually start the execution of a DAG run, even if it's not scheduled to run at that moment. It is often used for ad-hoc or on-demand execution of workflows.
   - To trigger a DAG, users can use the Airflow web interface (UI) or command-line interface (CLI) to initiate a run.
   - Once triggered, Airflow will create a new DAG run instance and execute the tasks defined within the DAG based on their dependencies and order.

# Core Concepts

Certainly, let's explore the core concepts of Apache Airflow: DAGs, Operators (Action Operators, Transfer Operators, and Sensor Operators), and Task/Task Instance. We'll discuss the relationships between these concepts and provide an ordered example of how they interact.

1. **DAG (Directed Acyclic Graph)**:
   - A DAG in Apache Airflow represents a workflow or a series of tasks with dependencies.
   - It is a collection of tasks and the order in which they should be executed.
   - DAGs are directed (tasks have a defined order) and acyclic (no circular dependencies).

2. **Operator**:
   - Operators define what gets done by a task in a DAG.
   - There are different types of operators, including Action Operators, Transfer Operators, and Sensor Operators, each serving a specific purpose.

3. **Action Operators**:
   - Action Operators are used to perform actions or computations.
   - Examples include the `PythonOperator` for running Python functions, `BashOperator` for executing shell commands, and `DummyOperator` for creating placeholder tasks.

4. **Transfer Operators**:
   - Transfer Operators are used to transfer data between systems or tasks.
   - Examples include the `SqlSensor` for waiting on the availability of data in a database and the `S3ToRedshiftOperator` for transferring data from Amazon S3 to Redshift.

5. **Sensor Operators**:
   - Sensor Operators are used to wait for a certain condition to be met before proceeding with the execution of downstream tasks.
   - Examples include the `ExternalTaskSensor` for waiting on the status of external tasks and the `HttpSensor` for checking the availability of a web service.

6. **Task/Task Instance**:
   - A task represents a unit of work to be done in a DAG.
   - Each task is an instance of an operator and is associated with a specific execution date.
   - Task Instances are created when a DAG run is triggered and represent the individual execution of a task at a particular point in time.

# Single-Node and Multi-Node Architectures

**Single-Node Architecture**:

1. **Components on a Single Machine**:
   - In a single-node architecture, all Airflow components (Scheduler, Workers, Database, and Web Interface) are hosted on a single machine.

2. **Simplicity and Ease of Setup**:
   - Single-node setups are straightforward to install and suitable for smaller workflows, development, and testing purposes.
   - They require minimal configuration and are easier to manage.

3. **Limited Scalability**:
   - Single-node setups have limited scalability because they are constrained by the resources (CPU, memory, and storage) of a single machine.
   - They may not be suitable for running large or resource-intensive workflows.

4. **Low Fault Tolerance**:
   - Single-node architectures lack built-in high availability and fault tolerance.
   - If the single machine fails, the entire Airflow instance becomes unavailable.

**Multi-Node Architecture**:

1. **Distributed Setup**:
   - In a multi-node architecture, Airflow components are distributed across multiple machines or nodes.
   - Common components are the Scheduler, Workers, Database (often hosted on a separate server), and Web Interface (which may still be on a separate machine).

2. **Scalability and Resource Isolation**:
   - Multi-node architectures provide better scalability by allowing you to add more worker nodes to handle increased task loads.
   - Resources can be allocated more flexibly, enabling resource isolation for different workflows.

3. **High Availability**:
   - Multi-node setups can be configured for high availability, ensuring that the Airflow system remains accessible even if one node fails.
   - Redundant components and load balancing can be used to achieve this.

4. **Complexity and Maintenance**:
   - Multi-node setups are more complex to configure and maintain compared to single-node setups.
   - They often involve setting up a distributed message queue (e.g., Celery) and configuring external databases for better performance and reliability.

5. **Suitable for Production**:
   - Multi-node architectures are well-suited for production environments where reliability, scalability, and fault tolerance are crucial.
   - They can handle large, mission-critical workflows effectively.

# How does it work?

For the purpose of the course, a single-node architecture will be used, containing the Web Server, the DAGs folder, the
Scheduler, the Metastore, and the Executor.

This is how Apache Airflow works: When a DAG is placed in the DAGs folder, the Scheduler scans for new DAGs every 5
minutes. When it finds a new Python file, it checks for any changes or errors. The Scheduler performs these checks on
existing DAGs every 30 seconds.

The Scheduler runs the DAG, creating the DagRun Object. With the DagRun Object in a "running" status, it takes the first
task to be executed, turning it into a TaskInstance Object. This object has two statuses: "none" or "scheduled."

The Scheduler then sends the TaskInstance Object to the Executor, where it enters the Executor Queue and gets a "Queued"
status. The Executor creates a subprocess to run the task, which can result in success or failure.

Finally, the Web Server updates its UI with the Metastore data about the execution statuses.

# DAG Views

## DAG View

The DAG view displays all DAGs that have been recognized and loaded successfully in Airflow. Multiple example DAGs are
often loaded automatically. To activate a DAG, simply select the button on the left corner next to the DAG name.

The Owner field provides information about the owner of the DAG. Information under RUN shows statuses, SCHEDULE points
to schedules (e.g., daily, monthly, etc.), and there is support for using CRON expressions. LAST RUN shows when the DAG
last ran; NEXT RUN shows when the next execution is scheduled. The RECENT TASK acts as a small history of the most
recent executions of the DAG in question. Finally, we have the RUN button that allows us to manually trigger the DAG,
the trash bin representing the DELETE option (it does not delete the DAG file, but rather its metadata in the
interface), and the links to other useful views.

## Grid View

A useful visualization for quickly seeing the status of task histories. There is a diagram with some bars and a
right-hand side view with more detailed information about the execution.

## Graph View

A pleasing view that visually displays the structure of the DAG. A view with some rectangles, which represent tasks,
also shows the execution order, and through the outlines of the geometric shapes, we can use colors to understand the
execution statuses.

## Landing Times View

After some time of execution, as a history is generated, this graph becomes useful for monitoring the execution time,
which helps to consider future optimizations.

## Calendar View

A calendar view with colors marking the proportion of successes and failures. This helps to have a clear view of how the
DAG has been behaving over time, and through some points on the calendar, observe the days marked for future executions.

## Gantt View

A Gantt chart that helps observe bottlenecks. The more filled the rectangles are, the more attention we should pay, as
this shows longer execution times, meaning some bottleneck may be occurring. It is also possible to see, by the
interleaving of the rectangles, parallel executions.

## Code View

Allows viewing the code of the DAG and making necessary modifications if desired.

# The Project

## Project Structure

The project will be based on the creation of 1 DAG with 5 tasks.

1. **create_table**: This task will create a table in a PostgreSQL relational database (included in the Airflow container that I'll be using).

2. **is_api_available**: This task will check if a given API is available for obtaining future data.

3. **extract_user**: This task will obtain user information from the previously checked API.

4. **process_user**: This task will perform transformations on the users as necessary before they are stored (previously was the E, now it's the T of ETL).

5. **store_user**: Finally, this task will store the data in the database (the L of ETL, concluding the process).

![project](https://github.com/Shamslux/DataEngineering/assets/79280485/0869d9d7-b20a-4271-a20a-87dcbf186fbc)


## What is a DAG?

It is a directed acyclic graph, as can be seen in the model below, where the nodes are tasks and the directed edges correspond to their dependencies.

![dag](https://github.com/Shamslux/DataEngineering/assets/79280485/c338bdc6-cce1-4dcd-92e5-ef990e356c5c)

## Initial Skeleton of a DAG

```python
from airflow import DAG

from datetime import datetime

with DAG('user_processing', start_date=datetime(2022, 1, 1),
         schedule_interval='@daily', catchup=False) as dag:
    None
```

The code above is an example of the basic skeleton of a DAG. Let's review each item and its functions:

1. **from airflow import DAG**: Necessary for it to be recognized as an Airflow DAG.

2. **from datetime import datetime**: Important for us to use in the start_date variable.

3. **with DAG('user_processing'....**: Defines the unique ID to identify the DAG.

4. **start_date=datetime(2022, 1, 1)...**: Sets an initial date, i.e., when the DAG starts to be scheduled.

5. **schedule_interval='@daily'...**: We can use Cron or, as in the example, expressions like @daily. These expressions contain a built-in Cron definition (e.g., @daily = every day at midnight). For further explanations of these definitions, refer to the documentation.

6. **catchup=False...**: If this option is left as true, all subsequent executions that should have run will be executed by Airflow. Leaving it as False provides greater control, which can be a good option for better managing DAG executions.

7. **None**: Since we haven't created anything yet, we'll just leave it empty.

## What is an Operator?

Simply put, Operators are the tasks within the DAG. An important tip is: never pass two different tasks within the same
Operator. For example, if you have a PythonOperator to clean the data and another one to process the data, never pass
both tasks as a single Operator. Why? Because if there's an error, both processes will need to start over!

For better practices and organization of projects, create one PythonOperator to clean the data and another one to
process the data.

![operator_dont_do](https://github.com/Shamslux/DataEngineering/assets/79280485/b07a2aff-3c85-46da-8b3c-8cb2c4fc6bae)

### Types of Operators

1. **Action Operators**: ***Execute*** an action.

2. **Transfer Operators**: ***Transfer*** data.

3. **Sensors**: ***Wait for*** a condition to occur.

## Providers

The installation of Airflow is modular. When you install it, you have the core module. But what if you wanted to
interact with AWS? Or with Dbt? For that, you would need to install the providers, which allow Airflow to interact with
these other tools and environments. This is one of the features that makes Airflow so powerful and scalable.

![providers](https://github.com/Shamslux/DataEngineering/assets/79280485/2da45067-280f-4648-94bc-1dbd60bcc24d)
