#!/bin/python

import os

SUCCESS_EXIT = 0
FAILURE_EXIT = 1

POSIX_SYSCALL_SUCCESS = 0

INSERT_URL_FLAG = 1
SELECT_URL_FLAG = 2

def get_remotes():
    pass

def panic(message):
    print(message)
    exit(FAILURE_EXIT)
        
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
        
def menu():
    
    print('Welcome to vgit:')
    
    try:
        option = int(input(' [1] - Insert a new remote url to repository\n [2] - Select a remote url\n'))
        
    except Exception:
        panic('Wrong option')
    
    if option == INSERT_URL_FLAG:
        insert_url()
    elif option == SELECT_URL_FLAG:
        select_url()
    else:
        panic('Wrong option')
    
        
def main():
    
    if os.path.exists('./.git'):
        menu()
    else:
        panic('This folder is not a git repository')

if __name__ == '__main__':
    main()