import os
import re


class FileManager:
    def __init__(self, base_path: str):
        self.base_path = base_path

    def write_files_from_response(self, response: str):
        """
        Parse LLM response and write files to disk.

        Expected format:

        FILE: path/to/file.ext
        <START_CODE>
        code here
        <END_CODE>
        """

        pattern = r"FILE:\s*(.*?)\n<START_CODE>\n(.*?)\n<END_CODE>"
        matches = re.findall(pattern, response, re.DOTALL)

        if not matches:
            print("❌ No files detected in coder response.")
            return False

        for file_path, code in matches:
            file_path = file_path.strip()

            # Skip directories accidentally generated
            if file_path.endswith("/") or "." not in os.path.basename(file_path):
                continue

            full_path = os.path.join(self.base_path, file_path)

            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(code.strip())

            print(f"✅ Created: {full_path}")

        return True
