import time
import sys
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
print("\n\n\t")
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
delay_print
delay_print (""+O+" db    db d888888b d8888b. db    db .d8888. "+B+"  db    db\n")
delay_print (""+O+" 88    88   `88'   88  `8D 88    88 88'  YP "+B+"  `8b  d8'\n")
delay_print (""+O+" Y8    8P    88    88oobY' 88    88 `8bo.   "+B+"   `8bd8' \n")
delay_print (""+O+" `8b  d8'    88    88`8b   88    88   `Y8b. "+B+"   .dPYb.  \n")
delay_print (""+O+"  `8bd8'    .88.   88 `88. 88b  d88 db   8D "+B+"  .8P  Y8. \n")
delay_print (""+O+"   YP    Y888888P 88   YD ~Y8888P' `8888Y'  "+B+" YP    YP "+R+"v1\n")


print('\n\n\t---file booster---\n')
print('\t\tcreated by:: waccub@gmail.com\n\n')

#####

limit=int(input("how many file you want to create:\n>>"))
strin=input("write something in file:\n>>")
ran=int(input("how many line you want to create:\n>>"))
print('\n')

#####

n=1
for j in range(1,limit+1):
    with open(f"file{j}.txt",'w',encoding='utf-8') as f:
        print(f"file has created--{n}")
        n+=1
        for i in range(1,ran+1):
            f.write(strin+f' {i}\n')

#####
print('\n\nsuccessfully created file.\n\thappy hacking...\n\n')
