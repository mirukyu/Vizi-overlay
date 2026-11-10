import json
import re
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from datetime import datetime

def add_vizi_overlay(img, filename=None):
    img = img.convert("RGBA")
    width, height = img.size

    meta = img.info
    desc = meta.get("Description")

    if not desc:
        raise Exception("No VRCX metadata found")

    data = json.loads(desc)

    photographer = data["author"]["displayName"]
    world = data["world"]["name"]
    player_count = len(data["players"])

    date_str = "Unknown date"
    if filename:
        basename = os.path.basename(filename)
        match = re.search(r"(\d{4})-(\d{2})-(\d{2})", basename)
        if match:
            date_str = match.group(0)

    line1 = "VIZI.SH"
    line2 = f"{world}"
    line3 = f"by {photographer}"
    line4 = f"{player_count} players"
    line5 = date_str

    font_big = ImageFont.truetype("arialbd.ttf", int(height * 0.035))
    font_small = ImageFont.truetype("arial.ttf", int(height * 0.02))
    font_date = ImageFont.truetype("arial.ttf", int(height * 0.018))

    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)

    margin = int(width * 0.02)
    spacing = 10

    def measure(text, font):
        box = draw.textbbox((0,0), text, font=font)
        return box[2]-box[0], box[3]-box[1]

    w1,h1 = measure(line1, font_big)
    w2,h2 = measure(line2, font_small)
    w3,h3 = measure(line3, font_small)
    w4,h4 = measure(line4, font_small)
    w5,h5 = measure(line5, font_date)

    box_w = max(w1,w2,w3,w4,w5) + margin
    box_h = h1+h2+h3+h4+h5 + spacing*6

    x = margin
    y = height - box_h - margin

    def text_shadow(pos, text, font):
        px,py = pos
        draw.text((px+2,py+2), text, font=font, fill=(0,0,0,200))
        draw.text((px,py), text, font=font, fill=(255,255,255,235))

    text_shadow((x+margin//2, y+spacing), line1, font_big)
    text_shadow((x+margin//2, y+h1+spacing*2), line2, font_small)
    text_shadow((x+margin//2, y+h1+h2+spacing*3), line3, font_small)
    text_shadow((x+margin//2, y+h1+h2+h3+spacing*4), line4, font_small)
    text_shadow((x+margin//2, y+h1+h2+h3+h4+spacing*5), line5, font_date)

    final = Image.alpha_composite(img, overlay)
    return final