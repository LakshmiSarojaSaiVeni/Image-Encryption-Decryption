# Encryption part
try:
    # Take path of image as input
    path = r'C:\Users\Vinee\OneDrive\Desktop\Intership\Image1.jpg'
    
    # Take encryption key as input
    key = int(input('Enter Key for encryption of Image : '))
    
    # Print path of image file and encryption key
    print('The path of file : ', path)
    print('Key for encryption : ', key)
    
    # Open the file for reading in binary mode
    with open(path, 'rb') as fin:
        image = fin.read()
    
    # Convert image into byte array to perform encryption
    image = bytearray(image)
    
    # Perform XOR operation on each byte
    for index, values in enumerate(image):
        image[index] = values ^ key
    
    # Open the file for writing in binary mode
    with open(path, 'wb') as fout:
        fout.write(image)
    
    print('Encryption Done...')
    
except FileNotFoundError:
    print("Error: File not found. Please check the path.")
except PermissionError:
    print("Error: You don't have permission to modify this file.")
except Exception as e:
    print(f"An error occurred during encryption: {str(e)}")
