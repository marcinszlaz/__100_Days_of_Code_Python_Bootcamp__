import os
import subprocess

# tuple with list of directories to ignore
ignore_tuple = (".", "venv", "env", "__pycache__", "node_modules", "static", "build", "dist", "assets")

def generate_requirements(base_path):
    for root, dirs, files in os.walk(base_path):
        # Filtrowanie folderów na starcie - "Rzemieślnicza Zapora"
        # Modyfikujemy dirs w miejscu, żeby os.walk nie wchodził głębiej w śmieci
        dirs[:] = [d for d in dirs if not d.startswith(ignore_tuple)]


        for d in dirs:
            full_path = os.path.join(root, d)
            # Tworzymy ścieżkę do nowego pliku (np. requirements_new.txt)
            output_file = os.path.join(full_path, "requirements_new.txt")

            print(f"Mielę projekt: {d}...")

            # Twoja finalna komenda z subprocess
            try:
                subprocess.run(
                    [
                        "pipreqs",
                        full_path,
                        "--savepath", output_file,
                        "--force",      # Nadpisuje tylko jeśli plik docelowy istnieje
                        "--use-local"   # Szybsze, bo nie pyta serwerów PyPI
                    ],
                    capture_output=True,
                    text=True,
                    shell=False
                )
            except Exception as e:
                print(f"Błąd w {d}: {e}")

# Odpalenie w Twoim katalogu z projektami
# generate_requirements("ścieżka/do/twoich/projektów")