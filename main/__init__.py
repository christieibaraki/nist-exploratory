import os
from pathlib import Path

__PARENT = os.path.dirname((os.path.dirname(__file__)))
MAIN_ROOT_DIR = os.path.join(__PARENT, "main")
DEMO_ROOT_DIR = os.path.join(__PARENT, "demo")
TEST_ROOT_DIR = os.path.join(__PARENT, "test")
ROOT_DIR = os.path.dirname(MAIN_ROOT_DIR)

