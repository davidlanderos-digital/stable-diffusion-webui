import os
import sys


if len(sys.argv) < 3:
    print("Usage: python split.py <big_zip_file>")
    sys.exit(1)


big_zip_file = sys.argv[1]

if not os.path.exists(big_zip_file):
    print("File not found: " + big_zip_file)
    sys.exit(1)

file_size = os.path.getsize(big_zip_file)

parts = file_size // 41943040

print("Splitting into " + str(parts) + " parts...")

part_size = file_size // parts
remainder = file_size % parts

# save all parts in the same directory as the big zip file
dir_name = os.path.dirname(big_zip_file)
big_file_bytes = open(big_zip_file, "rb")

for i in range(parts):
    part_name = os.path.join(dir_name, "part" + str(i) + ".zip")
    part_bytes = open(part_name, "wb")

    if i == parts - 1:
        # last part
        part_size += remainder

    part_bytes.write(big_file_bytes.read(part_size))
    part_bytes.close()

big_file_bytes.close()
