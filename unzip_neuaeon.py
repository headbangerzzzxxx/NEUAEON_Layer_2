import zipfile
import os

zip_path = 'neuaeon.zip'
extract_dir = 'neuaeon_unzipped'

if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print(f'Extracted {zip_path} to {extract_dir}')
