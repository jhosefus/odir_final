import pandas as pd

class MetadataHandler:
    """Carga, guarda y actualiza el CSV de metadatos."""

    def __init__(self, csv_path):
        self.csv_path = csv_path

    def load(self):
        try:
            df = pd.read_csv(self.csv_path)
            print(f"CSV cargado con {len(df)} registros.")
            return df
        except Exception as e:
            print(f"Error al cargar CSV: {e}")
            return pd.DataFrame()

    def save(self, df):
        try:
            df.to_csv(self.csv_path, index=False)
            print(f"CSV guardado en: {self.csv_path}")
        except Exception as e:
            print(f"Error al guardar CSV: {e}")

    def append(self, df, entry):
        return pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
