# Conductor
- https://docs.conductor-oss.org/devguide/running/docker.html

```shell
# locally build
git clone https://github.com/conductor-oss/conductor.git

cd conductor/docker
docker build -t conductor:server -f server/Dockerfile ../
```

Access UI: `http://localhost:5000`.

Access Swagger doc: `http://localhost:8080/swagger-ui/index.html`.

## tutorial

### Manual
- https://docs.conductor-oss.org/devguide/labs/first-workflow.html

1. create workflow: 'Definitions' > 'New Workflow Definition'.

```json
{
  "name": "first_sample_workflow",
  "description": "First Sample Workflow",
  "version": 1,
  "tasks": [
    {
      "name": "get_population_data",
      "taskReferenceName": "get_population_data",
      "inputParameters": {
        "http_request": {
          "uri": "https://datausa.io/api/data?drilldowns=Nation&measures=Population",
          "method": "GET"
        }
      },
      "type": "HTTP"
    }
  ],
  "inputParameters": [],
  "outputParameters": {
    "data": "${get_population_data.output.response.body.data}",
    "source": "${get_population_data.output.response.body.source}"
  },
  "schemaVersion": 2,
  "restartable": true,
  "workflowStatusListenerEnabled": false,
  "ownerEmail": "example@email.com",
  "timeoutPolicy": "ALERT_ONLY",
  "timeoutSeconds": 0
}
```

2. start workflow: `POST /api/workflow/{name}`
   - http://localhost:8080/swagger-ui/index.html?configUrl=/api-docs/swagger-config#/workflow-resource/startWorkflow_1

3. view results.

See 'Executions' > 'Worklow Input/Output', example:

```json
{
  "data": [
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2022,
      "Year": "2022",
      "Population": 331097593,
      "Slug Nation": "united-states"
    },
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2021,
      "Year": "2021",
      "Population": 329725481,
      "Slug Nation": "united-states"
    },
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2020,
      "Year": "2020",
      "Population": 326569308,
      "Slug Nation": "united-states"
    },
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2019,
      "Year": "2019",
      "Population": 324697795,
      "Slug Nation": "united-states"
    },
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2018,
      "Year": "2018",
      "Population": 322903030,
      "Slug Nation": "united-states"
    },
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2017,
      "Year": "2017",
      "Population": 321004407,
      "Slug Nation": "united-states"
    },
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2016,
      "Year": "2016",
      "Population": 318558162,
      "Slug Nation": "united-states"
    },
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2015,
      "Year": "2015",
      "Population": 316515021,
      "Slug Nation": "united-states"
    },
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2014,
      "Year": "2014",
      "Population": 314107084,
      "Slug Nation": "united-states"
    },
    {
      "ID Nation": "01000US",
      "Nation": "United States",
      "ID Year": 2013,
      "Year": "2013",
      "Population": 311536594,
      "Slug Nation": "united-states"
    }
  ],
  "source": [
    {
      "measures": [
        "Population"
      ],
      "annotations": {
        "source_name": "Census Bureau",
        "source_description": "The American Community Survey (ACS) is conducted by the US Census and sent to a portion of the population every year.",
        "dataset_name": "ACS 5-year Estimate",
        "dataset_link": "http://www.census.gov/programs-surveys/acs/",
        "table_id": "B01003",
        "topic": "Diversity",
        "subtopic": "Demographics"
      },
      "name": "acs_yg_total_population_5",
      "substitutions": []
    }
  ]
}
```

### REST API

see [rest-api.ipynb](./clients/rest-api.ipynb).

## Clients
### Python
- https://github.com/conductor-sdk/conductor-python/blob/main/README.md

```shell
$ python --version
Python 3.12.4
$ python -m virtualenv .venv
$ source .venv/bin/activate
$ pip freeze > requirements.txt
```

```shell
$ python helloworld.py
16:26:46,183 [3825] conductor.client.automator.task_handler INFO     created worker with name=greet and domain=None
16:26:46,183 [3825] conductor.client.automator.task_handler INFO     TaskHandler initialized
16:26:46,183 [3825] conductor.client.automator.task_handler INFO     Starting worker processes...
16:26:46,185 [3825] conductor.client.automator.task_runner INFO     Polling task greet with domain None with polling interval 0.1
16:26:46,185 [3825] conductor.client.automator.task_handler INFO     Started 2 TaskRunner process
16:26:46,185 [3825] conductor.client.automator.task_handler INFO     Started all processes
16:26:46,185 [3825] conductor.client.automator.task_runner INFO     Polling task greet with domain None with polling interval 0.1
workflow execution: http://localhost:5000/execution/10864d60-a4fa-4edd-9f80-2b275f77c2b0

16:26:49,218 [3825] conductor.client.automator.task_handler INFO     Stopped worker processes...

# 'Workbench'
## Workflow Name: greetings
## Workflow version: 1
## Input: {"name": "there"}
# 'Execution'
## Workflow Input/Output: { "result": "Hello there" }
```