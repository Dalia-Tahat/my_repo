import pyminizip
import hashlib

def md5_hash(text):
    #MD5 hash of  text
    return hashlib.md5(text.encode()).hexdigest()

def main():
    inputF = 'secret.txt'
    namesF = 'ListOfNames.txt'

    # Read the list of names
    with open(namesF, 'r') as file:
        ns = [line.strip() for line in file if line.strip()]

    # Compress the file multiple times
    for i, name in enumerate(ns):
        outputF = f"{name}.zip"
        password = md5_hash(name)
        
        # Compress the file using pyminizip
        # compression level between 1 and 9.(medium 5)
        pyminizip.compress(inputF, None, outputF, password, 5)
        print(f"Compressed {inputF} to {outputF} with password {password}")
        
        # Update inputF to the newly created zip file for the next iteration
        inputF = outputF

if __name__ == "__main__":
    main()
            
