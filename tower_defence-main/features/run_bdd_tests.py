import os
import sys
import subprocess

# Añadir 'tower_defence' al PYTHONPATH para permitir imports como tower_defence.src.wave_manager
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tower_defence')))

# Ruta a la carpeta de features BDD
bdd_features_path = os.path.join("features", "bdd")

# Comando behave limitado solo a esa carpeta
command = f"behave {bdd_features_path}"

# Ejecutar el comando
subprocess.run(command, shell=True)
