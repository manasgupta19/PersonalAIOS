from llm.client import Brain

brain = Brain()

result = brain.ask(
    """
Goal:
Improve career growth

Provide:
Analysis
Actions
"""
)

print(result)