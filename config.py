import os

TARGET_FOLDER = os.path.join(os.path.expanduser("~"), "Desktop")

CATEGORIES = {
    "Изображения": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Документы": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Архивы": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Видео": [".mp4", ".avi", ".mkv", ".mov"],
    "Музыка": [".mp3", ".wav", ".flac"],
    "Скрипты": [".py", ".js", ".sh", ".bat"],
    "Остальное": [] 
}
