import os

# Obtener dirección de la carpeta donde se está.
ruta_base = os.getcwd()

# Recorre la carpeta principal y las subcarpetas
for raiz, carpetas, archivos in os.walk(ruta_base):
    for archivo in archivos:
        if archivo.lower().endswith(".docx"):
            ruta_completa = os.path.join(raiz, archivo)
            try:
                os.remove(ruta_completa)
                print(f"Eliminado: {ruta_completa}")
            except Exception as e:
                print(f"No se pudo eliminar {ruta_completa}: {e}")

print("Proceso completado.")