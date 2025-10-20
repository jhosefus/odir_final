class Validator:
    """Valida entradas del usuario por terminal."""

    def validate_sex(self):
        while True:
            sex = input("Sexo (M/F): ").strip().upper()
            if sex in ["M", "F"]:
                return "Male" if sex == "M" else "Female"
            print("Entrada inválida.")

    def validate_diagnosis(self):
        valid = set("NDGCAHMO")
        while True:
            diag = input("Diagnóstico (N, D, G, C, A, H, M, O): ").upper().strip().replace(" ", "")
            if diag and set(diag).issubset(valid):
                return diag
            print("Diagnóstico inválido.")