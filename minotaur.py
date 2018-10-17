import os

startdir = os.getcwd()

def GetFilePath(startdir, filename):
    folder = []

    for i in os.walk(startdir):
        folder.append(i)

    is_exist = False
    for root, dir, files in folder:
        for file in files:
            if file == filename:
                is_exist = True
                print(root+"/"+file)

                with open(root+"/"+file) as inf:
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


print("Getting Minotaur...")
GetFilePath(startdir, "file.txt")
