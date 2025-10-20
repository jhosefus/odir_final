class DiagnosisEncoder:
    """
    Codifica diagnósticos multiclase en estructuras útiles para el modelo.

    Métodos:
        encode(diagnosis: str) -> Tuple[Dict[str, int], List[int], str]
            Convierte un string de diagnóstico en:
            - Diccionario de etiquetas binarias
            - Vector target como lista
            - Etiqueta principal (primer letra)
    """

    def encode(self, diagnosis):
        """
        Codifica el diagnóstico en estructuras útiles para el modelo.

        Args:
            diagnosis (str): Diagnóstico como cadena (ej. "DG")

        Returns:
            Tuple:
                - binary_labels (dict): {'D': 1, 'G': 1, ...}
                - target_vector (list): [0,1,1,0,0,0,0,0]
                - primer_label (str): 'D'
        """
        valid_labels = "NDGCAHMO"
        diagnosis = diagnosis.upper().strip().replace(" ", "")
        binary_labels = {label: int(label in diagnosis) for label in valid_labels}
        target_vector = [binary_labels[label] for label in valid_labels]
        primer_label = diagnosis[0] if diagnosis else "N"
        return binary_labels, target_vector, primer_label