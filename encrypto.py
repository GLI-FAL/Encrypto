from os import system
from time import sleep
import os
import base64
import marshal
import hashlib
#Colors
W = "\033[1;39m"
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
P = "\033[1;35m"
U = "\033[1;36m"
#################
def hash_encrypt():
    system("clear")
    print (""+B+"     __  __           __    __    _ __          _______   __")
    sleep(0.3)
    print (""+B+"    / / / /___ ______/ /_  / /   (_) /_        / ____/ | / /")
    sleep(0.3)
    print (""+R+"   / /_/ / __ `/ ___/ __ \/ /   / / __ \______/ __/ /  |/ / ")
    sleep(0.3)
    print (""+R+"  / __  / /_/ (__  ) / / / /___/ / /_/ /_____/ /___/ /|  /  ")
    sleep(0.3)
    print (""+Y+" /_/ /_/\__,_/____/_/ /_/_____/_/_.___/     /_____/_/ |_/  \n")
 
    text = input (""+Y+"["+R+"+"+Y+"]"+W+" Enter The Word to encrypt"+Y+" :")
    encoded_txt = hashlib.md5(text.encode())
    print (encoded_txt.hexdigest())

def moon_encrypt():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'w', 'x', 'u', 'v', 'y', 'z']

    key = ['r', 'w', 'e', 'q', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
               'c', 'x', 'v', 'b', 'n', 'm']
    text = str(input(""+Y+"["+B+"+"+Y+"]"+B+" Enter the word to encrypt :"))

    cipher = []

    for l in text:
        key_number = letters.index(l)
        new_letters = key[key_number]
        cipher.append(new_letters)

    encrypt_text = ''.join(cipher)

    print(encrypt_text)

def moon_decrypt():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'w', 'x', 'u', 'v', 'y', 'z']

    key = ['r', 'w', 'e', 'q', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
               'c', 'x', 'v', 'b', 'n', 'm']

    text = str(input(""+G+"[+] Enter the word to decrypt :"))

    cipher = []
    for l in text:
        key_number = key.index(l)
        new_letters = letters[key_number]
        cipher.append(new_letters)
    encrypt_text = ''.join(cipher)

    print(encrypt_text)


def B64_encrypt():
    system("clear")
    print (""+B+" ____                          __ _  _ ")
    sleep(0.3)
    print (""+B+" |  _ \                        / /| || | ")
    sleep(0.3)
    print (""+R+" | |_) | __ _ ___  ___ ______ / /_| || |_")
    sleep(0.3)
    print (""+R+" |  _ < / _` / __|/ _ \______| '_ \__   _|")
    sleep(0.3)
    print (""+Y+" | |_) | (_| \__ \  __/      | (_) | | |")
    sleep(0.3)
    print (""+Y+" |____/ \__,_|___/\___|       \___/  |_|\n")
    input_file = str(input(''+B+'Enter '+Y+'Your '+R+'Path name.py '+B+': '))
    output_file = input_file
    with open(input_file, 'rb') as m:
        data = m.read()
        Data=base64.b64encode(data)
    with open(output_file, 'wb') as x:
        x.write(Data)
    xxx = open(output_file, 'r')
    data_ =  xxx.read()
    with open(output_file, 'w') as f:
        f.write('import base64\n')
        f.write('x = ( b\'\'\'')
        f.write(data_)
        f.write('\'\'\' )\n')
        f.write('exec (base64.b64decode(x))')
        print (''+B+'D'+Y+'o'+R+'n'+W+'e!')

