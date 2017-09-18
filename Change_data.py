import re 
import os
import time,tkFileDialog
#path= r'C:\Users\Tony\data.txt'
path = tkFileDialog.askopenfilename(initialdir = 'C:\Users\Tony')
fin=open(path, "r")


t = os.path.getmtime(path)
print  time.localtime(t)
fout=open(r"C:\Users\Tony\New\data.txt","w")
for line in fin.readlines():
    line = line.replace(' the content need to change','.                   changed content')

    fout.write(line)
fin.close()
fout.close()
os.utime(r"C:\Users\Tony\New\data.txt", (t,t))
