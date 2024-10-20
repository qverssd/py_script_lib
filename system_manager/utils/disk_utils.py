import shutil

#Disk usage check
def check_disk_usage(path):
    usage = shutil.disk_usage(path)
    total = usage.total // (2**30)
    used = usage.used // (2**30)
    free = usage.free // (2**30)
    print(f"Disk: {path}")
    print(f"Total space: {total} GB")
    print(f"Used: {used} GB")
    print(f"Free: {free} GB")

#Copying files
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File {source} copied to  {destination}")
    except Exception as e:
        print(f"Error while file copied: {e}")