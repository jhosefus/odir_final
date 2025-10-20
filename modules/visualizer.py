import matplotlib.pyplot as plt
from PIL import Image
import os

class Visualizer:
    """Muestra imágenes y metadatos por ID."""

    def show_image(self, path, title):
        if os.path.isfile(path):
            try:
                img = Image.open(path)
                plt.imshow(img)
                plt.title(title)
                plt.axis("off")
                plt.show()
            except Exception as e:
                print(f"Error al mostrar imagen: {e}")
        else:
            print("Imagen no encontrada.")

    def show_metadata(self, df, id_value):
        registros = df[df["ID"] == str(id_value)]
        if registros.empty:
            print("No se encontró ningún registro.")
            return

        for _, fila in registros.iterrows():
            print(f"\nImagen: {fila['filename']}")
            print(f"Ruta: {fila['filepath']}")
            print(f"Edad: {fila['Patient Age']}")
            print(f"Sexo: {fila['Patient Sex']}")
            print(f"Diagnóstico: {fila['Diagnosis']}")
            print(f"Label: {fila['labels']}")
            print(f"Target: {fila['target']}")
            for label in "NDGCAHMO":
                print(f"  {label}: {fila.get(label, 'No disponible')}")
            self.show_image(fila["filepath"], f"{id_value} - {fila['filename']}")