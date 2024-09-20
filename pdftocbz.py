import glob
import os
import shutil
import sys

choice = input("Choose 1 for AVIF\nChoose 2 for WEBP")

if choice == "1":
    format = "avif"
    quality = "48"

elif choice == "2":
    format = "webp"
    quality = "55"

else:
    print("Wrong input, use any key to exit...")
    sys.exit(0)


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

    print("INFO: Converting PDF " + folder + " to folder...")
    os.system("pdftoppm " + "-png " + file + " " + folder + "/img")

    temppath = glob.glob(folder + "/*")
    temppath.sort()
    pic = temppath[0]
    os.remove(pic)
    tempfile = pic.split("/")[1]

    os.system("mutool convert -F png -o " + tempfile.replace("1", "") + " " + file + " 1")
    shutil.copyfile(tempfile, folder + "/" + tempfile)


    print("INFO: Zipping folder...")
    shutil.make_archive(folder, "zip", folder)

    zip = folder + ".zip"

    print("INFO: Converting ZIP " + folder + " to CBZ...")
    os.system("cbconvert convert --format " + format + " --quality " + quality + " --no-nonimage=true --outdir output/ " + zip)

    index += 1
    shutil.rmtree(folder)
    os.remove(zip)
    os.remove(tempfile)
