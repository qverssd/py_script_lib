from collections import Counter
from PIL import Image
import os

def get_dominant_color(image_path, resize=100):
    if not os.path.exists(image_path):
        print("File is not found")
        return
    
    img = Image.open(image_path)
    img = img.resize((resize, resize))
    pixels = list(img.getdata())

    most_common = Counter(pixels).most_common(1)[0][0]
    hex_color = '#{:02x}{:02x}{:02x}'.format(*most_common)

    print(f"Dominant color (RGB): {most_common}")
    print(f"Dominant color (HEX): {hex_color}")

if __name__ == "__main__":
    path = input("Add image path: ")
    get_dominant_color(path)