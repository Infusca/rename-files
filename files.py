import os
count = 0
files = []
# path = "F:\Smoke on Horizon\TurnKey-v2.1\images\wood_gallery"


print('Enter the full path name of the folder.')
path = input()

print ('Enter new name you want to name all the files (each file will be named "newName_1, newName_2, etc.")')
fileNameInput = input()

print('Enter file extentions you want included in the change, separated by a space.')
exts = input()
extList = []
extList = exts.split()

# check for correct file type extentions
for index, i in enumerate(extList):
    if not '.' in i:
        extList[index] = '.' + i

for file in os.listdir(path):
    old_name = path + '\\' + str(file)
    ext = os.path.splitext(file)[1]

    if ext in extList:
        if ext == '.jpeg':
            new_name = path + '\\' + fileNameInput + str(count) + '.jpeg'
        elif ext == '.jpg':
            new_name = path + '\\' + fileNameInput + str(count) + '.jpg'
        elif ext == '.gif':
            new_name = path + '\\' + fileNameInput + str(count) + '.gif'
        elif ext == '.txt':
            new_name = path + '\\' + fileNameInput + str(count) + '.txt'


        os.rename(old_name, new_name)
        count += 1












#
