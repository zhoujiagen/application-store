from conductor.client.worker.worker_interface import WorkerInterface
from conductor.client.worker.worker_task import worker_task


@worker_task(task_definition_name='greet')
def greet(name: str) -> str:
    return f'Hello {name}'


class GreetWorker(WorkerInterface):
    def execute(self, task):
        task_result = self.get_task_result_from_task(task)
        v = str(task.input_data['name'])
        task_result.add_output_data('result',  f'Hello {v}')
        task_result.status = 'COMPLETED'
        return task_result
