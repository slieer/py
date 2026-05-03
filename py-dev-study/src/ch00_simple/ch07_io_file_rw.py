# -*- coding: utf-8 -*-
"""
Created on 2010-7-10
last modified 2012-10-07
@author: me
"""


def fileOp():
    poem = """\
            programming is fun
            When the works id done
            if you wana make your work also fun:
                use python !
        """

    f = open("poem.txt", "w")
    f.write(poem)
    f.close()

    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:  ### Zero length indicates EOF
            break
        print(line)
    f.close()


def fileOp1():
    try:
        f = open("xxx.txt")
        print(f.readline())
    except IOError as e:
        print("file not find")
        print(e)


import io


def fileOp2():
    filePath = (
        "/opt/workspace/py/py-dev-study/src/ch00_simple/ch07_io_file_persist_object.py"
    )
    textIoWraper = io.open(filePath, "r", encoding="utf-8")
    lines = textIoWraper.readlines()
    for line in lines:
        print(line)

    textIoWraper.close()


from pathlib import Path, PurePath

if __name__ == "__main__":
    # fileOp()
    fileOp()

    fileOp2()

    p = Path(".")
    for item in p.iterdir():
        print(item)

    p = PurePath("/etc")
    print(p / "init.d" / "apache2")
