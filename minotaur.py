import os

def GetFilePath(startdir, filename):
    folder = []

    for i in os.walk(startdir):
        folder.append(i)

    is_exist = False
    for root, dir, files in folder:
        for file in files:
            if file == filename:
                is_exist = True
                print(os.path.join(root, file))

                with open(os.path.join(root, file)) as inf:
                    for line in inf:
                        line = line.strip()
                        if line == "Minotaur":
                            return 1;
                        elif line == "Deadlock":
                            return 0
                        elif " " in line:
                            include, nextfile = line.split()

                            if include == "@include":
                                if GetFilePath(startdir, nextfile) == 1:
                                    return 1
                            else:
                                print("file '{}' has wrong content: {}". format(filename, line))
                                return 0
                        else:
                            print("file '{}' has wrong content: {}". format(filename, line))
                            return 0

    if is_exist == False:
        print("file ", filename, "doesn't exist!")
        return

def ShowPath():

    startdir = os.getcwd()
    if not os.path.isdir(os.path.join(startdir, "root")):
        print("directory root doesn't exist!\n")
    elif not os.listdir(os.path.join(startdir, "root")):
        print("directory root is empty!\n")
    else:
        GetFilePath(os.path.join(startdir, "root"), "file.txt")

if __name__ == "__main__":
    ShowPath()
