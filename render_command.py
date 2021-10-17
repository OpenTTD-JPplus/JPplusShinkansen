#################################
####### SET UP FILES HERE #######
#################################

# Vehicle Name - this will also be the name of the folder the sprites will appear in the NewGRF's folder
vehicle_name = "e5_series"
vehicle_part = "cab"

# Manifests to use - I use several to get the size I want
vehicle_manifest = "12_standard_manifest_4"

# select zoom levels desired, options are 1,2,4
zoom_levels = "1,2"

# File and Folder locations

# Source folder (i.e. the MagicaVoxel folder) - much easier to store with MagicaVoxel to work on and then run this script when sprites are wanted
src_folder = r"/home/john/Applications/MagicaVoxel/vox/JPplusShinkansen/"
# Destination folder - i.e. in the NewGRF folder which the sprites are for. This will also copy the voxels beforehand to allow production of the sprites
dst_folder = r"/home/john/Projects/JPplusShinkansen/voxel/" 

#################################
# NO NEED TO CHANGE STUFF BELOW #
#################################

import subprocess
import shutil
import os

# Voxel to copy
voxel = vehicle_name + "_" + vehicle_part

# Copy voxel from MagicaVoxel folder to NewGRF folder
src_path = src_folder + voxel + ".vox"
dst_path = dst_folder + voxel + ".vox"
shutil.copy(src_path, dst_path)
print("'" + voxel+ ".vox' voxel transferred from MagicaVoxel to NewGRF voxel folder")

input_voxel = "voxel/" + voxel+ ".vox"                                      # Which voxel is to be used by GoRender
manifest_path = "voxel/manifest/" + vehicle_manifest + ".json"              # Which manifest is to be used by GoRender
output_sprite = "src/gfx/" + vehicle_name + "/" # + manifest_size           # Where the produced sprites will be sent       

output_sprite_path = output_sprite + ".png"                                 # What the produced sprites will be called

if os.path.exists(output_sprite_path):
    os.remove(output_sprite_path)

gorender = subprocess.run(["./renderobject", "-input", input_voxel, "-m", manifest_path, "-output", output_sprite, "-8", "-palette", "/home/john/Applications/gorender/files/ttd_palette.json", "-scale", zoom_levels], stdout = subprocess.PIPE, text=True)
print(gorender.stdout)
print("'" + voxel + ".png' sprites produced from '" + voxel+ ".vox'")
