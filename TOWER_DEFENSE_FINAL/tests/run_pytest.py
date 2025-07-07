import os
import sys
import subprocess

# Añadir 'tower_defence' al path para que los tests puedan importar desde tower_defence/src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'tower_defence')))

# Ejecutar pytest
subprocess.run(["pytest", "tests/"])
