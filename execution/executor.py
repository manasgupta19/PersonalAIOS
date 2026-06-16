from execution.timeline import (
    Timeline
)

from execution.task_manager import (
    TaskManager
)


timeline = (
    Timeline()
)

tasks = (
    TaskManager()
)


def create_plan(
    goal
):

    plan = (

        timeline
        .generate(
            goal
        )
    )

    for t in plan:

        tasks.save(
            t
        )

    return plan