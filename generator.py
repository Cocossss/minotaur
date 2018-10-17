import shutil
import os

def CreateDirsFiles(startdir):
    nextdir = startdir
    os.chdir(startdir)
    all_dirs = 0
    all_files = 0

    for i in range(subdirs):
        dir = "dir_" + str(all_dirs)
        nextdir = nextdir + "/" + dir
        os.mkdir(nextdir)
        os.chdir(nextdir)
        all_dirs = all_dirs + 1

        for i in range(dirs):
            os.mkdir(nextdir + "/" + "dir" + str(all_dirs))
            os.chdir(nextdir + "/" + "dir" + str(all_dirs))
            all_dirs = all_dirs + 1

            for j in range(files):
                file = "file" + str(all_files) + ".txt"
                all_files = all_files + 1
                f = open(file, "w")
                f.close()

            os.chdir(nextdir)

    return all_dirs, all_files


def FillFiles(startdir, test):
    list = []

    if not os.path.exists(startdir + "/Tests/input_file" + test + ".txt"):
        print("file " + startdir + "/Tests/input_file" + test + ".txt " + "doesn't exist!\n")
        return

    with open(startdir + "/Tests/input_file" + test + ".txt", "r") as inf:
        for line in inf:
            list.append(line.strip())

    for i in range(len(list)-1):
        if os.path.isfile(startdir + "/root"  + list[i]):
            with open(startdir + "/root"  + list[i], "a") as inf:
                while not os.path.isfile(startdir + "/root"  + list[i+1]):
                    inf.write(list[i+1] + "\n")
                    i = i + 1

                    if i == len(list) - 1:
                        break

startdir = os.getcwd()

if os.path.isdir(startdir + "/root"):
    shutil.rmtree(startdir + "/root")

os.mkdir(startdir + "/root")
os.chdir(startdir + "/root")

print("Hello! This is files and directories maker.")
print("\nEnter number of files in dirs: ", end = "")
files = int(input())

print("\nEnter number of subdirs: ", end ="")
subdirs = int(input())

print("\nEnter number of dirs in subdirs: ", end = "")
dirs = int(input())

if subdirs <= 0 or dirs <= 0 or files <= 0:
    print("Wrong input!\n")
    exit()

print("\n\nCreating dirs and files...\n")
dnum, fnum = CreateDirsFiles(startdir + "/root")

print("Enter number of file, that will begin search (note: number must be >= 0 and <=", fnum-1, "): ", end = "")
startfile = int(input())

if not (startfile >= 0 and startfile <= fnum-1):
    print("number must be >= 0 and <=", fnum-1, "\nTry again\n")
    exit()

flag = False
for address, dirs, files in os.walk(startdir):
    for file in files:
        if file == "file" + str(startfile) + ".txt":
            os.rename(address + "/"  + "file" + str(startfile) + ".txt", address + "/"  + "file.txt")
            flag = True
            break
    if flag == True:
        break

print("\nEnter number of test: ", end = "")
test = input()

print(test)
print("\n\nFilling files with data...\n")
FillFiles(startdir, test)
