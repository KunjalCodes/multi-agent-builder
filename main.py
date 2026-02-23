import os
import re

from agents.type_classifier import TypeClassifierAgent
from agents.planner import PlannerAgent
from agents.architect import ArchitectAgent
from agents.coder import CoderAgent
from agents.enhancer import EnhancerAgent
from core.file_manager import FileManager
from core.project_runner import ProjectRunner
from core.logger import Logger


def main():
    print("\n✨ Multi-Agent Builder\n")

    user_input = input("Enter your project idea:\n\n> ")

    # -------- Type Classification --------
    Logger.stage("🔎 Detecting project type...")
    classifier = TypeClassifierAgent()
    type_output = classifier.run(user_input)

    match = re.search(r"PROJECT_TYPE:\s*(\w+)", type_output)
    if not match:
        Logger.error("Could not detect project type.")
        return

    project_type = match.group(1).lower()
    Logger.success(f"Detected project type: {project_type}")

    # -------- Create Project Folder --------
    Logger.stage("📁 Creating project folder...")

    project_name = re.sub(r'[^a-zA-Z0-9_]+', '_', user_input.lower())
    project_path = os.path.join("generated_projects", project_name)

    os.makedirs(project_path, exist_ok=True)

    Logger.success(f"Project folder created at: {project_path}")

    # -------- Planner --------
    Logger.stage("🧠 Planner generating plan...")
    planner = PlannerAgent()
    plan = planner.run(
        f"PROJECT_TYPE: {project_type}\n\nUSER IDEA:\n{user_input}"
    )
    Logger.success("Plan generated.")

    # -------- Architect --------
    Logger.stage("🏗 Architect creating structure...")
    architect = ArchitectAgent()
    architecture = architect.run(
        f"PROJECT_TYPE: {project_type}\n\nPLAN:\n{plan}"
    )
    Logger.success("Architecture created.")

    # -------- Coder --------
    Logger.stage("💻 Coder generating base project...")
    coder = CoderAgent()
    base_code_output = coder.run(
        f"PROJECT_TYPE: {project_type}\n\nARCHITECTURE:\n{architecture}"
    )
    Logger.success("Base project generated.")

    # -------- Enhancer --------
    Logger.stage("🎨 Enhancer improving quality...")
    enhancer = EnhancerAgent()
    code_output = enhancer.run(base_code_output)
    Logger.success("Project enhanced.")

    # -------- File Writing --------
    Logger.stage("📂 Writing files to disk...")
    file_manager = FileManager(project_path)
    success = file_manager.write_files_from_response(code_output)

    if not success:
        Logger.error("File writing failed.")
        return

    Logger.success("Files written successfully.")

    # -------- Run Project --------
    Logger.stage("🚀 Running project...")
    runner = ProjectRunner()
    runner.run(project_path, project_type)


if __name__ == "__main__":
    main()
