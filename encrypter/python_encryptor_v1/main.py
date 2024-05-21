import os
from encrypter_decrypter.decrypter import Decrypter
from encrypter_decrypter.encrypter import Encrypter


def is_encrypted(path):
    """Check if the provided folder or file is encrypted."""
    if os.path.exists(path):
        if os.path.isdir(path):
            return path.endswith("_encrypted")
        elif os.path.isfile(path):
            return path.endswith(".encrypted")
    return False


if __name__ == "__main__":
    inputed_path = input("Enter the path of the folder or file you want to process: ")
    # Expand the tilde '~' character to represent the user's home directory
    input_path = os.path.expanduser(inputed_path)

    if os.path.exists(input_path):
        if os.path.isdir(input_path):
            if is_encrypted(input_path):
                decrypter = Decrypter()
                decrypter.decrypt_folder(input_path)
                print("Folder decrypted successfully!")
            else:
                encrypter = Encrypter()
                encrypter.encrypt_folder(input_path)
                print("Folder encrypted successfully!")
        elif os.path.isfile(input_path):
            if is_encrypted(input_path):
                decrypter = Decrypter()
                decrypter.decrypt_file(input_path)
                print("File decrypted successfully!")
            else:
                encrypter = Encrypter()
                encrypter.encrypt_file(input_path)
                print("File encrypted successfully!")
        else:
            print("Invalid path! Please provide a valid folder or file path.")
    else:
        print("Path does not exist! Please provide a valid path.")
