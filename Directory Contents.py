import os

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)



    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    """

print print_directory_contents('/Users/anayat/documents')