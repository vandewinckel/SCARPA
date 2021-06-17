import hashlib
import sys

def hash(file_path):
    BLOCK_SIZE = 65536

    file_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    return file_hash.hexdigest()