def B64_decrypt():
    system ("clear")
    print (""+B+" ____                          __ _  _ ")
    sleep(0.3)
    print (""+B+" |  _ \                        / /| || | ")
    sleep(0.3)
    print (""+R+" | |_) | __ _ ___  ___ ______ / /_| || |_")
    sleep(0.3)
    print (""+R+" |  _ < / _` / __|/ _ \______| '_ \__   _|")
    sleep(0.3)
    print (""+Y+" | |_) | (_| \__ \  __/      | (_) | | |")
    sleep(0.3)
    print (""+Y+" |____/ \__,_|___/\___|       \___/  |_|\n")
    input_file = str(input(''+B+'Enter '+Y+'Your '+R+'Path name.py '+B+': '))
    output_file = input_file
    with open(input_file, 'rb') as f:
        data = f.read()
        data = data.replace(b'import base64',b'')
        data = data.replace(b'x = ( b\'\'\'',b'')
        data = data.replace(b'\'\'\' )',b'')
        data = data.replace(b'exec (base64.b64decode(x))',b'')
        Data = base64.b64decode(data)
    with open(output_file, 'wb') as f:
        f.write(Data)
        print (''+B+'D'+Y+'o'+R+'n'+W+'e!')


def Marsh():
    system("clear")
    print (""+U+"        __  ___                __          __      _______   __")
    sleep(0.1)
    print (""+U+"       /  |/  /___ ___________/ /_  ____ _/ /     / ____/ | / /")
    sleep (0.1)
    print (""+Y+"      / /|_/ / __ `/ ___/ ___/ __ \/ __ `/ /_____/ __/ /  |/ / ")
    sleep (0.1)
    print (""+Y+"     / /  / / /_/ / /  (__  ) / / / /_/ / /_____/ /___/ /|  /  ")
    sleep(0.1)
    print (""+R+"    /_/  /_/\__,_/_/  /____/_/ /_/\__,_/_/     /_____/_/ |_/  \n")
    file = input(""+B+"[+] Type Name File With Extension to encrypt with marshal--> : ")
    Open_Raed = open(file).read()
    Compel = compile(Open_Raed, '', 'exec')
    Dumps = marshal.dumps(Compel)
    Start = open('UnCode-' + file, 'w')
    Start.write('import marshal\n')
    Start.write('exec(marshal.loads(' + repr(Dumps) + '))')
    Start.close()
    print('[+] Done')
    print ('[+] The new encrypted file name UnCode-'+file)

def pyc_compile():
    print (""+P+"_ __  _   _  ___       ___ ___  _ __ ___  _ __ (_) | ___ ")
    sleep(0.3)
    print (""+P+"| '_ \| | | |/ __|____ / __/ _ \| '_ ` _ \| '_ \| | |/ _\ ")
    sleep(0.3)
    print (""+P+"| |_) | |_| | (_|_____| (_| (_) | | | | | | |_) | | |  __/")
    sleep(0.3)
    print (""+P+"| .__/ \__, |\___|     \___\___/|_| |_| |_| .__/|_|_|\___|")
    sleep(0.3)
    print (""+P+"|_|    |___/                              |_|             \n")
    x = input ("[+] ENTER YOUR FILE NAME : ")
    z = system ("python -m compileall "+x+"")
    print ("[+] you will Find The Compile encrypt file inside A Folder Named __pycache__ [+]")



