#! /bin/python3

import subprocess
import sys

print("You need to have pip installed.")
dependencies = ["pandas", "numpy", "sklearn", "keras", "matplotlib"]
device = ""
while device not in ["CPU", "GPU", "cpu", "gpu"]:
    device = input("Compute with CPU/GPU?\n")

# choosing if to use cpu or gpu
if device in ["cpu", "CPU"]:
    dependencies.append("tensorflow")
else:
    dependencies.append("tensorflow-gpu")

# installing packages
for tmp in dependencies:
    subprocess.check_call([sys.executable, "-m", "pip", "install", tmp])
