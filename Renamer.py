import sys
import os
from PIL import Image
import re


def atoi(text):
    if text.isdigit():
        return int(text)


def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]


def extension():
    filenames = os.listdir()

    for i in range(len(filenames)):

        filename = filenames[i]

        if not filename.lower().endswith(".jpg"):
            os.remove(filenames[i])

            i -= 1


def deleting():
    filenames = os.listdir()

    for j in range(len(filenames)):

        filename = filenames[j]

        if filename.find("one_piece_") == -1:
            os.remove(filenames[j])

            j -= 1


def renaming():
    filenames = os.listdir()
    newlist = []
    z = 1

    for h in range(len(filenames)):

        newlist.append(filenames[h].split("one_piece_", 1)[1])

        if len(newlist) != len(set(newlist)):
            newlist[h] = newlist[h].split(".jpg", 1)[0] + f"_{z}.jpg"

            z += 1

        os.rename(filenames[h], newlist[h])


def imsize():
    filenames = os.listdir()
    newlist2 = []

    for m in range(len(filenames)):
        newlist2.append(filenames[m].split("_", 1)[1])
        os.rename(filenames[m], newlist2[m])


def part0():
    filenames = os.listdir()
    filenames.sort(key=natural_keys)

    pages = []

    for k in range(len(filenames)):

        try:

            image_size = Image.open(filenames[k])
            area = image_size.size[0] * image_size.size[1]
            pages.append([area])

        except:

            os.remove(filenames[k])

            k -= 1

    image_size.close()

    part0.pages = pages


def part1():
    filenames = os.listdir()
    filenames.sort(key=natural_keys)

    for l in range(1, len(filenames)):

        if not filenames[l][1].isdigit():

            if (filenames[l][0] == filenames[l - 1][0]

                    and part0.pages[l] >= part0.pages[l - 1]):
                os.remove(filenames[l - 1])

        else:

            if (filenames[l][0:2] == filenames[l - 1][0:2]

                    and part0.pages[l] >= part0.pages[l - 1]):
                os.remove(filenames[l - 1])


def part2():
    filenames = os.listdir()
    filenames.sort(key=natural_keys)

    for l in range(len(filenames) - 1):

        if not filenames[l][1].isdigit():

            if (filenames[l][0] == filenames[l + 1][0]

                    and part0.pages[l] >= part0.pages[l + 1]):
                os.remove(filenames[l + 1])

        else:

            if (filenames[l][0:2] == filenames[l + 1][0:2]

                    and part0.pages[l] >= part0.pages[l + 1]):
                os.remove(filenames[l + 1])


if __name__ == "__main__":

    if len(sys.argv) == 2:

        chapter_number = (sys.argv[1])
        directory = r"C:\Users\Jeremy\Downloads" + chr(92) + chapter_number
        os.chdir(directory)

        extension()
        deleting()
        renaming()
        imsize()
        part0()
        part1()
        part0()
        part2()

        print(f"Chapter {chapter_number} is ready to be read")

    else:

        print("Enter folder name")