while True :
        def main():
            system("clear")
        system("clear")
        print ("""
"""+B+"""

  .^
   .!
    ~!~:
   ..^!!~^.
   :^ .^~!!~^::.                                                          ::
   .~~:  .^~!!!!~^^..                                                     .!.
    .^!~^::..:^^~~!!!~~^::.                                              :~~
    ^..^~!!!~~^^^::^^!!!!!!~~~^^^::~:                         .       .:^!~::.
    .~^...:^~!!!!!!~~!!!!!!!!!!!!!!!!~^:                    .:~^^..:^~~!~^:^^
     .^!~~^::..^^^~~!!!!!!!!!!!!!!!!!!!~.                .^~!!!!!!!!!!!^^^~^
      .::~~!!~~~^^^^!!!!!!!!!!!!!!!!!!!!~             .:~!!!!!!!!!!!!!!~~^:
       .:::.:^^^~~!!!!!!!!!!!!!!!!!!!!!!!^          .^!!!!!!!!!!!!!!~^~^:.
         :^~~~^:^^^!!!!!!!!!!!!!!!!!!!!!!!~.       ^~!!!!!!!!!!!!!!!!~~^.
           .::~~~~~~~!!!!!!!!!!!!!!!!!!!!!!~:     ^!!!!!!!!!!!!!!!!~^.
                    .:~~!!!!!!!!!!!!!!!!!!!!!^:^^~!!!!!!!~~~~~~~~~^.
                      ..:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!^
                         .^!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~^:
                           :^!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!~.
                             .^~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:
                               .:^~!!!!!!!!!!!!!!!!!!!!!!!!~^!!^
                                   :!!!!!!!!!!!!!!!~^...:^~!:^!~
                                  .~!!!!!!!!!!!!~~:       ..^!~~^
                                 :~!!!!!!!!!!!~:.            ^~~!:
                               .^!!!!!!!!!!~~~~.             .~.~^
                             ^~!!!!!!!!!!~~:.  .:::.     .    :..:
                            ^!~!!!!!!!!!!^ .::::::~~::^^^~.
                            ^^^!!!!!!!!!!~   :~^~:^   ^:..
                              ^~~!!!!!!!~:   ..
                              :.~!!!!!~.
                                ^^!!~:.
                                 .~!^
                                  .^.
"""+R+"""
                        _____ _      _____ _______ ____________
                       / ____| |    |_   _|__   __/ ____| |  | |
                      | |  __| |      | |    | | | |    | |__| |
                      | | |_ | |      | |    | | | |    |  __  |
                      | |__| | |____ _| |_   | | | |____| |  | |
                       \_____|______|_____|  |_|  \_____|_|  |_|



""")
        print (""+R+"["+Y+"1"+R+"]"+W+" Encrypt-Base64")
        print (""+R+"["+Y+"2"+R+"]"+W+" Decrypt-Base64")
        print (""+R+"["+Y+"3"+R+"]"+W+" Encrypt-Marshal")
        print (""+R+"["+Y+"4"+R+"]"+W+" Encrypt-Compile")
        print (""+R+"["+Y+"5"+R+"]"+W+" cipher Word Encrypt")
        print (""+R+"["+Y+"6"+R+"]"+W+" cipher Word Decrypt")
        print (""+R+"["+Y+"7"+R+"]"+W+" encrypt monoalphabetic cipher")
        print (""+R+"["+Y+"8"+R+"]"+W+" decrypt monoalphabetic cipher")
        print (""+R+"["+Y+"9"+R+"]"+W+" haslib Word Encrypt")
        print (""+R+"["+Y+"10"+R+"]"+W+" Encrypt-Marshal-Base64")
        print (""+R+"["+Y+"0"+R+"]"+W+" To EXIT\n")
        p = input (""+R+"["+Y+"+"+R+"]"+W+" Enter Your Selection :")
        if p =='1':
            B64_encrypt()
            sleep(3.0)

        elif p =='2':
            B64_decrypt()
            sleep(3.0)

        elif p =='3':
            Marsh()
            sleep(3.0)

        elif p =='4':
            pyc_compile()
            sleep(3.0)

        elif p =='5':
            def encrypt(text,key):
                    cipher_list=[]
                    for l in text:
                        position = ord(l)
                        new_litter = chr(position+key)
                        cipher_list.append(new_litter)
                        t=''.join(cipher_list)
                        print(t)

            text=list(input(""+R+"["+Y+"+"+R+"] Enter word to encrypt :"))
            key=int(input(""+Y+"["+B+"+"+Y+"]"+B+" Enter the key:"))
            encrypt(text,key)
            sleep(6.0)

        elif p =='6':
            def encrypt(text,key):
                    cipher_list=[]
                    for l in text:
                        position = ord(l)
                        new_litter = chr(position-key)
                        cipher_list.append(new_litter)
                        t=''.join(cipher_list)
                        print(t)

            text=list(input(""+G+"[+] Enter word to Decrypt :"))
            key=int(input("[+] Enter the key :"))
            encrypt(text,key)
            sleep(6.0)

        elif p =='7':
            moon_encrypt()
            sleep(6.0)

        elif p =='8':
            moon_decrypt()
            sleep(6.0)

        elif p =='9':
            hash_encrypt()
            sleep(5.0)

        elif p =='10':
            B64_encrypt()
            Marsh()
            sleep(4.0)


        elif p =='0':
           break


main()

