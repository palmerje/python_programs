import colorgram

# Get colors from one of the Hirst painting photos
rgb_colors = []
colors = colorgram.extract('hirst_painting.jpg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
print(rgb_colors)
