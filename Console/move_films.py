import os

dirs = []


folders = []
mypath = '/media/napalm/HardDrive/Movies/Arthouse/'
for (dirpath, dirnames, filenames) in os.walk(mypath):
    folders.append(dirnames)
    break
print(folders)

def change_name(folders):
    for old_folder in folders[0]:
        if '\u200b' in old_folder:
            new_folder = old_folder.replace('\u200b', '')
            os.replace(mypath + old_folder, mypath + new_folder)
            print(new_folder)
        else:
            print("PASSED")
#change_name(folders)

def divide_centuries(folders):
    for folder in folders[0]:
        if "19" in folder:
            os.replace(mypath + folder, mypath + '20th Century/' + folder)
        elif "20" in folder:
            os.replace(mypath + folder, mypath + '21st Century/' + folder)
        else:
            print("passed")

def add_brackets(folders):
    for old_folder in folders[0]:
        if '(' not in old_folder:
            print(old_folder)
            new_folder = old_folder.replace(" 20", " (20") + ")"
            print(new_folder)
            os.replace(mypath + old_folder, mypath + new_folder)

#add_brackets(folders)
