import os

def count_files(myDir):
    file_count = sum(len(files) for _, _, files in os.walk(myDir))
    return file_count

dir_all = '/home/napalm/Documents/Film Torrents'
dir_done = '/home/napalm/Documents/Film Torrents/Done'

p = round(100 * (count_files(dir_done) / count_files(dir_all)), 2)
print("Completed Torrents: {}%".format(p))

