import os
cwd = os.getcwd()
print(cwd)

# Create a folder
#os.mkdir('FolderA')
#os.mkdir('FolderA/FolderB')

#os.makedirs('SubA/SubB/SubC')
#os.rmdir('FolderA/FolderB')
#os.removedirs('SubA/SubB/SubC')
for file in os.listdir("."):
    print(file)