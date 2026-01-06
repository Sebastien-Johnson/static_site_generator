import os
import shutil

#recursive function that copies contents from source directory to destination directory (static to public)
#clear (delete and remake) public directory
#copy all files, subdirectories, nested files etc

old_paths = []

def clear_dir(source_dir, dest_dir):
    #copies old path
    old_paths.append(dest_dir)
    #clears old path
    shutil.rmtree(dest_dir)
    #makes new dir at old path
    os.mkdir(dest_dir)
    refill_dir(source_dir, dest_dir)


def refill_dir(source_path, dest_path):
    entries = os.listdir(source_path)
    for entry in entries:
        new_dest = os.path.join(dest_path, entry)
        new_source = os.path.join(source_path, entry)
        if os.path.isfile(new_source):
            shutil.copy(new_source, dest_path)
        else:
            os.mkdir(new_dest)
            refill_dir(new_source, new_dest)
    
    return