# Name of NewGRF, as it appears in file names
newgrf_name = "JPplusShinkansen" + ".grf"

# Do you want to copy the completed NewGRF to your OpenTTD folder? (True/False)
copy_bool = True

# What is the path of your OpenTTD folder?
openttd_path = "/home/john/.local/share/openttd/newgrf"

import shutil

if copy_bool == True:
    print("Copying NewGRF to OpenTTD folder")
    shutil.copy(newgrf_name, openttd_path )
else:
    print("Complete. Did not copy.")
