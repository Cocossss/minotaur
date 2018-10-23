import shutil
import os
import minotaur

def CreateDirsFiles():

    startdir = os.getcwd()

    if os.path.isdir(os.path.join(startdir, "root")):
        shutil.rmtree(os.path.join(startdir, "root"))

    os.mkdir(os.path.join(startdir, "root"))
    os.chdir(os.path.join(startdir, "root"))
    nextdir = os.path.join(startdir, "root")

    print("Hello! This is files and directories maker.")
    print("\nEnter number of files in dirs: ", end = "")
    files = int(input())

    print("\nEnter number of subdirs: ", end ="")
    subdirs = int(input())

    print("\nEnter number of dirs in subdirs: ", end = "")
    dirs = int(input())

    if subdirs <= 0 or dirs <= 0 or files <= 0 or files > 3000:
        print("Wrong input!\n")
        exit()

    print("\n\nCreating dirs and files...\n")

    all_dirs = 0
    all_files = 0

    for i in range(subdirs):
        dir = "dir_" + str(all_dirs)
        nextdir = os.path.join(nextdir, dir)
        os.mkdir(nextdir)
        os.chdir(nextdir)
        all_dirs += 1

        for i in range(dirs):
            os.mkdir(os.path.join(nextdir, "{}{}".format("dir", str(all_dirs))))
            os.chdir(os.path.join(nextdir, "{}{}".format("dir", str(all_dirs))))
            all_dirs += 1

            for j in range(files):
                file = "{}{}{}".format("file", str(all_files), ".txt")
                all_files += 1
                f = open(file, "w")
                f.close()

            os.chdir(nextdir)

    return all_dirs, all_files, startdir


def FillFiles(startdir, test):
    list = []

    if not os.path.exists(os.path.join(startdir, "Tests", "{}{}{}".format("input_file", test, ".txt"))):
        print("{}{}{}\n". format("file ", os.path.join(startdir, "Tests", "input_file" + test + ".txt "), "doesn't exist!"))
        return

    with open(os.path.join(startdir, "Tests", "{}{}{}".format("input_file", test, ".txt")), "r") as inf:
        for line in inf:
            list.append(line.strip())

    for i in range(len(list)-1):
        if os.path.isfile(os.path.join(startdir, "root") + list[i]):
            with open(os.path.join(startdir, "root")  + list[i], "a") as inf:
                while not os.path.isfile(os.path.join(startdir, "root")  + list[i+1]):
                    inf.write(list[i+1] + "\n")
                    i = i + 1

                    if i == len(list) - 1:
                        break

def generate():

    dnum, fnum, startdir = CreateDirsFiles()

    print("Enter number of file, that will begin search (note: number must be >= 0 and <=", fnum-1, "): ", end = "")
    startfile = int(input())

    if not (startfile >= 0 and startfile <= fnum-1):
        print("number must be >= 0 and <=", fnum-1, "\nTry again\n")
        exit()

    flag = False
    startwalk = startdir
    for address, dirs, files in os.walk(startwalk):
        for file in files:
            if file == "file" + str(startfile) + ".txt":
                os.rename(os.path.join(address, "{}{}{}".format("file", str(startfile), ".txt")), os.path.join(address, "file.txt"))
                flag = True
                break
        if flag == True:
            break

    os.chdir(startdir)
    print("\nEnter number of test (test file must exist): ", end = "")
    test = input()

    print("\n\nFilling files with data...\n")
    FillFiles(startdir, test)

if __name__ == "__main__":
    generate()
    minotaur.ShowPath()
