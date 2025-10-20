import os

class ImageHandler:
    """Manejo físico de imágenes: carga, eliminación y rutas."""

    def __init__(self, image_dir):
        self.image_dir = image_dir

    def build_path(self, filename):
        return os.path.join(self.image_dir, filename)

    def upload(self, id_value, eye):
        filename = f"{id_value}_{eye}.jpg"
        path = self.build_path(filename)
        input(f"Coloque la imagen '{filename}' en la carpeta y presione Enter para continuar...")
        return filename if os.path.isfile(path) else None

    def delete(self, path):
        if path and os.path.isfile(path):
            try:
                os.remove(path)
                print(f"Archivo eliminado: {path}")
            except Exception as e:
                print(f"No se pudo eliminar {path}: {e}")