###FILE CREATION PROGRAM

import sys, os
from random import randint
from datetime import datetime

#check if there is a main dir if not create one
current = os.listdir(os.getcwd())
if 'main_directory' not in current:
    os.mkdir('main_directory')

def directories_total(directory= os.getcwd()):
    """Function to list directories 

    Args:
      directory: path to list directories from, default 'Current directory'

    Returns:
      list: list of folders created to cwd
    """   
    return os.listdir(directory)

def name_generator():
    """Creates a file name containing current date followed by a random number

    Returns:
      string: a file name in the format DD_MM_YYYY_XXXXX
    """ 
    folder_date = str(datetime.now().strftime('%d_%m_%Y'))
    file_name_tail = '_' + str(randint(10000,50001))
    return folder_date + file_name_tail

def create_dir(file_name):
    os.mkdir(f'main_directory\\{file_name}')

def help_text():
    print("""
Valitse yksi:
1) Luo kansio satunnaisella nimellä
2) Luo kansio nimellä
3) Tarkista montako kansiota on luotu
4) Poistu\n""")

#Loop time!

while True:
    help_text()
    command = input("Syötä toiminto: ")

    if command == '1':
        
        try:
            folder_name = name_generator()
            create_dir(folder_name)
            print(f"Luotiin kansio nimellä {folder_name}")
        except FileExistsError:
            print(f"Olet jo luonut kansion nimellä: {folder_name}")
            create_dir(name_generator())
    
    if command == '2':
        
        folder_name_manual = input("Syötä luotavan kansion nimi: ")
        try:
            create_dir(folder_name_manual)
            print(f"Luotiin kansio nimellä {folder_name_manual}")
        except FileExistsError:
            print(f"Olet jo luonut kansion nimellä: {folder_name_manual}")
            create_dir(name_generator())


    if command == '3':
        files_created = len(directories_total("main_directory"))
        print(f"Olet luonut {files_created} kansiota.")

    if command == '4':
        print("Kiitos ohjelman käytöstä!")
        break


            

