# A program that copies the first 10 bytes into another file.

with open("file.txt", "rb") as file1:
    # the rb stands for read and bit
    with open("file_copied.txt", "wb") as file2:
        # wb = write and bit.
        # The first 10 byte is copied into the buffer
        buf = file1.read(10)
        # the buffer is written into the second file. Note that the number of file can be increased if you desire so
        file2.write(buf)
        file2.close()
    file1.close()
print("File has been copied")