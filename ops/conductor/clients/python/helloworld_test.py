
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
  api_config = Configuration(
    debug=True,
    # server_api_url='http://localhost:8080/api' # DEV_ENV
  )

  workflow_executor = WorkflowExecutor(configuration=api_config)

  # register workflow
  workflow = register_workflow(workflow_executor=workflow_executor)

  # WARN: not compatiable
  # HTTP response body: {"status":404,"message":"No static resource api/workflow/execute/greetings/1.","instance":"56822bb740e4","retryable":false}
  # use UI 'Workbench' instead
  workflow_run = workflow_executor.execute(name=workflow.name, 
                                           version=workflow.version,
                                           workflow_input={'name': 'DevOps'})
  print(f'\nworkflow result: {workflow_run.output["result"]}\n')
  print(f'workflow execution: {api_config.ui_host}/execution/{workflow_run.workflow_id}\n')

if __name__ == '__main__':
  main()