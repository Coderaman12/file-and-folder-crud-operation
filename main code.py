from pathlib import Path
import os
from pydoc import pathdirs
from time import sleep
# initilization of project
print("--- APPLICATION STARTING ---")
sleep(3)
print("Loading",end="")
for i in range(3):
    sleep(1)
    print(".",end="")
print()
sleep(2)
print("--- APP INITILIZATION COMPLETED ---")

def Read_all_files_n_folders():
    path=Path("")
    for i,v in enumerate(path.rglob("*")):
        print(f"{i+1}. {v}")
    print("--- TOTAL FILE AND FOLDER PRESENT ---")

def Read_all_files():
    path=Path("")
    for i,v in enumerate(path.rglob("*.*")):
        if v.is_file():
            print(f"{i+1}. {v}")
    print("--- TOTAL FILE PRESENT ---")

while True:
    try:
        print("1.CREATE FOLDER\n2.UPDATE FOLDER NAME\n3.READ ALL FOLDERS\n4.DELETE FOLDER\n5.CREATE FILE\n6.UPDATE FILE\n7.RAED ALL FILES\n8.DELETE FILE\n0.EXIT APPLICATION.")
        n=int(input("Enter Your Choice: "))
        if n==1:
            pathdir=input("Enter Directory/Path name: ")
            path=Path(pathdir)
            path.mkdir(exist_ok=False)
            print("--- FOLDER CREATED SUCCESSFULLY ---")
        elif n==2:
            pathdir=input("Enter Directory/Path name: ")
            path=Path(pathdir)
            path.rename(input("Enter Updated Directory/Path name: "))
            print("--- FOLDER RENAMED SUCCESSFULLY ---")
        elif n==3:
            Read_all_files_n_folders()
            print("--- FOLDER READ SUCCESSFULLY ---")
        elif n==4:
            Read_all_files_n_folders()
            pathdir=input("Enter Directory/Path name to delete folder: ")
            path=Path(pathdir)
            folderdata=list(path.rglob("*"))
            if len(folderdata)>0:
                for i in folderdata:
                    if i.is_file():
                        os.remove(i)
                    else:
                        i.rmdir()
            path.rmdir()
            print("--- FOLDER DELETED SUCCESSFULLY ---")
        
        elif n==5:
            Read_all_files_n_folders()
            filepath=input("Enter File name/Path to create: ")
            with open(filepath,'w') as fw:
                txt=input("Want to Write SomeThings in File ?(press ENTER to skip): ")
                fw.write(txt)
            print("--- FILE CREATED SUCCESSFULLY ---")
        elif n==6:
            Read_all_files_n_folders()
            filepath=input("Enter File name/Path to update: ")
            flag=True
            while (flag==True):
                print("1.Rename File\n2.Replace File Data\n3.Append File Data\n0.For Exit in Update the File")
                ask=int(input("Choose any option: "))
                if ask==1:
                    os.rename(filepath,input("Enter New Name/Path: "))
                    print("--- FILE RENAMED SUCCESSFULLY ---")
                elif ask==2:
                    with open (filepath,'r') as fr,open (filepath,'w') as fw:
                        print("FILE DATA >> ",fr.read())
                        fw.write(input("START WRITEING FROM HERE >> "))
                        print("--- FILE REPLACED SUCCESSFULLY ---")
                elif ask==3:
                    with open (filepath,'r') as fr,open (filepath,'a') as fa:
                        print("FILE DATA >> ",fr.read())
                        fa.write(input("START WRITEING FROM HERE >> "))
                        print("--- FILE APPEND SUCCESSFULLY ---")
                elif ask==0:
                    print("---EXIT FROM THE UPDATEING PROCESS OF FILE ---")
                    flag=False
                else:
                    print("--- WRONG INPUT ---")
            print("--- FILE OPERATION SUCCESSFULLY DONE ---")
        elif n==7:
            Read_all_files()
            ask=input("Enter File Directory/Name to read the file: ")
            with open(ask,'r') as fr:
                print("File Data >> ",fr.read())
            print("--- FILE DATA READ SUCCESSFULLY ---")
        elif n==8:
            Read_all_files()
            ask=input("Enter File Directory/Name to delete the file: ")
            os.remove(ask)
            print("--- FILE DELETED SUCCESSFULLY ---")
        elif n==0:
            print("--- EXITNG PROCESS ---")
            sleep(3)
            print("Loading",end="")
            for i in range(3):
                sleep(1)
                print(".",end="")
            print()
            sleep(2)
            print("--- APP UNINITILIZED ---") 
            sleep(2)
            print("--- APPLICATION CLOSED ---")
            break              
    except Exception as err:
        print("ERROR >> ",err)