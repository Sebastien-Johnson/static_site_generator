import os
import shutil

#recursive function that copies contents from source directory to destination directory (static to public)
#clear (delete and remake) public directory
#copy all files, subdirectories, nested files etc

public_path = "/home/sebas/workspace/github.com/sebastien-johnson/bdev-coursework/static_site_gen/static_site_generator/public"
source = "/home/sebas/workspace/github.com/sebastien-johnson/bdev-coursework/static_site_gen/static_site_generator/static"
old_paths = []

def clear_dir(path = public_path):
    #copies old path
    old_paths.append(path)
    #deletes old directory
    shutil.rmtree(path)
    #makes new dir at old path
    os.mkdir(path)
    refill_dir(source, path)


def refill_dir(source_path, dest_path):
    entries = os.listdir(source_path)
    for entry in entries:
        new_dest = os.path.join(dest_path, entry)
        new_source = os.path.join(source_path, entry)
        if os.path.isfile(new_source):
            shutil.copy(new_source, dest_path)
        else:
            os.mkdir(new_dest)
            refill_dir(new_source, new_dest )

    return
 