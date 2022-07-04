
from ast import Break
import os
import sys
import subprocess

#this command line interface is only for windows
#this particular code assumes there are spaces in between the inputs and the inputs should only be lowercase 
#the supporting commands are CD, clr, dir, environ, echo, help, pause and quit
#implementation done assuming single spaces
#implementation done assuming commands start without spaces

all_commands = ['cd','clr','dir','environ','echo','help','pause','quit']
main_directory = "C:/Users/rbaner15"
print(main_directory,">",end="")


#the fucntions are listed below
def fun_cd():
    if cmd_test[0] == 'cd':
        if os.path.isdir(cmd_test[1]):
            os.chdir(cmd_test[1])
        else:
            print('Directory Invalid')
            sys.exit()
    print(os.getcwd())

def fun_clear():
    if cmd_test[0] =='clr':
        os.system('cls')

def fun_echo():
    
    if cmd_test[0]== "echo" and cmd_test[1] !=">" and cmd_test[1]!=">>":
        for i in range(1, len(cmd_test)):
            print(i)
    elif len(cmd_test)>2 and cmd_test[1]==">":
        string1 = ""
        fpp=open(cmd_test[2],'w')
        for i in range(3, len(cmd_test)):
            string1 = string1+" " +cmd_test[i]
        print(string1.strip(),file=fpp)
        fpp.close()
    elif len(cmd_test)>2 and cmd_test[1]==">>":
        string2 = ""
        fpp=open(cmd_test[2],'a')
        for i in range(3, len(cmd_test)):
            string2 = string2+" " +cmd_test[i]
        print(string2.strip(),file=fpp)
        fpp.close()

def fun_environ():
    if cmd_test[0]=="environ" and len(cmd_test)>1:
        if cmd_test[1]==">":
            fpp=open("outputfile_environ.txt",'w')
            fpp.write(str(os.environ()))
            fpp.close()
        elif cmd_test[1]==">>":
            fpp=open("outputfile_environ.txt",'a')
            fpp.write(str(os.environ()))
            fpp.close()

    if cmd_test[0]=="environ" and len(cmd_test)==1:
        print(os.environ())

def fun_pause():
    if cmd_test[0]=="pause":
        os.system("pause")

def fun_dir():
    if len(cmd_test)==2:
        print(os.listdir(cmd_test[1]))
        
    else:
        if cmd_test[0]=='dir' and len(cmd_test)>2:
            if cmd_test[1]==">" :
                fpp=open("outputfile_dir.txt",'w')
                fpp.write(str(os.listdir(cmd_test[2])))
                fpp.close()
                
            
            elif cmd_test[1]==">>":
                fpp=open("outputfile_dir.txt",'a')
                fpp.write(str(os.listdir(cmd_test[2])))
                fpp.close()
        

def fun_help():
    if len(cmd_test)==1:
        subprocess.Popen('notepad outputfile.txt')
        fpp= open("outputfile.txt",'r')
        fpp.read()
        fpp.close()
        
    if len(cmd_test)>1 and cmd_test[1]==">":
        fpp=open(cmd_test[2],'w')
        fpp.write(str(cmd_test[3]))
        fpp.close()
    if len(cmd_test)>1 and cmd_test[1]==">>":
        fpp= open(cmd_test[2], 'a')
        fpp.write(str(cmd_test[3]))
        fpp.close()

def fun_quit():
    if cmd_test[0]=="quit":
        sys.exit()

while True:
    print("Please enter your command below")
    input_user = input(os.getcwd() + ">")
    cmd_test = input_user.split(" ") #spliting on basis of single whitespace
    
    if cmd_test[0] == "dir":
        fun_dir()
    elif cmd_test[0] == "clr":
        fun_clear()
    elif cmd_test[0] =="pause":
        fun_pause() 
    elif cmd_test[0] =="cd":
        fun_cd()
    elif cmd_test[0] =="environ":
        fun_environ()
    elif cmd_test[0] =="echo":
        fun_echo()
    elif cmd_test[0] =="help":
        fun_help()
    elif cmd_test[0] == "quit":
        fun_quit()
    else:
        print("Sorry This cannot be identified as any internal or external command")
        



