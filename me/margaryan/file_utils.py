__author__ = 'arthur'

import fnmatch
import os
import shutil


# returns the list of files with specified extension in the given directory
def get_files_by_extension(target_dir, target_ext, show_full_path=False):
    result = []
    for root, dirnames, filenames in os.walk(target_dir):
        for filename in fnmatch.filter(filenames, '*' + target_ext):
            result.append(os.path.join(root, filename)) if show_full_path else result.append(filename)
    return result


# returns the data difference between 2 input files
def get_diff(filename1, filename2):
    with open(filename1) as text_one, open(filename2) as text_two:
        return set(text_one) ^ set(text_two)


# checks if specified directory exists
def dir_exists(dir_path):
    return os.path.isdir(dir_path)


# checks if specified file exists
def file_exists(file_path):
    return os.path.isfile(file_path)


# checks if specified file exists and user has read permission
def file_exists_and_readable(file_path):
    try:
        f = open(file_path, 'r')
        f.close()
    except IOError as e:
        print(e.message, e)
        return False
    return True


# checks if specified file exists and user has write permission
def file_exists_and_writable(file_path):
    try:
        f = open(file_path, 'w')
        f.close()
    except IOError as e:
        print(e.message, e)
        return False
    return True


# moves source file to specified destination
def move(src, dest):
    shutil.move(src, dest)


# deletes specified file
def delete(file_path):
    os.remove(file_path)


# makes a copy of input file in the specified location
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)


# makes a copy of large input file in the specified location
def copy_large_file(src, dest, buffer_size=16000):
    with open(src, 'rb') as f_src:
        with open(dest, 'wb') as f_dest:
            shutil.copyfileobj(f_src, f_dest, buffer_size)


# make a copy of the entire directory in the specified location
def copy_directory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)