
Generate a palette from the video

    ffmpeg -y -i file.webm -vf palettegen palette.png

Then,

    ffmpeg -y -i file.webm -i palette.png -filter_complex paletteuse -r 10 -s 320x480 file.gif

