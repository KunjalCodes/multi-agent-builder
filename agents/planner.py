from llm.groq_client import GroqClient


class PlannerAgent:
    def __init__(self):
        self.client = GroqClient()
        self.system_prompt = """
You are a senior product planner.

Your job is to:
1. Understand the user’s project idea.
2. Convert it into a structured development plan.

You must return:

PROJECT GOAL:
Clear description of what is being built.

FEATURES:
Bullet list of required features.

TECH STACK:
Recommended technologies.

HIGH LEVEL TASK BREAKDOWN:
Step-by-step development stages.

Do NOT write code.
Only produce structured planning output.
"""

    def run(self, user_input: str) -> str:
        return self.client.generate(self.system_prompt, user_input)
