import ollama

from llm.model_registry import (
    MODEL
)


class Brain:

    def ask(
        self,
        prompt
    ):

        response = (

            ollama.chat(

                model=MODEL,

                messages=[

                    {

                        "role":
                            "user",

                        "content":
                            prompt
                    }

                ]
            )
        )

        return (

            response

            ["message"]

            ["content"]

        )