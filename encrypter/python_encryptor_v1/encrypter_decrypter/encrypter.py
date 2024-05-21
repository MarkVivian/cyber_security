from cryptography.fernet import Fernet
import os
import shutil

class Encrypter:
    def __init__(self):
        self.key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "encryption_key.key")
        self.key = self.load_key()

    def generate_key(self):
        """Generate a new encryption key and save it to the specified file."""
        key = Fernet.generate_key()  # Generate a new encryption key
        with open(self.key_path, "wb") as key_file:  # Open the key file in binary write mode
            key_file.write(key)  # Write the key to the file
        return key  # Return the generated key

    def load_key(self):
        """Load the encryption key from the specified file or generate a new key if the file doesn't exist."""
        if os.path.exists(self.key_path):  # Check if the key file exists
            with open(self.key_path, "rb") as key_file:  # Open the key file in binary read mode
                return key_file.read()  # Read the key from the file
        else:
            return self.generate_key()  # Generate a new key if the file doesn't exist

    def encrypt_file(self, input_file):
        """Encrypt the specified file using the provided encryption key."""
        with open(input_file, "rb") as file:  # Open the input file in binary read mode
            data = file.read()  # Read the contents of the file

        fernet = Fernet(self.key)  # Create a Fernet cipher instance with the provided key
        encrypted_data = fernet.encrypt(data)  # Encrypt the data using Fernet encryption

        output_file = input_file + "_encrypted"  # Define the output file path
        with open(output_file, "wb") as file:  # Open the output file in binary write mode
            file.write(encrypted_data)  # Write the encrypted data to the output file

        return output_file  # Return the path of the encrypted file

    def encrypt_folder(self, input_folder):
        """Encrypt the specified folder and delete the original after encryption."""
        output_folder = input_folder + "_encrypted"  # Define the output folder path
        os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist

        for root, dirs, files in os.walk(input_folder):  # Iterate over all files and subdirectories in the input folder
            rel_dir = os.path.relpath(root, input_folder)  # Get the relative directory path
            output_dir = os.path.join(output_folder, rel_dir)  # Define the output directory path
            os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

            for filename in files:  # Iterate over all files in the current directory
                input_file = os.path.join(root, filename)  # Get the full path of the input file
                self.encrypt_file(input_file)  # Encrypt the current file

        try:
            shutil.rmtree(input_folder)  # Delete the original folder after encryption
        except Exception as e:
            print("Error:", e)
            print("Some files could not be deleted. Please delete the original folder manually.")
