import os
import shutil

for root, dirs, files in os.walk('papers/'):
    for f in files:
        if f.endswith(".pdf"):
            fname = f.replace('-', '')
            fname = fname[:3] + '-' + fname[3:]
            print(os.path.join(root, f), os.path.join(root, fname))
            shutil.copyfile(os.path.join(root, f), os.path.join(root, fname))
