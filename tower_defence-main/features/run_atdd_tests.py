import os
import subprocess

# Ruta a los features ATDD
atdd_features_path = os.path.join("features", "atdd")

# Comando behave limitado a esa carpeta
command = f"behave {atdd_features_path}"

# Ejecutar comando
subprocess.run(command, shell=True)
