import colorsys
import random


def generate_random_color():
    h = random.random()
    s = 0.5 + random.random() / 2.0
    v = 0.5 + random.random() / 2.0
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"


def generate_random_theme():
    theme_type = random.choice(
        ["Monochromatic", "Analogous", "Complementary", "Split Complementary"]
    )
    base_color = generate_random_color()
    h, s, v = colorsys.rgb_to_hsv(
        int(base_color[1:3], 16) / 255.0,
        int(base_color[3:5], 16) / 255.0,
        int(base_color[5:7], 16) / 255.0,
    )

    if theme_type == "Monochromatic":
        colors = [colorsys.hsv_to_rgb(h, s * i, v * i) for i in [1, 0.8, 0.6, 0.4, 0.2]]
    elif theme_type == "Analogous":
        colors = [
            colorsys.hsv_to_rgb((h + i / 12.0) % 1.0, s, v) for i in [-1, 0, 1, 2, 3]
        ]
    elif theme_type == "Complementary":
        colors = [
            colorsys.hsv_to_rgb((h + i / 2.0) % 1.0, s, v) for i in [0, 0.5, 1, 1.5, 2]
        ]
    elif theme_type == "Split Complementary":
        colors = [
            colorsys.hsv_to_rgb((h + i / 3.0) % 1.0, s, v) for i in [0, 1, 2, 3, 4]
        ]

    colors = [
        f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}" for r, g, b in colors
    ]
    return {
        "Text": colors[0],
        "Background": colors[1],
        "Primary": colors[2],
        "Secondary": colors[3],
        "Accent": colors[4],
    }
