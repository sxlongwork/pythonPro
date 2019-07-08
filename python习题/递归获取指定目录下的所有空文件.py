import os


def get_empty_file(dirpath):
    file_list = []
    if os.path.exists(dirpath):
        file_list = os.listdir(dirpath)
        for f in file_list:
            full_Path = os.path.join(dirpath, f)
            if os.path.isdir(full_Path):
                get_empty_file(full_Path)
            else:
                if os.path.getsize(full_Path) == 0:
                    print(full_Path)
    else:
        print("{} is not exsit in system.".format(dirpath))


path = input("pls input a directory:")
get_empty_file(path)