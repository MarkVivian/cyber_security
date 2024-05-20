from cryptography.fernet import Fernet
import os
import shutil

class Decrypter:
    def __init__(self):
        self.keys_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys")

    def load_key(self, key_name):
        """Load the encryption key corresponding to the provided key name."""
        key_path = os.path.join(self.keys_directory, key_name + "_key.key")
        if os.path.exists(key_path):  # Check if the key file exists
            with open(key_path, "rb") as key_file:  # Open the key file in binary read mode
                return key_file.read()  # Read the key from the file
        else:
            raise FileNotFoundError("Key file not found for decryption.")

    def decrypt_file(self, input_file):
        """Decrypt the specified file using the corresponding encryption key."""
        key_name = os.path.splitext(os.path.basename(input_file))[0].split("_encrypted")[0]
        key = self.load_key(key_name)

        with open(input_file, "rb") as file:  # Open the input file in binary read mode
            encrypted_data = file.read()  # Read the encrypted data from the file

        fernet = Fernet(key)  # Create a Fernet cipher instance with the provided key
        decrypted_data = fernet.decrypt(encrypted_data)  # Decrypt the data using Fernet decryption

        output_file = os.path.splitext(input_file)[0]  # Define the output file path without the '.encrypted' extension
        with open(output_file, "wb") as file:  # Open the output file in binary write mode
            file.write(decrypted_data)  # Write the decrypted data to the output file

        return output_file  # Return the path of the decrypted file

    def decrypt_folder(self, input_folder):
        """Decrypt the specified folder and delete the original after decryption."""
        key_name = os.path.basename(input_folder).split("_encrypted")[0]
        key = self.load_key(key_name)

        output_folder = os.path.dirname(input_folder)  # Define the output folder path
        os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist

        for root, dirs, files in os.walk(input_folder):  # Iterate over all files and subdirectories in the input folder
            rel_dir = os.path.relpath(root, input_folder)  # Get the relative directory path
            output_dir = os.path.join(output_folder, rel_dir)  # Define the output directory path
            os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

            for filename in files:  # Iterate over all files in the current directory
                input_file = os.path.join(root, filename)  # Get the full path of the input file
                self.decrypt_file(input_file)  # Decrypt the current file

        shutil.rmtree(input_folder)  # Delete the encrypted folder after decryption
