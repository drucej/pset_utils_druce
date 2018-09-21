import hashlib

def hash_str(some_val, salt=''):
    m = hashlib.sha256()
    m.update(some_val)

    if salt != None:
        m = [salt + m]

    return m
