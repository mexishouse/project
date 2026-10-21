"""
Railway se dataset download karke local dataset/ folder mein daal deta hai.
Chalane ka tareeqa:  python sync_dataset.py
"""
import io
import os
import zipfile
import urllib.request

URL = "https://project-production-a6d6.up.railway.app/api/dataset_zip"
SYNC_KEY = "apni-secret-key-yahan-likho"   # Railway Variables mein SYNC_KEY ki same value

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

req = urllib.request.Request(f"{URL}?key={SYNC_KEY}")
with urllib.request.urlopen(req, timeout=120) as r:
    data = r.read()

os.makedirs(DATASET_DIR, exist_ok=True)
with zipfile.ZipFile(io.BytesIO(data)) as zf:
    zf.extractall(DATASET_DIR)
    print(f"Done! {len(zf.namelist())} images dataset folder mein aa gayi.")