from execution.task_manager import (
    TaskManager
)

from automation.workflow import (
    Workflow
)


tasks = (
    TaskManager()
)

workflow = (
    Workflow()
)


def run():

    return (

        workflow
        .propose(

            tasks.all()

        )
    )