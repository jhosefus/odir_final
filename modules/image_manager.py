from modules.metadata_handler import MetadataHandler
from modules.image_handler import ImageHandler
from modules.diagnosis_encoder import DiagnosisEncoder
from modules.id_manager import IDManager
from modules.visualizer import Visualizer
from modules.validator import Validator

class ImageManager:
    def __init__(self, csv_path, image_dir):
        self.metadata = MetadataHandler(csv_path)
        self.image_handler = ImageHandler(image_dir)
        self.encoder = DiagnosisEncoder()
        self.id_manager = IDManager()
        self.visualizer = Visualizer()
        self.validator = Validator()
        self.df = self.metadata.load()

    def register_image(self):
        # Interacción por terminal
        id_value = self.id_manager.get_next_id(self.df)
        print(f"ID generado: {id_value}")
        age = input("Edad: ")
        sex = self.validator.validate_sex()
        left_keywords = input("Diagnóstico izquierdo: ")
        right_keywords = input("Diagnóstico derecho: ")
        diagnosis = self.validator.validate_diagnosis()

        binary_labels, target_vector, label = self.encoder.encode(diagnosis)
        left_file = self.image_handler.upload(id_value, "left")
        right_file = self.image_handler.upload(id_value, "right")

        # Crear registros
        for file in [left_file, right_file]:
            if file:
                entry = {
                    "ID": id_value,
                    "Patient Age": age,
                    "Patient Sex": sex,
                    "Left-Diagnostic Keywords": left_keywords,
                    "Right-Diagnostic Keywords": right_keywords,
                    "Diagnosis": diagnosis,
                    "labels": label,
                    "target": str(target_vector),
                    "filename": file,
                    "filepath": self.image_handler.build_path(file)
                }
                entry.update(binary_labels)
                self.df = self.metadata.append(self.df, entry)

        self.metadata.save(self.df)
        print("Registro completado.")
