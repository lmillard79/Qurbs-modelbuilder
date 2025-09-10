import os
import zipfile

def zip_directory(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Exclude __pycache__ directories
            dirs[:] = [d for d in dirs if d != '__pycache__']
            for file in files:
                if '__pycache__' not in file:
                    file_path = os.path.join(root, file)
                    # Include the root folder in the archive name
                    arcname = os.path.relpath(file_path, os.path.dirname(source_dir))
                    zipf.write(file_path, arcname)

source_directory = 'runoff_model'
output_zip = 'runoff_model.zip'

zip_directory(source_directory, output_zip)
print(f"Zipped {source_directory} into {output_zip}, including the root folder.")