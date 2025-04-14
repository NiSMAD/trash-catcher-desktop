from sorter import organize_files
from duplicates import find_duplicates, print_duplicates
from config import TARGET_FOLDER

def main_menu():
    while True:
        print("\n=== ClutterCatcher ===")
        print("1. 📂 Сортировать файлы")
        print("2. 🔍 Найти дубликаты")
        print("3. 🔄 Всё сразу")
        print("4. 🚪 Выход")
        choice = input("Выберите действие (1–4): ").strip()

        if choice == "1":
            organize_files(TARGET_FOLDER)
        elif choice == "2":
            dups = find_duplicates(TARGET_FOLDER)
            print_duplicates(dups)
        elif choice == "3":
            organize_files(TARGET_FOLDER)
            dups = find_duplicates(TARGET_FOLDER)
            print_duplicates(dups)
        elif choice == "4":
            print("👋 До скорого!")
            break
        else:
            print("⚠️ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
