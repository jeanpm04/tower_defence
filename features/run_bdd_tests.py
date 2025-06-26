import os
import subprocess

# Ruta a la carpeta de features BDD
bdd_features_path = os.path.join("features", "bdd")

# Comando behave limitado solo a esa carpeta
command = f"behave {bdd_features_path}"

# Ejecutar comando
subprocess.run(command, shell=True)
