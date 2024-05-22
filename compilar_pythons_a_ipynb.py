import os
import nbformat as nbf

ruta = "ruta/al/directorio"

nb = nbf.v4.new_notebook()

for archivo in os.listdir(ruta):
    if archivo.endswith(".py"):
        ruta_archivo = os.path.join(ruta, archivo)
        with open(ruta_archivo, "r") as f:
            codigo = f.read()
            # Crear una nueva celda de código con el contenido del archivo
            codigo_celda = nbf.v4.new_code_cell(codigo)
            # Añadir la celda al notebook
            nb.cells.append(codigo_celda)

with open("notebook_compilada.ipynb", "w") as f:
    nbf.write(nb, f)

print("Notebook creado exitosamente: notebook_compilada.ipynb")


