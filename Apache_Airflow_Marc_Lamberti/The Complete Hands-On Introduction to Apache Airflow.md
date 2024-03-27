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

## What is a Sensor?

Sensors wait for an event (or condition) before taking action. For example, imagine a person waiting at a bus stop for
some time. They will remain there until they spot the bus (the event) and then they will stand up to wait for the
vehicle to stop so they can finally board it.

### Two important concepts in Sensors

There are two concepts involving connection validation time. The first one is the ***poke_interval*** and the second one
is ***timeout***.

- **poke_interval**: This parameter sets the interval between sensor condition checks. It specifies how often the sensor
will check if the desired condition has been met. For example, if you set a ***poke_interval*** of 5 minutes, the sensor
will check the condition every 5 minutes to see if it has been met.

- **timeout**: The timeout parameter sets how long the sensor will wait until the condition is met before considering it
a failure. If the condition is not met within this period of time, the sensor will fail, and the workflow can handle the
failure according to the specified settings.

```python
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor

from datetime import datetime

with DAG('user_processing', start_date=datetime(2022, 1, 1),
         schedule_interval='@daily', catchup=False) as dag:
    
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql='''
              CREATE TABLE IF NOT EXISTS users(
                    firstname TEXT NOT NULL,
                    lastname  TEXT NOT NULL,
                    country   TEXT NOT NULL,
                    username  TEXT NOT NULL,
                    password  TEXT NOT NULL,
                    email     TEXT NOT NULL
              );
          '''
    )

    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id='user_api',
        endpoint='api/'
    )
```
1. **from airflow.providers.postgres.operators.postgres import PostgresOperator**: Imports the correct provider for
PostgreSQL. Note: I have already configured the connection in the Airflow webserver (there is a PostgreSQL installed
along with the Docker Compose image used).

2. **create_table = PostgresOperator**: The new task will make use of the appropriate operator to interact with
PostgreSQL.

3. **postgres_conn_id='postgres'**: Connection identifier (already configured, as mentioned before).

4. **sql=...**: The content of the SQL query.

5. **from airflow.providers.http.sensors.http import HttpSensor**: Provider for the HTTP sensor.

6. **http_conn_id='user_api'**: Specifies the HTTP connection to be used by the sensor to communicate with the API. This
connection must be previously configured in Airflow using the Connections menu of the Airflow web interface.

7. **endpoint='api/'**: Indicates the API endpoint that the sensor will access to check if it is available. In this
example, the sensor will access the api/ endpoint of the API.

## What is a Hook?

In a very simple way, the example given by the instructor involves a PostgreSQL database. The PostgresOperator would be
responsible for connecting to the database; however, between the Operator and the database, the PostgresHook comes into
play. It is necessary to abstract all the complexity involved in interacting with the PostgreSQL database.

In essence, it is necessary to use Hooks as intermediaries between the Operators and the entity being connected.

```python
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

def _store_user():
    hook = PostgresHook(postgres_conn_id='postgres')
    hook.copy_expert(
        sql="COPY users FROM stdin WITH DELIMITER as ','",
        filename='/tmp/processed_user.csv'
    )

with DAG('user_processing', start_date=datetime(2022, 1, 1),
         schedule_interval='@daily', catchup=False) as dag:
...

    store_user = PythonOperator(
        task_id='store_user',
        python_callable=_store_user
    )

create_table >> is_api_available >> extract_user >> process_user >> store_user
```

## The Final Result of the DAG

