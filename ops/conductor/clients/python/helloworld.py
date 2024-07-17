
from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from conductor.client.configuration.configuration import Configuration
from conductor.client.automator.task_handler import TaskHandler

from greetings_worker import GreetWorker
from greetings_workflow import greetings_workflow

def register_workflow(workflow_executor: WorkflowExecutor) -> ConductorWorkflow:
  workflow = greetings_workflow(workflow_executor=workflow_executor)
  workflow.register(overwrite=True)
  return workflow

def main():
  print("...")
  api_config = Configuration(
    debug=True,
    # server_api_url='http://localhost:8080/api' # DEV_ENV
  )

  workflow_executor = WorkflowExecutor(configuration=api_config)

  # register workflow
  workflow = register_workflow(workflow_executor=workflow_executor)

  # start worker polling
  task_handler = TaskHandler(configuration=api_config,
                            #  workers=[GreetWorker(task_definition_name='greet')],
                            #  import_modules=['greetings_worker']
                             )
  task_handler.start_processes()
  
  # FIX: REST API incompatible
  # .venv\lib\python3.12\site-packages\conductor\client\http\api\workflow_resource_api.py
  # def execute_workflow_with_http_info(self, body, request_id, name, version, **kwargs):  # noqa: E501
  # return self.api_client.call_api(
  #       '/workflow/{name}', 'POST',
  #          response_type='str',

  workflow_id = workflow_executor.execute(name=workflow.name, 
                                           version=workflow.version,
                                           workflow_input={'name': 'DevOps'})
  print(f'workflow execution: {api_config.ui_host}/execution/{workflow_id}\n')

  import time
  time.sleep(3.0)

  task_handler.stop_processes()

if __name__ == '__main__':
  main()