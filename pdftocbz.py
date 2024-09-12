import glob
import os
import shutil

path = glob.glob("*.pdf")
print("INFO: Getting all PDF files...")

print("INFO: Creating output folder...")
if not os.path.exists("output"):
    os.makedirs("output")

index = 1
for file in path:
    folder = file.replace(".pdf", "")
    os.makedirs(folder)

    print("INFO: Converting PDF " + str(index) + " to folder...")
    os.system("pdftoppm " + "-png " + file + " " + folder + "/img")

    print("INFO: Zipping folder...")
    shutil.make_archive(folder, "zip", folder)

    print("INFO: Converting ZIP " + str(index) + " to CBZ...")
    os.system("cbconvert convert --format avif --quality 48 --no-nonimage=true --outdir output/ " + folder + ".zip")

    index += 1
