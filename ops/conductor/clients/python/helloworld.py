
from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from conductor.client.configuration.configuration import Configuration
from conductor.client.automator.task_handler import TaskHandler

from greetings_worker import GreetWorker
from greetings_workflow import greetings_workflow


from conductor.client.orkes_clients import OrkesClients


def register_workflow(workflow_executor: WorkflowExecutor) -> ConductorWorkflow:
  workflow = greetings_workflow(workflow_executor=workflow_executor)
  workflow.register(overwrite=True)
  return workflow

def main():
  api_config = Configuration(
    debug=False,
    # server_api_url='http://localhost:8080/api' # DEV_ENV
  )

  workflow_executor = WorkflowExecutor(configuration=api_config)

  # register workflow
  workflow = register_workflow(workflow_executor=workflow_executor)

  # start worker polling
  task_handler = TaskHandler(configuration=api_config,
                             workers=[GreetWorker(task_definition_name='greet')],
                            #  import_modules=['greetings_worker']
                             )
  task_handler.start_processes()
  # WARN
  # _pickle.PicklingError: Can't pickle <function greet at 0x0000018366B0C900>: it's not the same object as greetings_worker.greet

  # workflow_run = workflow_executor.execute(name=workflow.name, 
  #                                          version=workflow.version,
  #                                          workflow_input={'name': 'DevOps'})
  # print(f'\nworkflow result: {workflow_run.output["result"]}\n')
  # print(f'workflow execution: {api_config.ui_host}/execution/{workflow_run.workflow_id}\n')
  start_workflow()
  

  task_handler.stop_processes()

def start_workflow():
  # https://github.com/conductor-sdk/conductor-python/tree/main?tab=readme-ov-file#execute-workflow-synchronously
  api_config = Configuration()
  clients = OrkesClients(configuration=api_config)
  workflow_client = clients.get_workflow_client() 

  from conductor.client.http.models import StartWorkflowRequest

  request = StartWorkflowRequest()
  request.name = 'greetings'
  request.version = 1
  request.input = {'name': 'Conductor'}

  workflow_run = workflow_client.execute_workflow(
          start_workflow_request=request, 
          wait_for_seconds=12)
  print(f'\nworkflow result: {workflow_run.output["result"]}\n')
  print(f'workflow execution: {api_config.ui_host}/execution/{workflow_run.workflow_id}\n')

if __name__ == '__main__':
  main()
