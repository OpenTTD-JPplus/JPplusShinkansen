from PIL import Image

# Purchase Sprites

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
    "100_series"   : "100_series_irl",
    "0_series"   : "0_series_irl",
    "e4_series"   : "e4_series_yellow",
    "e5_series"   : "e5_series_pink",
    "e7_series"   : "e7_series",
}

area = (267, 1, 307, 16)

for s in shinkansen:

    img = Image.open("src/trains/" + s +"/gfx/" + shinkansen[s] + ".png")
    
    purchase_sprite = img.crop(area)
    purchase_sprite.save("src/purchase/" + s + ".png")

# Sprites

shinkansen = {
    "0_series" : {
        "0_series_irl" : 3,
        "0_series_2cc" : 3,
        "0_series_kodama" : 3,
        "0_series_nose" : 2,
        "922_series" : 3,
    },
    "100_series" : {
        "100_series_irl" : 5,
        "100_series_2cc" : 5,
        "100_series_kodama" : 3,
    },
    "300_series" : {
        "300_series" : 4,
        "300_series_2cc" : 4,
    },
    "400_series" : {
        "400_series" : 3,
        "400_series_2cc" : 3,
        "400_series_refurb" : 3,
        "400_series_refurb_2cc" : 3,
        "400_series_pantos" : 3,
    },
    "e2_series" : {
        "e2_series_red" : 3,
        "e2_series_pnk" : 3,
        "e2_series_200" : 7,
        "e2_series_2cc" : 3,
    },
    "e3_series" : {
        "e3_r" : 10,
        "e3_r_2cc" : 10,
        "e3_700" : 14,
        "e3_1000" : 8,
        "e3_1000_2cc" : 8,
        "e3_2000" : 8,
        "e3_2000_2cc" : 8,
    },
    "e4_series" : {
        "e4_series_yellow" : 3,
        "e4_series_pink" : 3,
        "e4_series_2cc" : 3,
    },
    "e5_series" : {
        "e5_series_pink" : 3,
        "e5_series_purple" : 3,
        "e5_series_2cc" : 3,
    },
    "e7_series" : {
        "e7_series" : 3,
        "e7_series_2cc" : 3,
    },
    "e8_series" : {
        "e8_series" : 4,
        "e8_series_2cc" : 4,
        "e8_series_green" : 4,
    },
}

for s in shinkansen:
    for c in shinkansen[s]:
        r = shinkansen[s][c]
        area = (0, 0, 309, r * 50 + 1 )
        img = Image.open("src/trains/" + s +"/gfx/" + c + ".png")
        sprite = img.crop(area)
        sprite.save("src/trains/" + s +"/gfx/" + c + ".png")
        