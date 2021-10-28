#################################
####### SET UP FILES HERE #######
#################################

# Name of NewGRF, as it appears in file names
newgrf_name = "JPplusShinkansen"

# Files which should be first, in order (header, cargotable, etc)
header_stuff = [
    "header", 
    "basecosts",
    "railtypetable", 
    "cargotable", 
    "parameters", 
    "template",
    "vehicleid",
    #"wagon_attach",
    "dummy",            # dummy / empty sprites for 'invisible' sprites
    "mucar",
    "functions",  
    "sorting",
    "stats",
    "grfintegration",
    "grfoverrides"]

# Files to place in alphabetical order below
trains = [
    "0_series",
    #"e6_series",
    "e6_series",
    "e5_series",
    "e4_series",
    "e3_series"
    ]

# Do you want to copy the completed NewGRF to your OpenTTD folder? (True/False)
copy_bool = True

# What is the path of your OpenTTD folder?
openttd_path = "/home/john/.local/share/openttd/newgrf"

#################################
# NO NEED TO CHANGE STUFF BELOW #
#################################

# Thanks to Andythenorth for much of this code

import codecs
import subprocess
import shutil

# Get the version number from the custom tags file to use in the filename
with open("src/custom_tags.txt") as v:
    lines = v.read() 
    first = lines.split('\n', 1)[0]
version = first.split(":")[1]


# Create an empty list where all the NML code will be placed
sections = []

# Function for copying header_stuff code from the .nml files
def append_code(file):
    filename = "src/{}.nml"
    stuff = codecs.open(filename.format(file),'r','utf8')
    print("Merging", filename.format(file))
    sections.append(stuff.read())
    stuff.close()

# Append header stuff which should always be first
for i in header_stuff:
    append_code(i)

# Function for copying trains code from the .nml files
def append_trains(file):
    filename = "src/trains/{}.nml"
    stuff = codecs.open(filename.format(file),'r','utf8')
    print("Merging", filename.format(file))
    sections.append(stuff.read())
    stuff.close()

# Sort the unordered list for readability in the printout, then append to the list
trains.sort()
for i in trains:
    append_trains(i)

merged_nml_path = "src/merged/" + newgrf_name + "_v" + version +".nml"
grf_name = newgrf_name + "_v" + version + ".grf"

# Write the content of 'sections' into a file and save it
processed_nml_file = codecs.open(merged_nml_path,'w','utf8')
processed_nml_file.write('\n'.join(sections))
processed_nml_file.close()

print("#### nmlc ####")

# Run 
nmlc = subprocess.run(["nmlc", "-c", "-t", "src/custom_tags.txt", "-l", "src/lang", "--grf", grf_name, merged_nml_path], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text=True)
print(nmlc.stdout)
print(nmlc.stderr)

if copy_bool == True:
    print("Copying NewGRF to OpenTTD folder")
    shutil.copy(grf_name, openttd_path )
else:
    print("Complete. Did not copy.")
