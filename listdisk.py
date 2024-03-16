import os

def makelistdisk():
 res=os.system('fdisk -l')
 return res
