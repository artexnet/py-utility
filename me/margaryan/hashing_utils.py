__author__ = 'arthur'

import hashlib


BLOCK_SIZE = 65536


# calculates MD5 hash for input string and returns as hex
def hash_md5(_str):
    _hash = hashlib.md5(_str)
    return _hash.hexdigest()


# calculates SHA1 hash for input string and returns as hex
def hash_sha1(_str):
    _hash = hashlib.sha1(_str)
    return _hash.hexdigest()


# calculates SHA256 hash for input string and returns as hex
def hash_sha256(_str):
    _hash = hashlib.sha256(_str)
    return _hash.hexdigest()


# calculates SHA512 hash for input string and returns as hex
def hash_sha512(_str):
    _hash = hashlib.sha512(_str)
    return _hash.hexdigest()


# calculates MD5 hash for input file and returns as hex
def hash_file_md5(_file):
    _hash = hashlib.md5()
    with open(_file, 'rb') as aFile:
        buf = aFile.read()
        _hash.update(buf)
    return _hash.hexdigest()


# calculates SHA1 hash for input file and returns as hex
def hash_file_sha1(_file):
    _hash = hashlib.sha1()
    with open(_file, 'rb') as aFile:
        buf = aFile.read()
        _hash.update(buf)
    return _hash.hexdigest()


# calculates SHA256 hash for input file and returns as hex
def hash_file_sha256(_file):
    _hash = hashlib.sha256()
    with open(_file, 'rb') as aFile:
        buf = aFile.read()
        _hash.update(buf)
    return _hash.hexdigest()


# calculates SHA512 hash for input file and returns as hex
def hash_file_sha512(_file):
    _hash = hashlib.sha512()
    with open(_file, 'rb') as aFile:
        buf = aFile.read()
        _hash.update(buf)
    return _hash.hexdigest()


# calculates MD5 hash for the large input file and returns as hex
def hash_large_file_md5(_file):
    _hash = hashlib.md5()
    with open(_file, 'rb') as aFile:
        buf = aFile.read(BLOCK_SIZE)
        while len(buf) > 0:
            _hash.update(buf)
            buf = aFile.read(BLOCK_SIZE)
    return _hash.hexdigest()


# calculates SHA1 hash for the large input file and returns as hex
def hash_large_file_sha1(_file):
    _hash = hashlib.sha1()
    with open(_file, 'rb') as aFile:
        buf = aFile.read(BLOCK_SIZE)
        while len(buf) > 0:
            _hash.update(buf)
            buf = aFile.read(BLOCK_SIZE)
    return _hash.hexdigest()


# calculates SHA256 hash for the large input file and returns as hex
def hash_large_file_sha256(_file):
    _hash = hashlib.sha256()
    with open(_file, 'rb') as aFile:
        buf = aFile.read(BLOCK_SIZE)
        while len(buf) > 0:
            _hash.update(buf)
            buf = aFile.read(BLOCK_SIZE)
    return _hash.hexdigest()


# calculates SHA512 hash for the large input file and returns as hex
def hash_large_file_sha512(_file):
    _hash = hashlib.sha512()
    with open(_file, 'rb') as aFile:
        buf = aFile.read(BLOCK_SIZE)
        while len(buf) > 0:
            _hash.update(buf)
            buf = aFile.read(BLOCK_SIZE)
    return _hash.hexdigest()