![the_graph_of_dag](https://github.com/Shamslux/DataEngineering/assets/79280485/41dc7fd4-efce-4339-99e0-bf41724d52a1)

Above, we can see the graph showing the relationship between the elements of the DAG. In essence, it is a model that demonstrates the ability to create a table in a PostgreSQL database, check if an API is available, retrieve data from that API, and, using Pandas resources to handle JSON, structure it in a more aesthetic way and save it to the database, utilizing the features we covered with the Hook (read the previous topic above).

## Executing the DAG with Success!

We can see in the image below that the DAG was executed successfully.

![dag_status](https://github.com/Shamslux/DataEngineering/assets/79280485/f7c589f4-2666-408e-924e-85ea7457ec4f)

In the image below, we can see that the data transfer from the user extraction API was successful and that the CSV document was saved properly in the container.

![csv_airflow_downloaded](https://github.com/Shamslux/DataEngineering/assets/79280485/e4758a97-4acd-4b80-9661-c630665ade99)


Finally, in the image below, we can see the container's terminal containing PostgreSQL and with the table we had created in the DAG, now populated with the user obtained from the public API that generates random users.

![psql_user_in_table](https://github.com/Shamslux/DataEngineering/assets/79280485/c4dc5a5e-3c5f-4990-93a2-dd6d0e761ac3)

## Scheduling DAG Execution

- **start_date**: the timestamp from which the scheduler will attempt to backfill

- **schedule_interval**: how often a DAG runs

- **end_date**: the timestamp from which a DAG ends

```python

with DAG('my_example_dag', start_date=datetime(2022, 1, 1),
         schedule_interval='@daily') as dag:
```

The *schedule_interval* accepts CRON-like expressions, but there are some predefined forms (like the case of @daily). However, for finer adjustments, it is recommended to understand how to work with CRON.

Note: The DAG is triggered AFTER the start_date/last_run + the schedule_interval.

### A Practical Example of DAG Execution

Let's assume we have a DAG with a *start_date* at 10:00 AM and a *schedule_interval* every 10 minutes.

At 10:00 AM, nothing happens, although it's the *start_date* marker. After waiting for 10 minutes, Airflow will actually execute the DAG at 10:10 AM.

After 10 minutes, the DAG will be executed again, now at 10:20 AM.

### The Catchup Mechanism

In summary, if you create a DAG and set the *start_date* to, for example, '2022-01-03', but you created it on '2022-01-07' and you're going to run it for the present day, if the *catchup* is not configured as *false*, then the DAG will perform a backfill execution for each previous day from the *start_date* and not from the present day ('2022-01-07'). To prevent this from happening, it will be necessary to configure the *catchup* as *false*.

## What is a Dataset?

A Dataset is a logical grouping of data, such as a file, a table, etc. In short, anything that holds data, because, basically, Airflow doesn't care much whether it's a file or a table.

The Dataset has two properties. The URI parameter and the EXTRA parameter.

- **URI**: is a unique identifier for your dataset, as well as the actual path of the data. It must be composed only of ASCII characters, it is case sensitive, and the URI schema cannot be airflow.

```python
from airflow import Dataset

# valid datasets:
schemeless = Dataset("/path/file.txt")
csv_file = Dataset("file.csv")

# invalid datasets:
reserved = Dataset("airflow://file.txt")
not_ascii = Dataset("file_datašet")
```

- **EXTRA**: is a JSON dictionary where you can define additional information about your dataset.

```python
from airflow import Dataset

my_file = Dataset(
    "s3://dataset/file.csv",
    extra={'owner': 'james'},
)
```
## Bye bye Schedule Interval

Starting from version 2.4 of Airflow, there was a change in how DAGs were scheduled. See an example below:

```python
# before
with DAG(schedule_interval='@daily')

with DAG(timetable=MyTimeTable)

# since 2.4

with DAG(schedule=...)
```

## Scheduling DAGs based on datasets

Let's create two DAGs. One will produce a TXT file that will be our dataset. The other will be triggered from the moment this file undergoes an update.

### Structure of the "producer" DAG

```python
from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")

with DAG(
    dag_id="producer",
    schedule="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False
):
    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri, "a+") as f:
            f.write("producer update")
    
    update_dataset()
```

1 - Notice how the *schedule* is already following the model after the 2.4 update.

### Structure of the "consumer" DAG

```python
from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")

with DAG(
    dag_id="consumer",
    schedule=[my_file],
    start_date=datetime(2022, 1, 1),
    catchup=False
):
    @task
    def read_dataset():
        with open(my_file.uri, "r") as f:
            print(f.read())
    
    read_dataset()
```

### Executing the DAG

![dataset_view](https://github.com/Shamslux/DataEngineering/assets/79280485/b8fbc06c-025c-4476-a35d-c8f71abccb91)

Above, see the structure available in the "Datasets" tab of the Airflow webserver. We can see how the "consumer" DAG is triggered after the action of the "producer" DAG (responsible for updating the "my_file" dataset). Additionally, both will only function when they are both activated.

Below are the images showing the success of the DAGs.

![producer_success](https://github.com/Shamslux/DataEngineering/assets/79280485/0f7407eb-d59a-43f7-87b1-a38d3a30be9a)

![consumer_success](https://github.com/Shamslux/DataEngineering/assets/79280485/7b140384-e838-4db1-b2a9-24bf4fddf870)

![consumer_log](https://github.com/Shamslux/DataEngineering/assets/79280485/aeda88c8-0439-4d40-8a58-4928f37ec790)

## Waiting for Multiple Datasets

What if we wanted to wait for more than one file besides the single TXT file in our example? To achieve this, we would simply adjust the producer DAG to update two files, as shown below:

```python
from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

with DAG(
    dag_id="producer",
    schedule="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False
):
    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri, "a+") as f:
            f.write("producer update")

    @task(outlets=[my_file_2])
    def update_dataset_2():
        with open(my_file_2.uri, "a+") as f:
            f.write("producer update")
    
    update_dataset() >> update_dataset_2()
```

After this adjustment in the structure of the producer DAG, let's see the necessary adjustment in the consumer DAG:

```python
from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

with DAG(
    dag_id="consumer",
    schedule=[my_file, my_file_2],
    start_date=datetime(2022, 1, 1),
    catchup=False
):
    @task
    def read_dataset():
        with open(my_file.uri, "r") as f:
            print(f.read())
    
    read_dataset()
```

In the case of the structure above, we basically added *my_file_2* inside the list passed in *schedule*.

With that, below is how the image in the "Datasets" tab looks:

![two_datasets_datasets_view](https://github.com/Shamslux/DataEngineering/assets/79280485/2b1a754b-c13b-4084-a1de-b91ff728cd2f)


Thus, we learned how we can handle more than one file waiting for an update so that the DAG can be triggered after this update occurs.

## Dataset limitations

- DAGs can only use Datasets in the same Airflow instance. A DAG cannot wait for a Dataset defined in another Airflow instance.

- Consumer DAGs are triggered every time a task that updates datasets completes successfully. **Airflow doesn't check whether the data has been effectively updated.**

- You can't combine different schedules like datasets with cron expressions.

- If two tasks update the same dataset, as soon as one is done, that triggers the Consumer DAG immediately without waiting for the second task to complete.

- Airflow monitors datasets only within the context of DAGs and Tasks. If an external tool updates the actual data represented by a Dataset, Airflow has no way of knowing that.

# Databases and Executors

## What's an Executor?

The executor doesn't execute your tasks, but it defines how to execute your tasks. There are several executors for this: sequential, local, and celery. To change the executor, just access the *airflow.cfg* file. Inside it, you will see the *executor* parameter. By default, it will be like this: *executor = SequentialExecutor*.

Note: Throughout the course, our docker-compose.yaml configured the environment variable **AIRFLOW_CORE_EXECUTOR** as *CeleryExecutor* (which overrides the *executor* parameter in the *airflow.cfg* file).

## SequentialExecutor

SequentialExecutor is the default executor installed with Airflow. It uses the basic structure: Web Server, Scheduler, and SQLite (database). When running the DAGs, it will execute them one by one (see the image below). In the example image, T2 would be executed first, and after its completion, T3 would be executed. T2 and T3 would not be executed simultaneously. This executor is used more for testing, debugging, and simpler tasks.

![sequential_executor_example](https://github.com/Shamslux/DataEngineering/assets/79280485/f21167f0-9097-4ef7-9eeb-1299f1faa6d4)

## LocalExecutor

It is a step ahead of the SequentialExecutor, allowing multiple tasks to be executed, however, only on a single machine. It uses the same instance, but now uses a different database. In this case, PostgreSQL, MySQL, Oracle, or any other desired database, except SQLite, can be used. By doing so, it becomes possible to execute multiple tasks simultaneously.

![localexecutor_structure](https://github.com/Shamslux/DataEngineering/assets/79280485/6ad53bc5-54c4-4ffd-83d8-8494e8074113)

Be aware that this executor does not scale well, as it is limited to the resources of the single machine that runs it.

### Configuring this executor

```shell
executor=LocalExecutor

sql_alchemy_conn=postgresql+psycopg2://<user>:<password>@<host>/<db>
```
## CeleryExecutor

It is excellent for sketching out the number of tasks you can execute simultaneously. The CeleryExecutor features the Celery Queue with the Result Backend (where the Airflow Workers store the statuses of the tasks that have been executed) and the Broker (which is nothing more than a queue where the orchestrator sends a task to be executed and the Airflow Workers pick up the tasks from this queue to execute them).

![celery_1](https://github.com/Shamslux/DataEngineering/assets/79280485/cb5bcdca-e3a1-4ab2-a431-454106bd18ca)

![celery_2](https://github.com/Shamslux/DataEngineering/assets/79280485/05e054ee-1c2e-4a16-a8cd-baf6218d9a00)

![celery_3](https://github.com/Shamslux/DataEngineering/assets/79280485/308ffc93-3e98-43a8-9586-257b8b66c8af)

### Configuring this executor

Note: Keep in mind that it's necessary to install the Celery Queue (using, for example, Redis)

```shell

executor=CeleryExecutor

sql_alchemy_conn=postgresql+psycopg2://<user>:<password>@<host>/<db>

celery_result_backend=postgresql+psycopg2://<user>:<password>@<host>/<db>

celery_broker_url=redis://:@redis:6379/0
```
## Removing example DAGs

For a cleaner visualization of the webserver interface, we can adjust the *docker-compose* command to remove the example DAGs that come with the project.

![removing_dag_examples](https://github.com/Shamslux/DataEngineering/assets/79280485/87a4102b-a0a1-4d5d-8bff-c4683e6a15ef)

## Using Flower for monitoring

To activate the Flower feature (a dashboard that allows us to monitor tasks and workers when using the CeleryExecutor), we need to use the commands below in our Airflow's *docker-compose*:

```shell
docker-compose down
docker-compose --profile flower up -d
```

After that, we will have the container accessible through the configured port. We will see the following image of the web platform:

![flower_1](https://github.com/Shamslux/DataEngineering/assets/79280485/c4bafe2d-95ec-4de6-b98c-6247b786e295)

![flower_2](https://github.com/Shamslux/DataEngineering/assets/79280485/7a17e58d-170c-49ea-948d-294e8135581a)

**Note**: The "Max concurrency", for example, shows us that this worker can handle up to 16 tasks running at the same time. 

**Note²**: The instructor basically just showed this "pool" part and "queue", but did not enter into many details about the other aspects for time saving.

## What are Queues?

Queues are waiting lines for Airflow tasks. Tasks are pushed into the queue to be executed. Each task will be distributed to a Worker, but the key point of the queue is the ability to organize according to the desired Worker (defining a queue for the desired Worker, which is a machine).

![queue_example](https://github.com/Shamslux/DataEngineering/assets/79280485/d31233f8-a745-4782-be2e-121018d012a6)

With this, we can see, in the image below, that Celery allows its queues to define the Workers that best meet the tasks' needs. Thus, a **high_cpu** queue can be set for a machine with many processors, an **ml_model** queue can be set for a machine with a high GPU power, and a **default** queue, with more common tasks, can be assigned to a machine with fewer resources.

![queues_defined](https://github.com/Shamslux/DataEngineering/assets/79280485/6be140d0-dc9a-4a58-975c-086b0a8b79e8)

