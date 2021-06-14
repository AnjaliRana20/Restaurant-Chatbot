import os
import platform

# virtual environment setup and rasa installation

if platform.system() == 'Linux':
  os.system('python3 -m pip install virtualenv')
  os.system('mkdir python-virtual-environments && cd python-virtual-environments')
  os.system('python3 -m venv ./myvenv')
  os.system('source ./myvenv/bin/activate; pip3 install --upgrade pip setuptools wheel')
  os.system('source ./myvenv/bin/activate; pip install -r rasa')
else:
  print("Your operating system is nt compatible. Use LINUX-type OS.")