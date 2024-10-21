from PIL import Image

shinkansen = {
    "300_series"  : "300_series",
    "500_series"  : "500_series",
    "700_series"  : "700_series",
    "n700_series"  : "n700",
    "800_series"  : "800_series",
    "e1_series"   : "e1_series_irl",
    "l0_series"   : "l0_series",
    "e2_series"   : "e2_series_red",
    "200_series"   : "200_series_roundnose",
    "e6_series"   : "e6_series",
    "e3_series"   : "e3_r",
    "400_series"   : "400_series",
    "e8_series"   : "e8_series",
}

area = (267, 1, 307, 16)

for s in shinkansen:

    img = Image.open("src/trains/" + s +"/gfx/" + shinkansen[s] + ".png")
    
    purchase_sprite = img.crop(area)
    purchase_sprite.save("src/purchase/" + s + ".png")