
nombre_archivo = "Siuuuuuuuu.txt"

contenido = "Este es el contenido que se escribirá en el archivo de texto."

with open(nombre_archivo, "w") as archivo:
    archivo.write(contenido)

print(f"Se ha creado el archivo '{nombre_archivo}' con el contenido deseado.")