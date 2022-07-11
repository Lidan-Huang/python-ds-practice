# L = '''Fido
#        Whiskey
#        Dr. Sniffle'''

def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!
    # file1 = open(filename, 'w+')
    # file1.writelines(L)
    # file1.close()

    # file2 = open(filename, 'r')
    # lines = file2.readlines()

    # for line in lines:
    #     if line:
    #         print(f"- {line.strip()}")
    # file2.close()

    file1 = open(filename)

    for line in file1:
        print(f"- {line.strip()}")