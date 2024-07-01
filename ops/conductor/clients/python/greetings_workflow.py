
from conductor.client.workflow.conductor_workflow import ConductorWorkflow
from conductor.client.workflow.executor.workflow_executor import WorkflowExecutor
from greetings_worker import greet
from conductor.client.workflow.task.timeout_policy import TimeoutPolicy

def greetings_workflow(workflow_executor: WorkflowExecutor) -> ConductorWorkflow:
  name = 'greetings'
  workflow = ConductorWorkflow(name=name, executor=workflow_executor)
  workflow.version = 1
  # workflow.timeout_policy(TimeoutPolicy.TIME_OUT_WORKFLOW)
  # workflow.timeout_seconds(3)
  workflow.owner_email('dev@devops.com')
  workflow >> greet(task_ref_name='greet_ref', name=workflow.input('name'))
  return workflow