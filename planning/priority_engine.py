class PriorityEngine:

    def score(
        self,
        task
    ):

        score = 50

        text = (
            task["task"]
            .lower()
        )

        keywords = {

            "career": 20,
            "money": 20,
            "health": 20,
            "family": 20,
            "learn": 15,
            "urgent": 30
        }

        for k, v in keywords.items():

            if k in text:

                score += v

        return min(
            score,
            100
        )

    def rank(
        self,
        tasks
    ):

        ranked = []

        for t in tasks:

            t["priority"] = (
                self.score(
                    t
                )
            )

            ranked.append(
                t
            )

        return sorted(

            ranked,

            key=lambda x:
                x["priority"],

            reverse=True
        )