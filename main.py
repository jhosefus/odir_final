from modules.image_manager import ImageManager

CSV_PATH = "files/full_df.csv"
IMAGE_DIR = "dataset"

def main():
    manager = ImageManager(CSV_PATH, IMAGE_DIR)

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar imagen")
        print("2. Modificar metadatos")
        print("3. Eliminar imagen")
        print("4. Ver resumen por ID")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            manager.register_image()
        elif opcion == "2":
            manager.modify_image()
        elif opcion == "3":
            manager.delete_image()
        elif opcion == "4":
            manager.ver_resumen_imagen()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
