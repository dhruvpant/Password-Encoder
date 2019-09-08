from cryptography.fernet import Fernet
import sys

def generate_new_keyFile():
    try:
        handle = open("keyfile", "r")
        print("Keyfile already exists, cannot proceed")
        handle.close()
    except FileNotFoundError:
        key = Fernet.generate_key()
        file_handle = open("keyfile","w")
        file_handle.write(key.decode())
        file_handle.close()

def encrypt_string(decoded_string):
    key = ""
    encoded_string = ""
    try:
        handle = open("keyfile", "r")
        key = handle.read().strip()
        handle.close()
    except FileNotFoundError:
        print("Cannot open the keyfile")

    if key != "":
        cipher_suite = Fernet(key)
        encoded_string = cipher_suite.encrypt(decoded_string.encode('utf-8'))

    return encoded_string

def writeToFile(filename, encrypted_string):
    try:
        file_handle = open(filename,"w")
        file_handle.write(encrypted_string.decode())
        file_handle.close()
        print("Encrypted data written to "+filename)
    except:
        print("Cannot write to "+filename)

def showHelp():
    print('''
    Usage:
        Encoder.exe --generate_key_file         Generates a key file with the name of keyfile
        Encoder.exe --encrypt <plain text>      Encrypts the plain text using the keyfile
        Encoder.exe --encrypt <plain text> --file <File_name>   Encrypts the plain text using the keyfile and saves it to the specified file
    ''')


args = sys.argv
if len(sys.argv) < 2:
    showHelp()
else:
    if args[1] == "--generate_key_file":
        generate_new_keyFile()
    elif args[1] == "--encrypt":
        if(len(sys.argv) > 2):
            if args[2] != "":
                encrypted_string = encrypt_string(args[2].strip())
                if(len(sys.argv) > 3):
                    if args[3] != "" and args[3] == "--file":
                        if(len(sys.argv) > 4):
                            if args[4] != "":
                                writeToFile(args[4].strip(), encrypted_string)
                            else:
                                showHelp()
                        else:
                            showHelp()
                    else:
                        showHelp()
                else:
                    print(encrypted_string.decode())
            else:
                showHelp()
        else:
            showHelp()
    else:
        showHelp()
