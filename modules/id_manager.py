class IDManager:
    """Genera el próximo ID único basado en el CSV."""

    def get_next_id(self, df):
        if df.empty or "ID" not in df.columns:
            return "1"
        df["ID"] = df["ID"].astype(str)
        ids = [int(i) for i in df["ID"] if i.isdigit()]
        return str(max(ids) + 1) if ids else "1"