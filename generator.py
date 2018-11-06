import shutil
import os
import minotaur
import random

def CreateDirsFiles():

    possib = ["Include","Deadlock"]
    startdir = os.getcwd()

    if os.path.isdir(os.path.join(startdir, "root")):
        shutil.rmtree(os.path.join(startdir, "root"))

    os.mkdir(os.path.join(startdir, "root"))
    os.chdir(os.path.join(startdir, "root"))
    nextdir = os.path.join(startdir, "root")

    lenchain = random.randint(1, 8)
    chain = []
    notchain = []

    nextfile = ""
    for i in range(lenchain):
        if i == 0:
            nextfile = "file.txt"

        includes = random.randint(1, 4)
        Minotaur = random.randint(1, includes)
        current = nextfile

        for j in range(includes):
                num = "file{}.txt".format(str(random.randint(0, 3000)))
                while num in chain or num in notchain:
                    num = "file{}.txt".format(str(random.randint(0, 3000)))

                with open(os.path.join(nextdir, current), "a+") as inf:
                    inf.write("@include {}\n".format(num))

                if j == Minotaur-1:
                    nextfile = num
                    chain.append(num)

                else:
                    notchain.append(num)

    with open(os.path.join(nextdir, nextfile), "a+") as inf:
        inf.write("Minotaur")

    for i in notchain:
        if random.choice(possib) == "Include":
            includes = random.randint(1, 3)

            for j in range(includes):
                num = "file{}.txt".format(str(random.randint(0, 3000)))

                while num in notchain or num in chain:
                    num = "file{}.txt".format(str(random.randint(0, 3000)))

            with open(os.path.join(nextdir, i), "a+") as inf:
                inf.write("@include {}\n".format(num))
                notchain.append(num)

        else:
            with open(os.path.join(nextdir, i), "a+") as inf:
                inf.write("Deadlock")

    count = 0
    flag = False
    all_dirs = 0
    dirs = random.randint(1,4)
    filelist = chain + notchain + ["file.txt"]
    files = len(chain)*dirs//len(filelist)

    if files == 0:
        files = 2*len(filelist)//(len(chain)*dirs)

    for i in range(len(chain)):
        dir = "dir_" + str(all_dirs)
        nextdir = os.path.join(nextdir, dir)
        os.mkdir(nextdir)
        os.chdir(nextdir)
        all_dirs += 1

        for i in range(dirs):
            os.mkdir(os.path.join(nextdir, "dir{}".format(str(all_dirs))))
            os.chdir(os.path.join(nextdir, "dir{}".format(str(all_dirs))))
            all_dirs += 1

            for i in range(files):
                if count == len(chain)+len(notchain)+1:
                    flag = True
                    break
                if not os.path.isfile(os.path.join(startdir, "root", filelist[count])):
                    filelist.remove(filelist[count])
                shutil.move(os.path.join(startdir, "root", filelist[count]), os.path.join(nextdir, "dir{}".format(str(all_dirs-1))))
                count += 1

            if flag == True:
                break

        if flag == True:
            break

    os.chdir(startdir)

if __name__ == "__main__":
    CreateDirsFiles()
    minotaur.ShowPath()
