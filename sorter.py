import os
import shutil
from config import TARGET_FOLDER, CATEGORIES

def get_category(extension: str):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Other"

def organize_files(folder):
    print(f"\n📦 Сканируем папку: {folder}\n")

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1]
            category = get_category(ext)

            target_dir = os.path.join(folder, category)
            os.makedirs(target_dir, exist_ok=True)

            new_path = os.path.join(target_dir, filename)
            try:
                shutil.move(filepath, new_path)
                print(f"✅ Перемещён: {filename} → {category}")
            except Exception as e:
                print(f"❌ Ошибка с файлом {filename}: {e}")

    print("\n🧼 Уборка завершена!")
