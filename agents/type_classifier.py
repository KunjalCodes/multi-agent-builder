from llm.groq_client import GroqClient


class TypeClassifierAgent:
    def __init__(self):
        self.client = GroqClient()
        self.system_prompt = (
            "You are a project type classifier.\n\n"
            "Given a user project idea, respond with ONLY ONE line:\n\n"
            "PROJECT_TYPE: frontend\n"
            "OR\n"
            "PROJECT_TYPE: fastapi\n\n"
            "Rules:\n"
            "- If it mentions HTML, CSS, website, landing page, portfolio, UI, design → frontend\n"
            "- If it mentions API, backend, CRUD, database, FastAPI → fastapi\n"
            "- No explanation.\n"
            "- Only one line output.\n"
        )

    def run(self, user_input: str) -> str:
        return self.client.generate(self.system_prompt, user_input)
