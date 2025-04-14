import os
import hashlib
from config import TARGET_FOLDER

def file_hash(path, chunk_size=8192):
    hasher = hashlib.md5()
    try:
        with open(path, "rb") as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Ошибка чтения {path}: {e}")
        return None

def find_duplicates(folder):
    print(f"\n🔍 Ищем дубликаты в: {folder}\n")

    hashes = {}
    duplicates = {}

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            h = file_hash(path)
            if h:
                if h in hashes:
                    duplicates.setdefault(h, []).append(path)
                    duplicates[h].append(hashes[h])
                else:
                    hashes[h] = path

    for h in duplicates:
        duplicates[h] = list(set(duplicates[h]))

    return duplicates

def print_duplicates(duplicates):
    if not duplicates:
        print("✅ Дубликатов не найдено!")
    else:
        print("⚠️ Найдены дубликаты:\n")
        for i, (h, paths) in enumerate(duplicates.items(), 1):
            print(f"[{i}] Хэш: {h}")
            for path in paths:
                print(f"  - {path}")
            print()
