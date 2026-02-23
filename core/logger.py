import time
import sys


class Logger:
    @staticmethod
    def stage(message: str):
        print(f"\n{message}")
        time.sleep(0.5)

    @staticmethod
    def info(message: str):
        print(message)
        time.sleep(0.2)

    @staticmethod
    def success(message: str):
        print(f"✅ {message}")
        time.sleep(0.2)

    @staticmethod
    def error(message: str):
        print(f"❌ {message}")
        time.sleep(0.2)
