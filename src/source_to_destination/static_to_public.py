import os
import shutil

#recursive function that copies contents from source directory to destination directory (static to public)
#clear (delete and remake) public directory
#copy all files, subdirectories, nested files etc

public_path = "/home/sebas/workspace/github.com/sebastien-johnson/BDev-Coursework/static_site_generator/public"
source = "/home/sebas/workspace/github.com/sebastien-johnson/BDev-Coursework/static_site_generator/static"
old_paths = []

def clear_dir(path = public_path):
    #copies old path
    old_paths.append(path)
    #clears old path
    shutil.rmtree(path)
    #makes new dir at old path
    new_dir = os.mkdir(path)
    #makes list of new file and directory NAMES (not paths)
    source_files = os.listdir(source)
    refill_dir(source_files, new_dir)


def refill_dir(source_files, new_dir):
    for file in source_files:
        full_path = os.path.join(file, source)
        if os.path.isfile(full_path):
            shutil.copy(f"{source}/{file}", new_dir)
        else:
            os.mkdir(f"{new_dir}/{file}")
            return shutil.copy(refill_dir((source), (f"{new_dir}/{file}")))
    