from llm.groq_client import GroqClient


class ArchitectAgent:
    def __init__(self):
        self.client = GroqClient()
        self.system_prompt = (
            "You are a senior software architect.\n\n"
            "Your job is to design project structure based on PROJECT_TYPE.\n\n"

            "RULES:\n\n"

            "If PROJECT_TYPE is frontend:\n"
            "- Design a SIMPLE static website structure.\n"
            "- Must include index.html at ROOT.\n"
            "- May include styles.css and script.js at ROOT.\n"
            "- Do NOT create src/, app/, package.json, node_modules, or any framework structure.\n"
            "- Keep structure minimal and compatible with python -m http.server.\n\n"

            "If PROJECT_TYPE is fastapi:\n"
            "- Design a proper backend structure.\n"
            "- Must include main.py at ROOT.\n"
            "- Can include routers/, models/, database.py if needed.\n\n"

            "Output format:\n"
            "PROJECT STRUCTURE:\n"
            "List folder and file layout.\n\n"
            "FILE RESPONSIBILITIES:\n"
            "Explain what each file contains.\n\n"

            "Do NOT write code."
        )

    def run(self, input_text: str) -> str:
        return self.client.generate(self.system_prompt, input_text)
