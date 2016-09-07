import sys
from sort import *


def main():
    
    #typeflags -i = integer -s = string -si = string and integer
    #sortflas -a -d

    #make cmd flags
    typeflags = ["-i", "-s", "-si"]
    sortflags = ["-a", "-d"]
    openfile = sys.argv[1].lower()
    writefile = sys.argv[2].lower()
    typeflag = sys.argv[3].lower()
    sortflag = sys.argv[4].lower()
    
    #open file and create for write
    fr = open("{0}.txt".format(openfile),"r")
    fw = open("{0}.txt".format(writefile), "w")

    #make buf
    buf = []
    strBuf = []
    for line in fr:
        if line != "\n" and line != "":
            if isFloat(line):
                buf.append((int)(line.rstrip()))
            else:
                strBuf.append(line.rstrip())
    fr.close()
        
    #logic
    if typeflag in typeflags and sortflag in sortflags:
        
        if typeflag == "-i":
            buf = insertSort(buf)
        if typeflag == "-s":
            buf = insertSort(strBuf)
        if typeflag == "-si":
            buf = insertSort(buf) + insertSort(strBuf)      
    else:
        print("Error. Wrond flags")
        sys.exit()

    #reverse    
    if sortflag == "-d":
        buf = reversed(buf)
    
    print("Sorting complet")

    #write in file
    for index in buf:
        fw.write("{0} \n".format(index))
    fw.close()



if __name__ == '__main__':
    main()
    