import os
###########################################################
path = r'C:\Users\daule\Desktop\KBTU Faili'
os.chdir(path)

while (True):

    print ("Menu press: \n 1: to change directory name \n "
            "2: print amount of all files \n "
            "3: print amount of folders \n "
            "4: print all files of directory \n " 
            "5: create a new file \n "
            "6: create a new directory \n "
            "7: work with file \n "
          )
    command_id = int(input())
    if command_id == 0:
        print(os.getcwd())
    if command_id == 10:
        print(os.chdir(path))
    if command_id == 1:
        print ("Which directory name you need to change:")
        directory_name = input()
        print ("write new name of the direcotry:")
        new_name = input()
        os.rename(directory_name, new_name)
    if (command_id == 2):
        files = os.listdir()
        print (len(files))
    if (command_id == 3):
        files = os.listdir()
        folder  = 0
        for x in files:
            if (os.path.isdir(x)):
                folder += 1
        print (folder)
    if (command_id == 4):
        files = os.listdir()
        print (files)
    if (command_id == 5):
        print ("write the name of the file:")
        file_name = input()
        open(file_name, "w+").close()
    if (command_id == 6):
        print ("Enter the name of the directory")
        d_name = input()
        os.mkdir(d_name)
    if (command_id == 7):
        print ("Enter name of the file")
        f_name = input()
        f = open(f_name, "a+")
        while (True):
            print ("print file editing option: \n b:  to change file name \n "
            "a:  delete the file \n "
            "c:  edit the file \n "
            "d:  return to the menu \n " 
            )
            c = input()
            
            if (c == 'b'):
                f.close()
                print ("write the new name of the file")
                new_file_name = input()
                os.rename(f_name, new_file_name)
            if (c == 'a'):
                f.close()
                os.remove(f_name)
                break
            if (c == 'c'):
                f = open(f_name, "a+")
                print ("What to append to the file:")
                s = input()
                f.write(s)
                f.close()
            if (c == 'd'):
                break