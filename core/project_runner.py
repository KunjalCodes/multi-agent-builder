import os
import subprocess
import webbrowser
import time


class ProjectRunner:
    def __init__(self):
        pass

    def run(self, project_path: str, project_type: str):
        if project_type == "frontend":
            self.run_frontend(project_path)
        elif project_type == "fastapi":
            self.run_fastapi(project_path)
        else:
            print("❌ Unknown project type.")

    def run_frontend(self, project_path: str):
        print("🚀 Starting frontend server...")

        os.chdir(project_path)
        port = 8000

        try:
            process = subprocess.Popen(
                ["python", "-m", "http.server", str(port)]
            )

            time.sleep(2)

            url = f"http://localhost:{port}"
            print(f"🌐 Opening browser at {url}")
            webbrowser.open(url)

            process.wait()

        except Exception as e:
            print("❌ Error running frontend project:")
            print(e)

    def run_fastapi(self, project_path: str):
        print("🚀 Starting FastAPI server...")

        os.chdir(project_path)
        port = 8000

        try:
            process = subprocess.Popen(
                [
                    "uvicorn",
                    "main:app",
                    "--reload",
                    "--port",
                    str(port),
                ]
            )

            time.sleep(3)

            url = f"http://127.0.0.1:{port}"
            print(f"🌐 FastAPI running at {url}")
            webbrowser.open(url)

            process.wait()

        except Exception as e:
            print("❌ Error running FastAPI project:")
            print(e)
