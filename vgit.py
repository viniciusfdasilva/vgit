#!/bin/python

import os

SUCCESS_EXIT = 0
FAILURE_EXIT = 1

POSIX_SYSCALL_SUCCESS = 0

INSERT_URL_FLAG = 1
SELECT_URL_FLAG = 2
CLEAN_FILE      = 3

def panic(message):
    print(message)
    exit(FAILURE_EXIT)
    
    
def get_banner():
    print('\n*****************************************************\n')
    print('Welcome to vgit:\n')
    print('Author: Vinicius F. da Silva')
    print('Year: 2023\n')
    print('*****************************************************\n')
        
def success(message):
    print(message)
    exit(SUCCESS_EXIT)
      
        
def insert_url():
    
    remote_url = input('Type your remote url: \n')
    status = os.system(f'echo {remote_url} >> ./.git/vgit_remotes')
    
    panic('Insert error') if status != POSIX_SYSCALL_SUCCESS else success('Url inserted successfully!')


def get_urls():
    
    urls = []
    
    try:
        
        with open(file='./.git/vgit_remotes', mode='r') as gitfile:
            
            urls = gitfile.read().split('\n')
        
    except Exception:
        panic('Urls not found')

    return urls[0:len(urls)-1]

def select_url():
    
    urls = get_urls()
    
    i = 1
    
    for url in urls:
        
        print(f'[{i}] - {url}')
        i += 1
        
    try:
        option = int(input('\nSelect url\n'))
    except Exception:
        panic('Wrong option')
        
    if option < 1 or option > len(urls):
        panic('Wrong option')
        
    os.system('git remote remove origin >/dev/null')    
    status = os.system(f"git remote add origin {urls[option-1]} >/dev/null")
    
    panic('Insert error') if status != POSIX_SYSCALL_SUCCESS else success('Remote origin add successfully!')
        
def clean_file():
    
    status = os.system('rm ./.git/vgit_remotes')
    success('File cleaned successfully') if status == POSIX_SYSCALL_SUCCESS else panic('File clean process error')
    
def menu():
    
    get_banner()
    
    try:
        option = int(input(' [1] - Insert a new remote url to repository\n [2] - Select a remote url\n [3] - Clean file \n'))
        
    except Exception:
        panic('Wrong option')
    
    if option == INSERT_URL_FLAG:
        insert_url()
    elif option == SELECT_URL_FLAG:
        select_url()
    elif option == CLEAN_FILE:
        clean_file()
    else:
        panic('Wrong option')
    
        
def main():
    
    if os.path.exists('./.git'):
        menu()
    else:
        panic('This folder is not a git repository')

if __name__ == '__main__':
    main()