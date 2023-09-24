import os
import sys
import zipfile

folder_of_this_script = os.path.dirname(os.path.abspath(__file__))
files = [f for f in os.listdir(folder_of_this_script) if "part" in f]
print("Joining " + str(len(files)) + " parts...")
num_of_parts = len(files)
big_file_bytes = open(folder_of_this_script + "/big.zip", "wb")
for i in range(num_of_parts):
    part_name = folder_of_this_script + "/part" + str(i) + ".zip"
    part_bytes = open(part_name, "rb")
    big_file_bytes.write(part_bytes.read())
    part_bytes.close()
big_file_bytes.close()
files_dst = folder_of_this_script + "/../models/"
print("Extracting to " + files_dst)
with zipfile.ZipFile(folder_of_this_script + "/big.zip", "r") as zip_ref:
    zip_ref.extractall(files_dst)
os.remove(folder_of_this_script + "/big.zip")


