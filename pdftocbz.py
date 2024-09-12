import glob
import os
import shutil

print("INFO: Getting all PDF files...")
path = glob.glob("*.pdf")
path.sort()

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

    zip = folder + ".zip"

    print("INFO: Converting ZIP " + str(index) + " to CBZ...")
    os.system("cbconvert convert --format avif --quality 48 --no-nonimage=true --outdir output/ " + zip)

    index += 1
    shutil.rmtree(folder)
    os.remove(zip)
