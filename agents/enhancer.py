from llm.groq_client import GroqClient


class EnhancerAgent:
    def __init__(self):
        self.client = GroqClient()
        self.system_prompt = (
            "You are a senior UI/UX engineer.\n\n"
            "You will receive a project in this exact format:\n\n"
            "PROJECT_TYPE: ...\n"
            "FILE: path\n"
            "<START_CODE>\n"
            "code\n"
            "<END_CODE>\n\n"

            "Your job:\n"
            "- Improve the QUALITY of the code inside <START_CODE> blocks.\n"
            "- Improve styling, spacing, UI if frontend.\n"
            "- Do NOT change file names.\n"
            "- Do NOT add new files.\n"
            "- Do NOT remove files.\n"
            "- Do NOT change PROJECT_TYPE line.\n"
            "- Do NOT modify FILE lines.\n"
            "- Do NOT remove <START_CODE> or <END_CODE>.\n"
            "- Only rewrite content inside the code blocks.\n\n"

            "Return output in EXACT SAME FORMAT.\n"
            "Structure must remain identical.\n"
        )

    def run(self, code_output: str) -> str:
        return self.client.generate(self.system_prompt, code_output)
