import os
import zipfile

FOLDER_NAME = "AParadiseKiller (apworld)"

def zip_to_apworld():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, FOLDER_NAME)

    zip_path = os.path.join(script_dir, FOLDER_NAME + ".zip")
    apworld_path = os.path.join(script_dir, FOLDER_NAME + ".apworld")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, script_dir)
                zipf.write(full_path, arcname)

    if os.path.exists(apworld_path):
        os.remove(apworld_path)

    os.rename(zip_path, apworld_path)

    print(f"Created: {apworld_path}")

if __name__ == "__main__":
    zip_to_apworld()