# Print list of files and directories
import os

def file_list(dir):
    subdir_list = []
    for item in os.listdir(dir):
        fullpath = os.path.join(dir,item)
        if os.path.isdir(fullpath):
            subdir_list.append(fullpath)
        else:
            print(fullpath)

    for d in subdir_list:
        file_list(d)

file_list('D:\Workspace\test\PythonProject')
