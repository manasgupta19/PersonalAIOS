from automation.approvals import (
    ApprovalManager
)


approval = (
    ApprovalManager()
)


class Workflow:

    def propose(
        self,
        tasks
    ):

        proposals = []

        for t in tasks:

            proposals.append(

                approval.can_execute(

                    f"Follow up: {t['task']}"

                )

            )

        return proposals