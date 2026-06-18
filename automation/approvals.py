class ApprovalManager:

    def can_execute(
        self,
        action
    ):

        return {

            "action":
                action,

            "approved":
                False
        }